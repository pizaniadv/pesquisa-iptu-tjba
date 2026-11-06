"""Tabela da TES-001 (imunidade de IPTU, alineas b/c: onus da destinacao), gerada dos registros harmonizados (harmonizacao-t3-v1).
Unidade = processo (numero CNJ sem sufixo), ato principal por materia (merito > processual > cautelar > admissibilidade > nao_examinada)
e especie (acordao > integrativa > monocratica). Onus = determinacao do leitor (estado/t3/respostas-leitores.jsonl; piloto pelo dossie v2).
Alinea = leitura T3 (subtema/pergunta), regex so como fallback. Via = indicio por codigo no texto (tutela pela provisoriedade).
Saidas: analises/teses/TES-001-tabela-v1.json e .csv. Visao gerada: nunca editar a mao.
Uso: python -I scripts/tabela_tes001.py"""
import collections, csv, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
CNJ = re.compile(r"\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}")
PRI_MAT = {"merito": 0, "processual": 1, "cautelar": 2, "sucumbencial": 3, "admissibilidade": 4, "nao_examinada": 5}
PRI_ESP = {"acordao": 0, "integrativa": 1, "decisao_monocratica": 2}
ONUS_PILOTO = {"DEC-TJBA-2f27678bfdd9": "municipio", "DEC-TJBA-9d673755fc33": "contribuinte", "DEC-TJBA-4a49bc3601d8": "nao_tratado"}
ALINEA_REVISADA = {"DEC-TJBA-6bb18811b55b": "c"}  # revisao do orquestrador: subtema do leitor = art. 150, VI, c (arrendataria, SV 52); "a" vinha de mencao a Tema 437
ONUS_REVISADO = {"DEC-TJBA-e3b4aef87c1f": "misto"}  # conferencia de inteiro teor v1 (06/11): voto do agravo poe no fisco o onus do nao atendimento; entidade provou os requisitos (onus "ambos")
RES = {"favoravel_integral": "favoravel", "favoravel_parcial": "favoravel", "desfavoravel": "desfavoravel", "sem_exame": "sem_exame", "indeterminavel": "indeterminavel"}


def alinea(txt_q, txt_doc):
    t = txt_q.lower()
    s = set(re.findall(r'al[íi]nea\s*["“\']?\s*([abc])\b', t)) | set(re.findall(r'\bvi\s*,\s*["“\']?([abc])["”\']?\b', t))
    if not s:
        if re.search(r"templo|religios|igreja|diocese|culto", t): s.add("b")
        if re.search(r"rec[íi]proca|economia mista|coelba|embasa|codeba|uni[ãa]o", t): s.add("a")
        if re.search(r"sindicat|educa|assist|beneficen|filantr|sem fins lucrativos|art\. 14", t): s.add("c")
    return "+".join(sorted(s)) or "?"


def via(r, q, doc):
    if q.get("provisoriedade") == "provisoria" or q.get("materia_examinada") == "cautelar": return "tutela"
    d = doc.lower()
    if re.search(r"pr[ée]-?\s?executividade", d): return "excecao_pre_executividade"
    if "mandado de segurança" in d or "mandado de seguranca" in d: return "mandado_seguranca"
    if re.search(r"embargos (à|a|do devedor|de devedor) execu", d): return "embargos_execucao"
    if "execução fiscal" in d or "execucao fiscal" in d: return "execucao_fiscal_outro"
    return "acao_conhecimento_ou_outro"


