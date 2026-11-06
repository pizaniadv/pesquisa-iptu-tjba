"""Catalogo de teses (E4-2): extrai so a EMENTA limpa (limpar_html v1, teto 3.000) dos candidatos com indicio T1 favoravel
(Municipio recorre + desprovido, ou contribuinte recorre + provido), fora do eixo IPTU-04 (ja tratado na E4-1), e divide em lotes de 60.
Saida: estado/catalogo/lote-NN.jsonl ({id, sha256_ementa, eixos_indicio, ementa}) e estado/catalogo/indice.json.
Uso: python -I scripts/extrair_ementas_fav.py"""
import collections, hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
POR_LOTE, TETO = 60, 3000


def fav(r):
    d = r.get("dispositivo_indicio") or []
    return (r.get("municipio_recorre_indicio") and d == ["desprovido"]) or (not r.get("municipio_recorre_indicio") and d == ["provido"])


def main():
    L = [json.loads(l) for f in ("candidatos-tjba.jsonl", "candidatos-tjbaapi.jsonl") for l in open(J("dados", f), encoding="utf-8")]
    alvo = sorted([r for r in L if fav(r) and "IPTU-04" not in (r.get("eixos_indicio") or [])], key=lambda r: r["id"])
    api = {}
    if any(r["ponteiro"].startswith("API:") for r in alvo):
        for l in open(J("derivados", "hits-tjbaapi.jsonl"), encoding="utf-8"):
            h = json.loads(l); api[h["sha256_linha"]] = h["registro"]
    porarq = collections.defaultdict(dict)
    for r in alvo:
        if not r["ponteiro"].startswith("API:"):
            arq, _, ln = r["ponteiro"].rpartition(":"); porarq[arq][int(ln)] = r["id"]
    em = {}
    for arq, linhas in porarq.items():
        alvo_max = max(linhas)
        with open(arq, "rb") as fh:
            for i, raw in enumerate(fh, 1):
                if i in linhas:
                    em[linhas[i]] = limpar_html(json.loads(raw.decode("utf-8")).get("ementa"))
                if i >= alvo_max: break
    for r in alvo:
        if r["ponteiro"].startswith("API:"): em[r["id"]] = limpar_html((api.get(r["sha256_linha"]) or {}).get("ementa"))
    out = J("estado", "catalogo"); os.makedirs(out, exist_ok=True)
    itens = [r for r in alvo if (em.get(r["id"]) or "").strip()]
    sem = [r["id"] for r in alvo if not (em.get(r["id"]) or "").strip()]
    for k in range(0, len(itens), POR_LOTE):
        with open(os.path.join(out, f"lote-{k // POR_LOTE + 1:02d}.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for r in itens[k:k + POR_LOTE]:
                e = em[r["id"]][:TETO]
                f.write(json.dumps({"id": r["id"], "sha256_ementa": hashlib.sha256(e.encode("utf-8")).hexdigest(), "eixos_indicio": r.get("eixos_indicio"), "ementa": e}, ensure_ascii=False) + "\n")
    json.dump({"criterio": "indicio T1 favoravel (Municipio recorre+desprovido ou contribuinte recorre+provido), fora de IPTU-04", "total": len(alvo),
               "com_ementa": len(itens), "sem_ementa": sem, "lotes": (len(itens) + POR_LOTE - 1) // POR_LOTE},
              open(os.path.join(out, "indice.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("alvo", len(alvo), "com ementa", len(itens), "sem ementa", len(sem), "lotes", (len(itens) + POR_LOTE - 1) // POR_LOTE,
          "chars", sum(len(em[r["id"]][:TETO]) for r in itens))


if __name__ == "__main__":
    main()
