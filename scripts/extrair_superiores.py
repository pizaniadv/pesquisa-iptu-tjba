"""Acrescenta ao piloto: 1 decisao do <ACERVO>/STJ (sorteio, semente fixa, nivel A1) e 3 precedentes qualificados do PANGEA
escolhidos pelo TEXTO para exercitar o schema (sumula vinculante, tese de RG julgada, tema de RG afetado/pendente).
Extrai texto + meta (sha256) em evidencias/extracoes/ e acrescenta a estado/piloto.json."""
import json, os, random, hashlib
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEMENTE = 20261105
PANGEA_IDS = {"stf-sv-52": "S16-sumula-vinculante", "stf-rg-693": "S17-rg-julgado-imunidade", "stf-rg-1398": "S18-rg-afetado-pendente"}


def grava(cid, txt, meta, piloto, estrato, ptr):
    b = txt.encode("utf-8"); ex = os.path.join(RAIZ, "evidencias", "extracoes")
    open(os.path.join(ex, cid + ".txt"), "wb").write(b)
    meta.update({"ponteiro": ptr, "sha256_texto": hashlib.sha256(b).hexdigest()})
    json.dump(meta, open(os.path.join(ex, cid + ".meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not any(s["id"] == cid for s in piloto["selecao"]):
        piloto["selecao"].append({"id": cid, "estrato": estrato, "ponteiro": ptr, "sha256_texto": meta["sha256_texto"], "chars": len(txt)})
    print(estrato, cid, len(txt))


def main():
    pp = os.path.join(RAIZ, "estado", "piloto.json"); piloto = json.load(open(pp, encoding="utf-8"))
    C = [json.loads(l) for l in open(os.path.join(RAIZ, "dados", "candidatos-stj.jsonl"), encoding="utf-8")]
    C = sorted([d for d in C if d["nivel_T1"] == "A1"], key=lambda d: d["id"])
    d = random.Random(SEMENTE).choice(C)
    arq, _, ln = d["ponteiro"].rpartition(":"); ln = int(ln)
    with open(arq, "rb") as fh:
        raw = next(r for i, r in enumerate(fh, 1) if i == ln)
    r = json.loads(raw.decode("utf-8"))
    md = os.path.join(os.environ.get("ACERVO_STJ", "<ACERVO>/STJ"), r.get("arquivo") or "")
    corpo = open(md, encoding="utf-8").read() if r.get("arquivo") and os.path.exists(md) else ""
    txt = f"[EMENTA]\n{r.get('ementa') or ''}\n\n[CONTEUDO]\n{corpo}\n"
    meta = {k: r.get(k) for k in ("orgao", "ano", "numero_processo", "classe", "relator", "tipo_decisao", "tema", "arquivo")}
    meta["extracao"] = "ementa do JSONL + .md do espelho STJ em acervo local (sem OCR)"
    grava(d["id"], txt, meta, piloto, "S15-stj-sorteio", d["ponteiro"])
    for l in open(os.path.join(RAIZ, "evidencias", "pangea-iptu.jsonl"), encoding="utf-8"):
        p = json.loads(l)
        if p["id"] in PANGEA_IDS:
            cid = "DEC-PANGEA-" + hashlib.sha256(p["id"].encode()).hexdigest()[:12]
            txt = f"[PRECEDENTE QUALIFICADO — espelho BNP/CNJ]\nid: {p['id']}\norgao: {p['orgao']}\nespecie: {p['especie']} ({p['especie_desc']})\nnumero: {p['numero']}\nsituacao: {p['situacao']}\nultima_atualizacao: {p['ultima_atualizacao']}\nlink: {p['link_decisao']}\n\n[TEXTO]\n{p['texto']}\n"
            meta = {k: p.get(k) for k in ("id", "orgao", "especie", "numero", "situacao", "ultima_atualizacao", "link_decisao", "_sha256")}
            meta["extracao"] = "<ACERVO>/PANGEA/pangea.db (espelho de 21/07/2026); situacao a reconferir no portal na data de corte"
            grava(cid, txt, meta, piloto, PANGEA_IDS[p["id"]], f"<ACERVO>/PANGEA/pangea.db:{p['id']}")
    json.dump(piloto, open(pp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