def main():
    onus = {json.loads(l)["id"]: json.loads(l) for l in open(J("estado", "t3", "respostas-leitores.jsonl"), encoding="utf-8")}
    for sp in glob.glob(J("estado", "t3", "releitura-h2", "DEC-*.json")):  # releitura H2 com inteiro teor (06/11) prevalece sobre a leitura do relatorio
        s = json.load(open(sp, encoding="utf-8"))
        if s.get("destino") == "reclassificar" and s.get("onus_tes001"):
            onus[s["id"]] = {"onus": s["onus_tes001"], "onus_texto": "releitura H2 (inteiro teor)"}
    linhas = []
    for p in sorted(glob.glob(J("dados", "decisoes", "*.json"))):
        r = json.load(open(p, encoding="utf-8"))
        if r["estado"] in ("excluido", "pendente"): continue
        qs = [q for q in r["questoes"] if q["eixo"] == "IPTU-04" and q["tributo"] == "IPTU"]
        if not qs: continue
        if r["id"] not in onus and r["id"] not in ONUS_PILOTO: continue  # so leitura T3 ou o trio do piloto da TES-001
        q = sorted(qs, key=lambda q: (PRI_MAT.get(q.get("materia_examinada"), 9), 0 if RES.get(q["resultado"]) == "favoravel" else 1))[0]
        doc = limpar_html(open(J("evidencias", "extracoes", r["id"] + ".txt"), encoding="utf-8").read())
        num = r["identificacao"]["numero_processo"].get("original") or ""
        m = CNJ.search(num); base = m.group(0) if m else num
        o = ONUS_REVISADO.get(r["id"]) or onus.get(r["id"], {}).get("onus") or ONUS_PILOTO.get(r["id"], "?")
        linhas.append({"id": r["id"], "processo": base, "especie": r["identificacao"].get("especie_ato"), "orgao": (r["identificacao"].get("orgao") if isinstance(r["identificacao"].get("orgao"), str) else ""),
                       "julgamento": (r.get("datas") or {}).get("julgamento") if isinstance((r.get("datas") or {}).get("julgamento"), str) else "",
                       "questao": q["id"], "materia": q.get("materia_examinada"), "resultado": RES.get(q["resultado"], q["resultado"]), "provisoriedade": q.get("provisoriedade"),
                       "alinea": ALINEA_REVISADA.get(r["id"]) or alinea((q.get("subtema") or "") + " " + q["pergunta"], doc), "via": via(r, q, doc), "onus": o,
                       "onus_texto": onus.get(r["id"], {}).get("onus_texto", ""), "completude": (r.get("qualidade") or {}).get("completude")})
    grupos = collections.defaultdict(list)
    for l in linhas: grupos[l["processo"]].append(l)
    proc = []
    for k, g in grupos.items():
        g.sort(key=lambda l: (PRI_MAT.get(l["materia"], 9), PRI_ESP.get(l["especie"], 9), l["id"]))
        pr = dict(g[0]); pr["atos_do_processo"] = [l["id"] for l in g]; proc.append(pr)
    out = {"gerado_por": "scripts/tabela_tes001.py", "regra": "metodologia/harmonizacao-t3-v1.md", "atos": len(linhas), "processos": len(proc), "linhas_processo": sorted(proc, key=lambda l: l["processo"])}
    json.dump(out, open(J("analises", "teses", "TES-001-tabela-v1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open(J("analises", "teses", "TES-001-tabela-v1.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); cols = ["processo", "id", "especie", "orgao", "julgamento", "alinea", "via", "materia", "resultado", "provisoriedade", "onus", "onus_texto", "completude", "atos_do_processo"]
        w.writerow(cols)
        for l in out["linhas_processo"]: w.writerow([("|".join(l[c]) if isinstance(l[c], list) else l[c]) for c in cols])
    sys.stdout.reconfigure(encoding="utf-8")
    print("atos", len(linhas), "processos", len(proc))
    print("alinea:", collections.Counter(l["alinea"] for l in proc))
    bc = [l for l in proc if l["alinea"] in ("b", "c", "b+c")]
    print("b/c (sem a):", len(bc), "| materia:", collections.Counter(l["materia"] for l in bc))
    mer = [l for l in bc if l["materia"] in ("merito", "processual", "cautelar")]
    print("\n== b/c, ato com exame (merito/processual/cautelar):", len(mer))
    t = collections.Counter((l["via"], l["onus"], l["resultado"]) for l in mer)
    for k, v in sorted(t.items()): print(f"  {k[0]:28s} onus={k[1]:13s} {k[2]:14s} {v}")
    print("\n== onus x resultado (b/c com exame):")
    for k, v in sorted(collections.Counter((l["onus"], l["resultado"]) for l in mer).items()): print("  ", k, v)
    print("\n== via x onus (b/c com exame):")
    for k, v in sorted(collections.Counter((l["via"], l["onus"]) for l in mer).items()): print("  ", k, v)


if __name__ == "__main__":
    main()
