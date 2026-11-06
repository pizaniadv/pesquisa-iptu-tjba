"""Monta os pacotes da T2 (regra metodologia/t2-pertinencia-v1.md §1) e os divide em lotes de ate 50.
Fonte: evidencias/extracoes/<id>.txt, limpo por limpar_html v1 (idempotente sobre texto ja limpo).
Uso: python -I scripts/pacote_t2.py --lote E4-IPTU04          (ids de estado/lote-<lote>.json)
     python -I scripts/pacote_t2.py --lote CAL-PILOTO --piloto (ids de dados/decisoes/*.json)
Saida: estado/t2/<lote>/pacotes-NN.jsonl  ({id, sha256_pacote, pacote})"""
import argparse, glob, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
TERMOS = re.compile(r"(?i)(iptu|predial|territorial|imun|isen|tribut|lan[çc]amento|\bcda\b|execu[çc][ãa]o fiscal)")
TETO_EMENTA, JAN, TETO_JAN, CAUDA, POR_LOTE = 3000, 350, 2500, 700, 50


def texto_limpo(rid):
    return limpar_html(open(J("evidencias", "extracoes", rid + ".txt"), encoding="utf-8").read())


def pacote(t):
    em, _, co = t.partition("[CONTEUDO]")
    em = em.replace("[EMENTA]", "").strip()
    co = co.strip()
    ints = []
    for m in TERMOS.finditer(co):
        a, b = max(0, m.start() - JAN), min(len(co), m.end() + JAN)
        if ints and a <= ints[-1][1]: ints[-1][1] = max(ints[-1][1], b)
        else: ints.append([a, b])
    jan, n = [], 0
    for a, b in ints:
        if n >= TETO_JAN: break
        s = co[a:b][: TETO_JAN - n]; jan.append(s); n += len(s)
    cauda = co[-CAUDA:] if len(co) > CAUDA else co
    return ("[EMENTA]\n" + em[:TETO_EMENTA] + "\n\n[TRECHOS]\n" + "\n[...]\n".join(jan) + "\n\n[FINAL]\n" + cauda).strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lote", required=True); ap.add_argument("--piloto", action="store_true")
    a = ap.parse_args()
    if a.piloto: ids = sorted(os.path.basename(p)[:-5] for p in glob.glob(J("dados", "decisoes", "*.json")))
    else: ids = json.load(open(J("estado", f"lote-{a.lote}.json"), encoding="utf-8"))["ids"]
    out = J("estado", "t2", a.lote); os.makedirs(out, exist_ok=True)
    tot = 0
    for k in range(0, len(ids), POR_LOTE):
        with open(os.path.join(out, f"pacotes-{k // POR_LOTE + 1:02d}.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for rid in ids[k:k + POR_LOTE]:
                p = pacote(texto_limpo(rid)); tot += len(p)
                f.write(json.dumps({"id": rid, "sha256_pacote": hashlib.sha256(p.encode("utf-8")).hexdigest(), "pacote": p}, ensure_ascii=False) + "\n")
    print(f"{a.lote}: {len(ids)} pacotes em {(len(ids) + POR_LOTE - 1) // POR_LOTE} lotes, {tot} caracteres")


if __name__ == "__main__":
    main()
