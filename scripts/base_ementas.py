"""Base de ementas de TODOS os candidatos da trilha neutra (sem reler acervo local): junta derivados/hits-*.jsonl (registro original) aos
candidatos por sha256_linha. Saida: derivados/ementas-candidatos.jsonl ({id, numero, orgao, julgamento, classe, eixos, fav_indicio, ementa})
Uso: python -I scripts/base_ementas.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)


def main():
    reg = {}
    for f in ("hits-tjba.jsonl", "hits-tjbaapi.jsonl"):
        for l in open(J("derivados", f), encoding="utf-8"):
            h = json.loads(l); reg[h["sha256_linha"]] = h.get("registro") or {}
    n = sem = 0
    with open(J("derivados", "ementas-candidatos.jsonl"), "w", encoding="utf-8", newline="\n") as out:
        for f in ("candidatos-tjba.jsonl", "candidatos-tjbaapi.jsonl"):
            for l in open(J("dados", f), encoding="utf-8"):
                c = json.loads(l); r = reg.get(c["sha256_linha"])
                if r is None: sem += 1; continue
                d = c.get("dispositivo_indicio") or []
                fav = (c.get("municipio_recorre_indicio") and d == ["desprovido"]) or (not c.get("municipio_recorre_indicio") and d == ["provido"])
                out.write(json.dumps({"id": c["id"], "numero": c.get("numero_processo"), "orgao": c.get("orgao"), "julgamento": c.get("data_julgamento"),
                                      "classe": c.get("classe"), "eixos": c.get("eixos_indicio"), "fav_indicio": bool(fav),
                                      "ementa": limpar_html(r.get("ementa"))}, ensure_ascii=False) + "\n"); n += 1
    print("gravados", n, "sem registro", sem)


if __name__ == "__main__":
    main()
