"""Busca DIRIGIDA na API GraphQL do TJBA pelo campo `assunto` (caixa de busca do portal; nao neutra, subconta) para cada tese da E4-3.
Consulta "IPTU <frase>" sem filtro de data (2º grau e Turmas Recursais), ate 60 itens (ementa) por tese.
Grava evidencias/dirigida/tjba-api-e43-2026-11-06.json e recibos em auditoria/buscas.jsonl (Q-DIR-E43-TJBAAPI-*).
Uso: python -I scripts/tjba_assunto_e43.py"""
import datetime as dt, json, os, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
URL = "https://jurisprudenciaws.tjba.jus.br/graphql"
Q = ("query($f:DecisaoFilter,$p:Int,$i:Int){ filter(decisaoFilter:$f,pageNumber:$p,itemsPerPage:$i){ itemCount "
     "decisoes{ numeroProcesso dataPublicacao tipoDecisao orgaoJulgador{ nome } relator{ nome } classe{ descricao } ementa } } }")
TZ = dt.timezone(dt.timedelta(hours=-3))


def chamar(f, p, i):
    body = json.dumps({"query": Q, "variables": {"f": f, "p": p, "i": i}}).encode()
    for t in range(4):
        try:
            r = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json", "Origin": "https://jurisprudencia.tjba.jus.br", "Referer": "https://jurisprudencia.tjba.jus.br/", "User-Agent": "pesquisa-juridica-escritorio"}, method="POST")
            return json.loads(urllib.request.urlopen(r, timeout=90).read())
        except Exception as e:
            time.sleep(5 * (t + 1)); err = str(e)
    return {"erro": err}


def main():
    T = json.load(open(J("estado", "E4-3", "teses.json"), encoding="utf-8"))["teses"]
    out = []
    for t in T:
        termo = 'IPTU AND "' + t["chave"] + '"'
        f = {"assunto": termo, "dataInicial": "2020-01-01", "dataFinal": "2026-11-05", "ordenadoPor": "dataPublicacao", "segundoGrau": True, "turmasRecursais": True, "tipoAcordaos": True, "tipoDecisoesMonocraticas": True}
        d = chamar(f, 0, 60)
        res = ((d.get("data") or {}).get("filter") or {})
        dec = res.get("decisoes") or []
        out.append({"n": t["n"], "nome": t["nome"], "termo": termo, "itemCount": res.get("itemCount"), "erro": d.get("erro") or d.get("errors"),
                    "itens": [{"numero": x.get("numeroProcesso"), "publicacao": (x.get("dataPublicacao") or "")[:10], "tipo": x.get("tipoDecisao"),
                               "orgao": (x.get("orgaoJulgador") or {}).get("nome"), "classe": (x.get("classe") or {}).get("descricao"),
                               "ementa": limpar_html(x.get("ementa"))[:3000]} for x in dec]})
        with open(J("auditoria", "buscas.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({"data": dt.datetime.now(TZ).isoformat(timespec="seconds"), "consulta": f"Q-DIR-E43-TJBAAPI-{t['n']}", "banco": "tjbaapi",
                                 "trilha": "dirigida", "assunto": termo, "itemCount": res.get("itemCount"), "retornados": len(dec)}, ensure_ascii=False) + "\n")
        print(t["n"], termo, res.get("itemCount"), len(dec), flush=True)
        time.sleep(1.5)
    json.dump({"fonte": URL, "aviso": "campo assunto = busca livre do portal; nao neutra; a API subconta (ver relatorio da rodada 1)", "teses": out},
              open(J("evidencias", "dirigida", "tjba-api-e43-2026-11-06.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
