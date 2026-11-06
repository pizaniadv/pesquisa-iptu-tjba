"""Seleciona o lote PILOTO (E3) por estratos, com semente fixa, e extrai o texto de cada decisao para leitura.
Estratos por INDICIO T1 (nao por resultado verificado). Janela prioritaria: publicacao >= 2021.
Saida: estado/piloto.json (lista + estrato + semente) e evidencias/extracoes/<id>.txt (+ .meta.json com sha256).
Uso: python -I scripts/selecionar_piloto.py"""
import json, os, random, hashlib
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEMENTE = 20261105
EST = [  # (nome, n, filtro)
    ("S01-imunidade-municipio-recorre-desprovido", 3, lambda d: "IPTU-04" in d["eixos_indicio"] and d["municipio_recorre_indicio"] and d["dispositivo_indicio"] == ["desprovido"] and d["instancia"] == "SEGUNDO_GRAU"),
    ("S02-imunidade-contribuinte-recorre-desprovido", 1, lambda d: "IPTU-04" in d["eixos_indicio"] and not d["municipio_recorre_indicio"] and d["dispositivo_indicio"] == ["desprovido"] and d["instancia"] == "SEGUNDO_GRAU"),
    ("S03-imunidade-provido", 1, lambda d: "IPTU-04" in d["eixos_indicio"] and d["dispositivo_indicio"] == ["provido"]),
    ("S04-prescricao-municipio-recorre", 2, lambda d: "IPTU-10" in d["eixos_indicio"] and d["municipio_recorre_indicio"] and d["instancia"] == "SEGUNDO_GRAU"),
    ("S05-sujeicao-passiva", 2, lambda d: ("IPTU-02" in d["eixos_indicio"] or "IPTU-03" in d["eixos_indicio"]) and d["instancia"] == "SEGUNDO_GRAU"),
    ("S06-base-calculo-legalidade", 2, lambda d: ("IPTU-06" in d["eixos_indicio"] or "IPTU-08" in d["eixos_indicio"]) and "IPTU-11" not in d["eixos_indicio"]),
    ("S07-progressividade", 1, lambda d: "IPTU-07" in d["eixos_indicio"]),
    ("S08-zona-urbana-rural", 1, lambda d: "IPTU-01" in d["eixos_indicio"]),
    ("S09-turma-recursal", 2, lambda d: d["instancia"] == "TURMA_RECURSAL"),
    ("S10-agravo-tutela", 1, lambda d: "IPTU-13" in d["eixos_indicio"] and "gravo" in (d["classe"] or "")),
    ("S11-nao-conhecido", 1, lambda d: d["dispositivo_indicio"] == ["nao_conhecido"]),
    ("S12-parcial", 1, lambda d: "parcial" in d["dispositivo_indicio"]),
    ("S13-repeticao", 1, lambda d: "IPTU-14" in d["eixos_indicio"] and "IPTU-11" not in d["eixos_indicio"]),
    ("S14-taxa-e-iptu", 1, lambda d: "IPTU-17" in d["eixos_indicio"]),
]


def main():
    L = [json.loads(l) for l in open(os.path.join(RAIZ, "dados", "candidatos-tjba.jsonl"), encoding="utf-8")]
    L = [d for d in L if d["nivel_T1"] in ("A1", "A2") and d["data_publicacao"] >= "2021" and d["tem_conteudo"]]
    L.sort(key=lambda d: d["id"])
    rnd = random.Random(SEMENTE); usados = set(); sel = []
    for nome, n, filt in EST:
        pool = [d for d in L if filt(d) and d["id"] not in usados]
        for d in rnd.sample(pool, min(n, len(pool))):
            usados.add(d["id"]); sel.append({"id": d["id"], "estrato": nome, "ponteiro": d["ponteiro"], "pool": len(pool)})
    # extrai texto
    exdir = os.path.join(RAIZ, "evidencias", "extracoes"); os.makedirs(exdir, exist_ok=True)
    for s in sel:
        arq, _, ln = s["ponteiro"].rpartition(":"); ln = int(ln)
        with open(arq, "rb") as fh:
            for i, raw in enumerate(fh, 1):
                if i == ln: break
        r = json.loads(raw.decode("utf-8"))
        txt = f"[EMENTA]\n{r.get('ementa') or ''}\n\n[CONTEUDO]\n{r.get('conteudo') or ''}\n"
        b = txt.encode("utf-8")
        open(os.path.join(exdir, s["id"] + ".txt"), "wb").write(b)
        meta = {k: r.get(k) for k in ("id", "sourceId", "numeroProcesso", "codigoProcesso", "relator", "orgaoJulgador", "classe", "source",
                                       "instancia", "tipoDecisao", "dataPublicacao", "dataJulgamento", "dataAtualizacao", "hash")}
        meta.update({"ponteiro": s["ponteiro"], "sha256_linha": hashlib.sha256(raw.rstrip(b"\n").rstrip(b"\r")).hexdigest(),
                     "sha256_texto": hashlib.sha256(b).hexdigest(), "extracao": "ementa+conteudo do JSON (texto puro do portal), sem OCR"})
        json.dump(meta, open(os.path.join(exdir, s["id"] + ".meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        s["sha256_texto"] = meta["sha256_texto"]; s["numero"] = r.get("numeroProcesso"); s["chars"] = len(txt)
    json.dump({"semente": SEMENTE, "criterio": "estratos por indicio T1; A1/A2; publicacao>=2021; com conteudo", "selecao": sel},
              open(os.path.join(RAIZ, "estado", "piloto.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for s in sel: print(s["estrato"], s["id"], s["numero"], s["chars"], "pool", s["pool"])


if __name__ == "__main__":
    main()
