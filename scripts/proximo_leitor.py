"""Controle da onda T3: marca o proximo leitor como lancado e imprime seus ids (registro em estado/t3/lancados.txt).
--status: quantos leitores lancados e quantos ids ja com registro em dados/decisoes.
Uso: python -I scripts/proximo_leitor.py [--status]"""
import json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
L = json.load(open(J("estado", "t3", "onda-E4-IPTU04.json"), encoding="utf-8"))["leitores"]
lp = J("estado", "t3", "lancados.txt")
lanc = set(open(lp).read().split()) if os.path.exists(lp) else {"1", "2", "3", "4", "5"}
feito = lambda i: os.path.exists(J("dados", "decisoes", i + ".json"))
if "--status" in sys.argv:
    tot = sum(len(r["ids"]) for r in L); ok = sum(feito(i) for r in L for i in r["ids"])
    print(f"lancados {len(lanc)}/{len(L)} | registros {ok}/{tot}")
    for r in L:
        if str(r["n"]) in lanc:
            falta = [i for i in r["ids"] if not feito(i)]
            if falta: print("  leitor", r["n"], "faltam", len(falta))
    sys.exit()
for r in L:
    if str(r["n"]) not in lanc:
        lanc.add(str(r["n"])); open(lp, "w").write(" ".join(sorted(lanc, key=int)))
        print(r["n"], ", ".join(r["ids"])); break
else:
    print("FIM")
