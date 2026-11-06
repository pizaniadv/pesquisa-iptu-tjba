"""Fatia deterministicamente o que sai da T2 para a T3 (lote E4-IPTU04): gemeos por sha256 do texto limpo + alinea por regex.
A alinea aqui e INDICIO (regex), nao classificacao: so decide a ordem de leitura (TES-001 = alineas b/c primeiro).
Saida: estado/t3/<lote>-fatias.json. Uso: python -I scripts/fatiar_t3.py --lote E4-IPTU04"""
import argparse, collections, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
RX = {
    "b_templo": re.compile(r"(?i)templo|igreja|culto|religios|diocese|par[óo]quia|mitra|evang[ée]lic|assembleia de deus|batista|loja ma[çc]"),
    "c_entidade": re.compile(r"(?i)sindicat|federa[çc][ãa]o d|institui[çc][ãa]o de (educa|assist)|assist[êe]ncia social|entidade (beneficente|filantr)|sem fins lucrativos|filantr[óo]pic|art(\.|igo)\s*14 do c[óo]digo tribut|art(\.|igo)\s*14,? (do )?ctn|partido pol[íi]tic"),
    "a_reciproca": re.compile(r"(?i)rec[íi]proca|economia mista|empresa p[úu]blica|autarquia|codeba|embasa|correios|\bect\b|infraero|\binss\b|uni[ãa]o federal|caixa econ[ôo]mica|petrobras|codesp|funda[çc][ãa]o p[úu]blica|universidade federal"),
}
IMUN = re.compile(r"(?i)imun")
ISEN = re.compile(r"(?i)isen[çc]|isent")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lote", required=True); a = ap.parse_args()
    R = [json.loads(l) for l in open(J("dados", "t2", f"{a.lote}.jsonl"), encoding="utf-8")]
    ids = [r["id"] for r in R if r["veredito_efetivo"] != "nao_pertinente"]
    grupos, info = collections.defaultdict(list), {}
    for i in ids:
        t = limpar_html(open(J("evidencias", "extracoes", i + ".txt"), encoding="utf-8").read())
        corpo = re.sub(r"\s+", " ", t).strip()
        h = hashlib.sha256(corpo.encode("utf-8")).hexdigest(); grupos[h].append(i)
        m = json.load(open(J("evidencias", "extracoes", i + ".meta.json"), encoding="utf-8"))
        al = [k for k, rx in RX.items() if rx.search(t)]
        if not IMUN.search(t): al = ["so_isencao"] if ISEN.search(t) else ["sem_imunidade_no_texto"]
        elif not al: al = ["imunidade_alinea_indefinida"]
        info[i] = {"alineas_indicio": al, "chars": len(t), "numero": m.get("numeroProcesso"), "classe": (m.get("classe") or {}).get("descricao") if isinstance(m.get("classe"), dict) else m.get("classe")}
    gem = [sorted(v) for v in grupos.values() if len(v) > 1]
    rep = {min(v): sorted(v) for v in grupos.values()}  # representante = menor id do grupo
    fat = collections.defaultdict(list)
    for r, g in sorted(rep.items()):
        al = info[r]["alineas_indicio"]
        if "b_templo" in al or "c_entidade" in al: f = "TES001_bc"
        elif "a_reciproca" in al: f = "TES002_a"
        else: f = al[0]
        fat[f].append(r)
    out = {"lote": a.lote, "entrada_T3": len(ids), "grupos_texto_identico": len(grupos), "gemeos": [{"ids": g, "numeros": [info[i]["numero"] for i in g], "classes": [info[i]["classe"] for i in g]} for g in gem],
           "fatias": {k: {"n": len(v), "chars": sum(info[i]["chars"] for i in v), "ids": v} for k, v in sorted(fat.items())},
           "indicio_por_id": info, "nota": "alinea por regex = indicio para ordem de leitura; a T3 classifica"}
    os.makedirs(J("estado", "t3"), exist_ok=True)
    json.dump(out, open(J("estado", "t3", f"{a.lote}-fatias.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("entrada", len(ids), "grupos", len(grupos), "gemeos", len(gem))
    for k, v in out["fatias"].items(): print(f"  {k}: {v['n']} decisoes, {v['chars']} chars")
    for g in out["gemeos"][:8]: print("  gemeo", g)


if __name__ == "__main__":
    main()
