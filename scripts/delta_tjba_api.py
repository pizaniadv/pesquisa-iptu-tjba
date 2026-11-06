"""Delta do TJBA ausente em acervo local (acervo local cobre 2020-01..2025-12) pela API GraphQL publica do TJBA (somente leitura).
Consulta Q-NEUTRA-TJBAAPI-01: assunto = termo neutro (protocolo v1 §4), segundo grau + turmas recursais,
acordaos + monocraticas, por mes. Grava em derivados/hits-tjbaapi.jsonl no MESMO formato de varrer_f.py
(arquivo = 'API:<mes>:<termo>', linha = posicao), para a triagem T1 tratar igual.
Calibracao de 05/11/2026 (03/2025): a busca por 'assunto' do portal devolveu 11 decisoes contra 131 da varredura
integral de acervo local -> NAO e neutra. Por isso o modo padrao e INTEGRAL: baixa todas as decisoes do mes (assunto vazio)
e filtra localmente com a MESMA expressao de varrer_f.py (Q-NEUTRA-01); so os acertos sao gravados.
Uso: python -I scripts/delta_tjba_api.py --de 2026-01 --ate 2026-11 [--contar] [--calibrar 2025-03]"""
import re
PRE = re.compile(r"(?i)(iptus?|i\.p\.t\.u|predial\s+e\s+territorial|propriedade\s+predial|imposto\s+predial|territorial\s+urbano)")
import argparse, json, os, sys, time, hashlib, urllib.request, datetime as dt, calendar
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "https://jurisprudenciaws.tjba.jus.br/graphql"
HDR = {"Content-Type": "application/json", "Origin": "https://jurisprudencia.tjba.jus.br", "Referer": "https://jurisprudencia.tjba.jus.br/",
       "User-Agent": "pesquisa-juridica-escritorio"}
CAMPOS = "id sourceId numeroProcesso codigoProcesso orgaoJulgador{id nome} relator{id nome} classe{id descricao} source instancia tipoDecisao dataPublicacao dataJulgamento dataAtualizacao conteudo ementa hash"
Q = "query($f:DecisaoFilter,$p:Int,$i:Int){ filter(decisaoFilter:$f,pageNumber:$p,itemsPerPage:$i){ itemCount pageCount decisoes{ %s } } }" % CAMPOS
TERMOS = ["IPTU", "predial AND territorial AND urbano", "imposto AND predial"]


def agora():
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds")


def post(f, p, i):
    body = json.dumps({"query": Q, "variables": {"f": f, "p": p, "i": i}}).encode()
    for t in range(6):
        try:
            req = urllib.request.Request(URL, data=body, headers=HDR, method="POST")
            with urllib.request.urlopen(req, timeout=180) as r:
                d = json.load(r)
            if "errors" in d: raise RuntimeError(str(d["errors"])[:300])
            return d["data"]["filter"]
        except Exception as e:
            print("retry", t, e, file=sys.stderr); time.sleep(4 * (t + 1))
    raise RuntimeError("API TJBA indisponivel")


def meses(de, ate):
    y, m = map(int, de.split("-")); Y, M = map(int, ate.split("-"))
    while (y, m) <= (Y, M):
        yield y, m
        m += 1
        if m == 13: y, m = y + 1, 1


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--de"); ap.add_argument("--ate"); ap.add_argument("--calibrar")
    ap.add_argument("--contar", action="store_true"); ap.add_argument("--modo", default="integral", choices=["integral", "assunto"])
    a = ap.parse_args()
    alvo = [tuple(map(int, a.calibrar.split("-")))] if a.calibrar else list(meses(a.de, a.ate))
    saida = os.path.join(RAIZ, "derivados", "hits-calibracao-api.jsonl" if a.calibrar else "hits-tjbaapi.jsonl")
    hoje = dt.date(2026, 11, 5)
    for (y, m) in alvo:
      ult = calendar.monthrange(y, m)[1]
      tot_mes = 0
      for dia in range(1, ult + 1):
        d0 = dt.date(y, m, dia)
        if d0 > hoje: break
        for termo in (TERMOS if a.modo == "assunto" else [""]):
            # fatia DIARIA: consulta mensal subconta (calibracao 03/2025: 8.407 x 31.044 em acervo local)
            f = {"assunto": termo, "orgaos": [], "relatores": [], "classes": [],
                 "dataInicial": f"{d0.isoformat()}T00:00:00.000Z", "dataFinal": f"{d0.isoformat()}T23:59:59.999Z",
                 "segundoGrau": True, "turmasRecursais": True, "tipoAcordaos": True, "tipoDecisoesMonocraticas": True,
                 "ordenadoPor": "dataPublicacao"}
            if a.contar:
                r = post(f, 0, 1); tot_mes += r["itemCount"]; continue
            ini = agora(); p = 0; n = 0; tot = None; pages = None; vistos = 0
            with open(saida, "a", encoding="utf-8") as out:
                while True:
                    r = post(f, p, 50)
                    tot, pages = r["itemCount"], r["pageCount"]
                    for d in r["decisoes"]:
                        vistos += 1
                        if a.modo == "integral" and not PRE.search((d.get("ementa") or "") + " " + (d.get("conteudo") or "")):
                            continue
                        linha = json.dumps(d, ensure_ascii=False, sort_keys=True)
                        out.write(json.dumps({"banco": "tjbaapi", "arquivo": f"API:{d0.isoformat()}:{termo or 'integral'}", "linha": n,
                                              "sha256_linha": hashlib.sha256(linha.encode()).hexdigest(), "familias": [termo],
                                              "registro": d}, ensure_ascii=False) + "\n"); n += 1
                    p += 1
                    if p >= (pages or 0) or not r["decisoes"]: break
                    time.sleep(0.4)
            rec = {"consulta": "Q-NEUTRA-TJBAAPI-01", "protocolo": "v1", "banco": "tjbaapi", "fonte": URL, "expressao": termo if a.modo == "assunto" else PRE.pattern,
                   "filtros": {k: v for k, v in f.items() if k != "assunto"}, "campo": "assunto (busca textual do portal)",
                   "campo_data": "dataPublicacao", "inicio": ini, "fim": agora(), "ordem": "dataPublicacao",
                   "registros_no_periodo": tot, "percorridos": vistos, "retornados": n if a.modo == "integral" else tot, "coletados": n, "paginas": pages, "itens_por_pagina": 50,
                   "situacao": ("concluida" if vistos == tot else "parcial") if a.modo == "integral" else ("concluida" if n == tot else "parcial"), "modo": a.modo, "calibracao": bool(a.calibrar)}
            open(os.path.join(RAIZ, "auditoria", "buscas.jsonl"), "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"{d0} [{termo or 'integral'}] {n}/{tot} percorridos={vistos}", flush=True)
      if a.contar: print(f"{y}-{m:02d} soma_diaria={tot_mes}", flush=True)


if __name__ == "__main__":
    main()
