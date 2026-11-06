"""Extrai o texto LIMPO (limpar_html v1) das decisoes de um lote da E4 e grava evidencias/extracoes/<id>.txt + .meta.json.
Lote = candidatos com o eixo de indicio pedido (todos os niveis T1, todos os anos; a T1 e so indicio — protocolo v2),
menos os ja classificados em dados/decisoes/. Aceita os dois formatos de ponteiro: acervo local (arquivo:linha) e API (por sha256_linha
em derivados/hits-tjbaapi.jsonl). Nao sobrescreve extracao existente.
Uso: python -I scripts/extrair_lote.py --eixo IPTU-04 --lote E4-IPTU04"""
import argparse, collections, glob, hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html, LIMPEZA_VERSAO  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
CAMPOS = ("id", "sourceId", "numeroProcesso", "codigoProcesso", "relator", "orgaoJulgador", "classe", "source",
          "instancia", "tipoDecisao", "dataPublicacao", "dataJulgamento", "dataAtualizacao", "hash")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--eixo", required=True); ap.add_argument("--lote", required=True)
    a = ap.parse_args()
    feitos = {os.path.basename(p)[:-5] for p in glob.glob(J("dados", "decisoes", "*.json"))}
    cand = []
    for f in ("candidatos-tjba.jsonl", "candidatos-tjbaapi.jsonl"):
        for l in open(J("dados", f), encoding="utf-8"):
            r = json.loads(l)
            if a.eixo in (r.get("eixos_indicio") or []) and r["id"] not in feitos: cand.append(r)
    cand.sort(key=lambda r: r["id"])
    api = {}
    if any(r["ponteiro"].startswith("API:") for r in cand):
        for l in open(J("derivados", "hits-tjbaapi.jsonl"), encoding="utf-8"):
            h = json.loads(l); api[h["sha256_linha"]] = h["registro"]
    porarq = collections.defaultdict(dict)
    for r in cand:
        if not r["ponteiro"].startswith("API:"):
            arq, _, ln = r["ponteiro"].rpartition(":"); porarq[arq][int(ln)] = r["id"]
    brutos = {}
    for arq, linhas in porarq.items():  # uma passada por arquivo
        alvo = max(linhas)
        with open(arq, "rb") as fh:
            for i, raw in enumerate(fh, 1):
                if i in linhas: brutos[linhas[i]] = raw.rstrip(b"\n")  # convencao da varredura (varrer_f.py): tira so o \n; o \r entra no hash
                if i >= alvo: break
    exdir = J("evidencias", "extracoes"); os.makedirs(exdir, exist_ok=True)
    lista, novos, falhas = [], 0, []
    for r in cand:
        tp = os.path.join(exdir, r["id"] + ".txt")
        if r["ponteiro"].startswith("API:"):
            reg = api.get(r["sha256_linha"]); sha_linha = r["sha256_linha"]
        else:
            raw = brutos.get(r["id"]); reg = json.loads(raw.decode("utf-8")) if raw else None
            sha_linha = hashlib.sha256(raw).hexdigest() if raw else None
            if sha_linha and sha_linha != r["sha256_linha"]: falhas.append((r["id"], "sha256_linha diverge do candidato")); continue
        if reg is None: falhas.append((r["id"], "registro nao achado")); continue
        lista.append(r["id"])
        if os.path.exists(tp): continue
        txt = f"[EMENTA]\n{limpar_html(reg.get('ementa'))}\n\n[CONTEUDO]\n{limpar_html(reg.get('conteudo'))}\n"
        b = txt.encode("utf-8"); open(tp, "wb").write(b)
        meta = {k: reg.get(k) for k in CAMPOS}
        meta.update({"ponteiro": r["ponteiro"], "sha256_linha": sha_linha, "sha256_texto": hashlib.sha256(b).hexdigest(),
                     "extracao": f"ementa+conteudo do JSON, {LIMPEZA_VERSAO} (HTML removido de forma deterministica), sem OCR",
                     "lote": a.lote, "nivel_T1": r["nivel_T1"], "chars_brutos": len((reg.get("ementa") or "") + (reg.get("conteudo") or ""))})
        json.dump(meta, open(os.path.join(exdir, r["id"] + ".meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        novos += 1
    os.makedirs(J("estado"), exist_ok=True)
    json.dump({"lote": a.lote, "eixo": a.eixo, "criterio": "eixo de indicio T1; todos os niveis e anos; menos os ja classificados",
               "excluidos_ja_classificados": sorted(feitos), "ids": lista, "falhas": falhas},
              open(J("estado", f"lote-{a.lote}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tam = sum(os.path.getsize(os.path.join(exdir, i + ".txt")) for i in lista)
    print(f"lote {a.lote}: {len(lista)} decisoes, {novos} extracoes novas, {len(falhas)} falhas, {tam} bytes limpos")
    for f in falhas: print("FALHA", *f)


if __name__ == "__main__":
    main()
