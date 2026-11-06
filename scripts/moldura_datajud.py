"""Moldura amostral NEUTRA do 1o grau e do 2o grau (TJBA) pelo DataJud publico (metadados; sem decisao).
Uso legitimo aqui: METADADOS de classe/assunto/orgao para sortear processos (nunca movimento/prazo — regra da casa).
Consulta Q-NEUTRA-DATAJUD-01: assunto 5952 (IPTU, TPU/CNJ), todas as classes EXCETO Execucao Fiscal (moldura A).
Moldura B (Execucao Fiscal): so contagem por ano/orgao (660 mil; amostra futura).
Saida: dados/moldura-datajud-a.jsonl + recibo em auditoria/buscas.jsonl. Chave publica do CNJ lida do script da casa."""
import json, os, re, sys, time, urllib.request, datetime as dt
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENTE = r"<ecossistema-local>"
KEY = os.environ["DATAJUD_API_KEY"]  # chave publica da API do DataJud (CNJ), informada pelo ambiente
URL = "https://api-publica.datajud.cnj.jus.br/api_publica_tjba/_search"
CAMPOS = ["numeroProcesso", "classe", "orgaoJulgador", "dataAjuizamento", "grau", "assuntos", "sistema", "formato",
          "dataHoraUltimaAtualizacao", "nivelSigilo"]
QUERY = {"bool": {"must": [{"term": {"assuntos.codigo": 5952}}],
                  "must_not": [{"term": {"classe.codigo": 1116}}]}}  # 1116 = Execucao Fiscal (TPU)


def post(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": f"APIKey {KEY}", "Content-Type": "application/json"})
    for t in range(12):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                return json.load(r)
        except Exception as e:
            print("retry", t, e, file=sys.stderr); time.sleep(min(60, 5 * (t + 1)))
    raise SystemExit("DataJud indisponivel")


def main():
    ini = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds")
    tot = post({"size": 0, "track_total_hits": True, "query": QUERY})["hits"]["total"]["value"]
    out_p = os.path.join(RAIZ, "dados", "moldura-datajud-a.jsonl")
    n = 0; after = None; vistos = set(); dup = 0
    if os.path.exists(out_p):  # retomada: continua do ultimo _sort gravado
        for l in open(out_p, encoding="utf-8"):
            s0 = json.loads(l); n += 1; after = s0.get("_sort")
            vistos.add((s0.get("numeroProcesso"), s0.get("grau"), (s0.get("orgaoJulgador") or {}).get("codigo")))
        if after is None: n = 0; vistos = set(); open(out_p, "w").close()
    with open(out_p, "a", encoding="utf-8") as out:
        while True:
            body = {"size": 500, "query": QUERY, "_source": CAMPOS, "sort": [{"@timestamp": {"order": "asc"}}]}
            if after: body["search_after"] = after
            hits = post(body)["hits"]["hits"]
            if not hits: break
            for h in hits:
                s = h["_source"]; s["_id_datajud"] = h["_id"]; s["_sort"] = h.get("sort")
                k = (s.get("numeroProcesso"), s.get("grau"), (s.get("orgaoJulgador") or {}).get("codigo"))
                if k in vistos: dup += 1
                vistos.add(k)
                out.write(json.dumps(s, ensure_ascii=False) + "\n"); n += 1
            after = hits[-1]["sort"]
            print(n, "/", tot, flush=True); time.sleep(0.3)
    rec = {"consulta": "Q-NEUTRA-DATAJUD-01", "protocolo": "v1", "banco": "datajud-tjba", "fonte": URL,
           "expressao": json.dumps(QUERY), "campo": "assuntos.codigo / classe.codigo", "inicio": ini,
           "fim": dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds"),
           "retornados": tot, "coletados": n, "duplicatas_mesma_chave": dup, "ordem": "@timestamp asc (search_after)",
           "limite_conhecido": "DataJud publico tem defasagem; sigilo nao aparece; assunto cadastrado pela parte/serventia (ruido)",
           "situacao": "concluida" if n == tot else "parcial"}
    open(os.path.join(RAIZ, "auditoria", "buscas.jsonl"), "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(rec["situacao"], n, tot)


if __name__ == "__main__":
    main()
