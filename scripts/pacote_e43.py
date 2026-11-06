"""Monta o pacote de leitura de cada familia da E4-3 (regra estado/brief-ficha-tese-v1.md).
Por tese: catalogo (favoraveis com excerto conferido, ate 25), acervo (contagens + amostra de 8 ementas sem indicio favoravel, semente 20261106),
djen (ate 6 itens por frase, texto ate 2.500), tjba_api (ate 6, ementa ate 1.500), pangea (ate 6, campos ate 1.500).
F1 e dividida em F1a e F1b (tamanho). Saida: estado/E4-3/pacote-<familia>.json. Uso: python -I scripts/pacote_e43.py"""
import collections, json, os, random, re
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
SPLIT = {"F1_execucao_processo": {"F1a_execucao_processo": [4, 10, 11, 12, 13, 15], "F1b_execucao_processo": [16, 18, 24, 34, 36, 37]}}


CNJ = re.compile(r"\d{7}-?\d{2}\.?\d{4}\.?\d\.?\d{2}\.?\d{4}")


def base(num):
    m = CNJ.search(num or "")
    return re.sub(r"\D", "", m.group(0)) if m else (num or "").strip()


def dedup(itens, kn, kt, visto):
    """Funde julgados repetidos: mesmo processo (numero sem sufixo) ou mesmo texto normalizado. `visto` acumula entre fontes."""
    out, textos = [], set()
    for i in itens:
        b = base(i.get(kn)); tx = re.sub(r"\W+", "", (i.get(kt) or "").lower())[:400]
        if (b and b in visto) or (tx and tx in textos): continue
        if b: visto.add(b)
        if tx: textos.add(tx)
        out.append(i)
    return out


def main():
    T = json.load(open(J("estado", "E4-3", "teses.json"), encoding="utf-8"))["teses"]
    cat = json.load(open(J("analises", "catalogo-teses-v1.json"), encoding="utf-8"))["linhas"]
    B = {json.loads(l)["id"]: json.loads(l) for l in open(J("derivados", "ementas-candidatos.jsonl"), encoding="utf-8")}
    rec = json.load(open(J("estado", "E4-3", "recorte-acervo.json"), encoding="utf-8"))
    tj = {x["n"]: x for x in json.load(open(J("evidencias", "dirigida", "tjba-api-e43-2026-11-06.json"), encoding="utf-8"))["teses"]}
    dirig = {}
    for f in set(t["familia"] for t in T):
        p = J("evidencias", "dirigida", f"{f}-2026-11-06.json")
        if os.path.exists(p):
            for x in json.load(open(p, encoding="utf-8"))["teses"]: dirig[x["n"]] = x
    grupos = collections.defaultdict(list)
    for t in T:
        f = t["familia"]
        for sub, ns in SPLIT.get(f, {}).items():
            if t["n"] in ns: f = sub
        grupos[f].append(t)
    rnd = random.Random(20261106)
    for f, ts in grupos.items():
        pac = {"familia": f, "regra": "estado/brief-ficha-tese-v1.md", "teses": []}
        for t in ts:
            rx = re.compile("(?i)" + t["regex"])
            c = [l for l in cat if l["pertinente"] and not l["erros"] and (l["tema"] in t["temas_catalogo"] and (l["tema"] != "outro" or rx.search(l["tese"] or "")))]
            fav = [l for l in c if l["resultado"] in ("favoravel", "parcial")][:25]
            con = [l for l in c if l["resultado"] == "desfavoravel"][:10]
            ids = rec[str(t["n"])]["ids"]
            outras = [B[i] for i in ids if not B[i]["fav_indicio"]]
            amostra = rnd.sample(outras, min(8, len(outras)))
            d = dirig.get(t["n"], {})
            visto = set()  # processos ja presentes (catalogo primeiro), para nao repetir entre fontes
            fav, con = dedup(fav, "numero", "excerto", visto), dedup(con, "numero", "excerto", visto)
            amostra = dedup(amostra, "numero", "ementa", visto)
            api_itens = dedup(tj.get(t["n"], {}).get("itens", []), "numero", "ementa", visto)
            dj = [{"frase": x["frase"], "retornados": x["retornados"], "itens": dedup(x["itens"], "numero", "texto", visto)} for x in d.get("djen", [])]
            procs_acervo = {base(B[i]["numero"]) for i in ids}
            procs_fav = {base(B[i]["numero"]) for i in ids if B[i]["fav_indicio"]}
            pac["teses"].append({
                "n": t["n"], "nome": t["nome"],
                "catalogo": {"favoraveis": [{k: l[k] for k in ("numero", "orgao", "julgamento", "resultado", "tese", "excerto", "id")} for l in fav],
                             "contrarias": [{k: l[k] for k in ("numero", "orgao", "julgamento", "resultado", "tese", "excerto", "id")} for l in con],
                             "nota": "deduplicado por processo (numero sem sufixo) e texto; julgados repetidos do portal foram fundidos"},
                "acervo": {"n_decisoes": rec[str(t["n"])]["n"], "n_processos": len(procs_acervo), "n_processos_fav_indicio": len(procs_fav),
                           "rotulo": "recorte por palavra na ementa; indicio, nao taxa; contar por processo",
                           "amostra_outras": [{"id": b["id"], "numero": b["numero"], "orgao": b["orgao"], "julgamento": b["julgamento"], "ementa": (b["ementa"] or "")[:1500]} for b in amostra]},
                "djen": [{"frase": x["frase"], "retornados_brutos": x["retornados"], "itens": [{**i, "texto": (i.get("texto") or "")[:2500]} for i in x["itens"][:6]]} for x in dj],
                "tjba_api": {"termo": tj.get(t["n"], {}).get("termo"), "itemCount_bruto": tj.get(t["n"], {}).get("itemCount"),
                             "itens": [{**i, "ementa": (i.get("ementa") or "")[:1500]} for i in api_itens[:6]]},
                "pangea": [{k: (str(v)[:1500] if v else v) for k, v in r.items()} for r in d.get("pangea", [])[:6]]})
        p = J("estado", "E4-3", f"pacote-{f}.json")
        json.dump(pac, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f, len(ts), "teses", os.path.getsize(p), "bytes")


if __name__ == "__main__":
    main()
