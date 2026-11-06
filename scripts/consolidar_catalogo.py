"""Confere e consolida o catalogo de teses (brief-catalogo-teses-v1): campos, enums e excerto literal na ementa do lote
(tolerancia so a espacos colapsados). Linha reprovada fica marcada (nao some). Gera analises/catalogo-teses-v1.json e .csv
e o resumo por tema x resultado. Recibos: auditoria/catalogo-teses-v1.jsonl. Uso: python -I scripts/consolidar_catalogo.py"""
import collections, csv, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import mapa_espacos, achar  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
RES = {"favoravel", "parcial", "desfavoravel", "sem_exame", "incerto"}


def main():
    cand = {json.loads(l)["id"]: json.loads(l) for f in ("candidatos-tjba.jsonl", "candidatos-tjbaapi.jsonl") for l in open(J("dados", f), encoding="utf-8")}
    linhas, faltam = [], []
    for p in sorted(glob.glob(J("estado", "catalogo", "lote-*.jsonl"))):
        ent = [json.loads(l) for l in open(p, encoding="utf-8")]
        sp = p.replace("lote-", "saida-")
        sai = {}
        if os.path.exists(sp):
            for l in open(sp, encoding="utf-8"):
                l = l.strip()
                if not l: continue
                try: s = json.loads(l); sai[s.get("id")] = s
                except json.JSONDecodeError: pass
        for e in ent:
            s = sai.get(e["id"]); erros = []
            if s is None: faltam.append(e["id"]); continue
            if s.get("resultado") not in RES: erros.append("resultado")
            if not isinstance(s.get("pertinente"), bool): erros.append("pertinente")
            ex = s.get("excerto") or ""
            c, pos = mapa_espacos(e["ementa"])
            if not (15 <= len(ex) <= 400) or achar(e["ementa"], c, pos, ex) is None: erros.append("excerto")
            r = cand.get(e["id"], {})
            linhas.append({"id": e["id"], "lote": os.path.basename(p), "numero": r.get("numero_processo"), "orgao": r.get("orgao"), "julgamento": r.get("data_julgamento"),
                           "classe": r.get("classe"), "pertinente": s.get("pertinente"), "resultado": s.get("resultado"), "tema": s.get("tema"), "tese": s.get("tese"),
                           "via": s.get("via"), "excerto": ex, "erros": erros})
    json.dump({"regra": "estado/brief-catalogo-teses-v1.md", "linhas": linhas, "faltam": faltam}, open(J("analises", "catalogo-teses-v1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(J("analises", "catalogo-teses-v1.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); cols = ["tema", "resultado", "tese", "numero", "orgao", "julgamento", "classe", "via", "pertinente", "id", "excerto", "erros"]
        w.writerow(cols)
        for l in sorted(linhas, key=lambda l: (str(l["tema"]), str(l["resultado"]), str(l["julgamento"]))): w.writerow([("|".join(l[c]) if isinstance(l[c], list) else l[c]) for c in cols])
    with open(J("auditoria", "catalogo-teses-v1.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for l in linhas: f.write(json.dumps({k: l[k] for k in ("id", "lote", "resultado", "tema", "erros")}, ensure_ascii=False) + "\n")
    sys.stdout.reconfigure(encoding="utf-8")
    ok = [l for l in linhas if not l["erros"] and l["pertinente"]]
    print("linhas", len(linhas), "faltam", len(faltam), "reprovadas", sum(bool(l["erros"]) for l in linhas), "nao_pertinentes", sum(l["pertinente"] is False for l in linhas))
    t = collections.defaultdict(collections.Counter)
    for l in ok: t[l["tema"]][l["resultado"]] += 1
    print(f"{'tema':38s} fav parc desf s/ex inc")
    for k in sorted(t, key=lambda k: -sum(t[k].values())):
        x = t[k]; print(f"{str(k):38s} {x['favoravel']:4d} {x['parcial']:4d} {x['desfavoravel']:4d} {x['sem_exame']:4d} {x['incerto']:4d}")


if __name__ == "__main__":
    main()
