"""Buscas DIRIGIDAS da E4-3 por tese (fora do denominador): DJEN por termo (TJBA) e PANGEA (FTS5, precedentes qualificados).
Le estado/E4-3/teses.json; grava evidencias/dirigida/<familia>-2026-11-06.json e recibos em auditoria/buscas.jsonl (Q-DIR-E43-*).
DJEN: comunicaapi.pje.jus.br, ate 2 paginas de 100 por frase, texto integral publicado (decisoes monocraticas inteiras; acordao = ementa).
Uso: python -I scripts/dirigida_e43.py [--familia F1_execucao_processo]"""
import argparse, collections, datetime as dt, json, os, sqlite3, time, urllib.error, urllib.parse, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
TZ = dt.timezone(dt.timedelta(hours=-3))
API = "https://comunicaapi.pje.jus.br/api/v1/comunicacao"


def djen(frase, paginas=2):
    itens, st = [], None
    for pag in range(1, paginas + 1):
        url = API + "?" + urllib.parse.urlencode({"texto": frase, "siglaTribunal": "TJBA", "pagina": pag, "itensPorPagina": 100})
        d = None
        for t in range(4):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "pesquisa-iptu/1.0", "Accept": "application/json"}), timeout=60) as r:
                    st = r.status; d = json.loads(r.read().decode("utf-8"))
                if (d or {}).get("status") == "error": time.sleep(8 * (t + 1)); d = None; st = "ocupado"; continue
                break
            except urllib.error.HTTPError as e:
                st = e.code
                if e.code in (429, 500, 502, 503, 504): time.sleep(5 * (t + 1)); continue
                break
            except Exception:
                time.sleep(5 * (t + 1))
        time.sleep(1.2)
        lote = (d or {}).get("items") or []
        itens += lote
        if len(lote) < 100: break
    return st, itens


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--familia"); a = ap.parse_args()
    T = json.load(open(J("estado", "E4-3", "teses.json"), encoding="utf-8"))["teses"]
    pg = sqlite3.connect("file:" + os.environ.get("PANGEA_DB", "<ACERVO>/PANGEA/pangea.db") + "?mode=ro", uri=True)
    cols = [r[1] for r in pg.execute("pragma table_info(precedentes)")]
    fam = collections.defaultdict(list)
    for t in T:
        if a.familia and t["familia"] != a.familia: continue
        agora = dt.datetime.now(TZ).isoformat(timespec="seconds")
        out = {"n": t["n"], "nome": t["nome"], "djen": [], "pangea": []}
        for fr in [t["chave"] + " IPTU"]:
            st, itens = djen(fr)
            out["djen"].append({"frase": fr, "http": st, "retornados": len(itens),
                                "itens": [{"numero": i.get("numeroprocessocommascara") or i.get("numero_processo"), "data": (i.get("data_disponibilizacao") or "")[:10],
                                           "orgao": i.get("nomeOrgao"), "tipo": i.get("tipoDocumento"), "texto": (i.get("texto") or "")[:6000]} for i in itens]})
            with open(J("auditoria", "buscas.jsonl"), "a", encoding="utf-8", newline="\n") as f:
                f.write(json.dumps({"data": agora, "consulta": f"Q-DIR-E43-DJEN-{t['n']}", "banco": "djen", "trilha": "dirigida", "frase": fr, "http": st, "retornados": len(itens)}, ensure_ascii=False) + "\n")
        try:
            rows = list(pg.execute(f"select {','.join(cols)} from precedentes where precedentes match ? limit 40", (t["pangea"],)))
        except sqlite3.Error as e:
            rows = []; out["pangea_erro"] = str(e)
        out["pangea"] = [{k: (str(v)[:3000] if v is not None else None) for k, v in zip(cols, r)} for r in rows]
        with open(J("auditoria", "buscas.jsonl"), "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps({"data": agora, "consulta": f"Q-DIR-E43-PANGEA-{t['n']}", "banco": "pangea", "trilha": "dirigida", "expr": t["pangea"], "retornados": len(rows)}, ensure_ascii=False) + "\n")
        fam[t["familia"]].append(out)
        print(t["n"], t["nome"][:40], "djen", [x["retornados"] for x in out["djen"]], "pangea", len(rows), flush=True)
    for f, lst in fam.items():
        json.dump({"familia": f, "gerado": dt.datetime.now(TZ).isoformat(timespec="seconds"), "trilha": "dirigida (fora do denominador)", "teses": lst},
                  open(J("evidencias", "dirigida", f"{f}-2026-11-06.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
