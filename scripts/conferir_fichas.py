"""Confere as fichas da E4-3: cada excerto do JSON da ficha tem de estar LITERALMENTE (tolerancia so a espacos) em algum texto
dos pacotes (estado/E4-3/pacote-*.json), da base de ementas ou dos inteiros teores capturados (evidencias/pje2g, evidencias/pdpj).
Desde 06/11/2026 (revisao Codex, item 8) confere tambem a ATRIBUICAO: o excerto tem de estar num texto do mesmo processo
(campo `numero` do excerto, comparado pelos 20 digitos do CNJ). Resultado por excerto: atribuido | so_no_corpus (literal, mas nao
num texto daquele processo) | falha. Saida: auditoria/conferencia-fichas-e43.jsonl e resumo. Uso: python -I scripts/conferir_fichas.py"""
import collections, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import mapa_espacos  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
cnj = lambda s: re.sub(r"\D", "", s or "")[:20]


def textos(o, acc):
    if isinstance(o, dict):
        for v in o.values(): textos(v, acc)
    elif isinstance(o, list):
        for v in o: textos(v, acc)
    elif isinstance(o, str) and len(o) > 30: acc.append(o)


def por_processo(o, idx):
    """Indexa por processo cada objeto do pacote que tem `numero` (todos os seus textos)."""
    if isinstance(o, dict):
        n = cnj(o.get("numero")) if isinstance(o.get("numero"), str) else ""
        if len(n) == 20:
            acc = []; textos({k: v for k, v in o.items() if k != "numero"}, acc); idx[n].extend(acc)
        for v in o.values(): por_processo(v, idx)
    elif isinstance(o, list):
        for v in o: por_processo(v, idx)


def contem(tx, t):
    return tx in t or re.sub(r"\s+", " ", tx) in re.sub(r"\s+", " ", t)


def main():
    acc, idx = [], collections.defaultdict(list)
    for p in glob.glob(J("estado", "E4-3", "pacote-*.json")):
        o = json.load(open(p, encoding="utf-8")); textos(o, acc); por_processo(o, idx)
    for l in open(J("derivados", "ementas-candidatos.jsonl"), encoding="utf-8"):
        d = json.loads(l); acc.append(d.get("ementa") or ""); idx[cnj(d.get("numero"))].append(d.get("ementa") or "")
    num_do_id = {}
    for p in glob.glob(J("dados", "decisoes", "*.json")):
        r = json.load(open(p, encoding="utf-8")); num_do_id[r["id"]] = cnj(r["identificacao"]["numero_processo"].get("original"))
    for p in glob.glob(J("evidencias", "pje2g", "*", "*.txt")) + glob.glob(J("evidencias", "pdpj", "*", "*.txt")) + glob.glob(J("evidencias", "extracoes", "*.txt")):
        t = open(p, encoding="utf-8", errors="replace").read(); acc.append(t)
        pasta = os.path.basename(os.path.dirname(p)); rid = pasta if pasta.startswith("DEC-") else re.sub(r"(\.F)?\.txt$", "", os.path.basename(p))
        n = num_do_id.get(rid) or (cnj(pasta) if len(cnj(pasta)) == 20 else "")
        if n: idx[n].append(t)
    corpus = "\n\u0001\n".join(acc)
    colap, _ = mapa_espacos(corpus)
    sys.stdout.reconfigure(encoding="utf-8")
    tot = ok = 0; atrib = collections.Counter(); rel = []
    for p in sorted(glob.glob(J("analises", "fichas", "TES-*.json"))):
        f = json.load(open(p, encoding="utf-8")); falhas = []; fora = []
        for e in f.get("excertos", []):
            tx = (e.get("texto") or "").strip(); tot += 1
            if not tx: falhas.append("vazio"); continue
            if tx in corpus or re.sub(r"\s+", " ", tx) in colap:
                ok += 1
                n = cnj(e.get("numero"))
                if n and any(contem(tx, t) for t in idx.get(n, [])): atrib["atribuido"] += 1
                else: atrib["so_no_corpus"] += 1; fora.append({"numero": e.get("numero"), "texto": tx[:80]})
            else: falhas.append(tx[:80])
        rel.append({"ficha": os.path.basename(p), "excertos": len(f.get("excertos", [])), "falhas": falhas, "fora_do_processo": fora})
        print(f"{os.path.basename(p):55s} excertos={len(f.get('excertos', [])):3d} falhas={len(falhas)} fora_do_processo={len(fora)}")
    with open(J("auditoria", "conferencia-fichas-e43.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for r in rel: fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("ATRIBUICAO", dict(atrib))
    print("TOTAL excertos", tot, "conferidos", ok, "falhas", tot - ok)


if __name__ == "__main__":
    main()
