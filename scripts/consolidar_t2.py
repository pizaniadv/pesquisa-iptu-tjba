"""Confere a saida da T2 (regra metodologia/t2-pertinencia-v1.md §4) e grava os recibos.
- Cada linha: campos e enums; excerto literal no texto limpo do .txt (tolerancia so a espacos colapsados).
- Linha reprovada ou id faltante -> veredito efetivo 'duvida' (nunca exclui).
- Recibos: auditoria/triagem-T2-<lote>.jsonl (regravado de forma atomica). Consolidado: dados/t2/<lote>.jsonl.
- --calibrar: compara com o desfecho conhecido do piloto (dados/decisoes/*.json) e aplica o aceite do §5.
Uso: python -I scripts/consolidar_t2.py --lote CAL-PILOTO --modelo sonnet --calibrar"""
import argparse, glob, json, os, re, sys, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import limpar_html, mapa_espacos, achar  # noqa: E402
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
REGRA, BRIEF = "t2-pertinencia-v1", "brief-t2-sonnet-v1"
VERED = {"pertinente", "nao_pertinente", "duvida"}
EIXO = re.compile(r"^IPTU-(0[1-9]|1[0-7])$")
EXC = re.compile(r"^EXC-0[1-7]$")


def conferir(s, pac):
    erros = []
    if s.get("veredito") not in VERED: erros.append("veredito invalido")
    m = s.get("motivo")
    if s.get("veredito") == "nao_pertinente" and not (isinstance(m, str) and EXC.match(m)): erros.append("nao_pertinente sem motivo EXC")
    if s.get("veredito") != "nao_pertinente" and m not in (None, ""): erros.append("motivo fora de nao_pertinente")
    if not isinstance(s.get("eixos"), list) or any(not (isinstance(e, str) and EIXO.match(e)) for e in s["eixos"]): erros.append("eixos invalidos")
    if s.get("imunidade_ou_isencao_examinada") not in (True, False, None): erros.append("imunidade_ou_isencao_examinada invalido")
    ex = s.get("excerto") or ""
    if not (15 <= len(ex) <= 400): erros.append("excerto fora do tamanho")
    else:
        t = limpar_html(open(J("evidencias", "extracoes", s["id"] + ".txt"), encoding="utf-8").read())
        c, pos = mapa_espacos(t)
        if achar(t, c, pos, ex) is None: erros.append("excerto nao achado no texto")
    return erros


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--lote", required=True); ap.add_argument("--modelo", required=True)
    ap.add_argument("--calibrar", action="store_true"); a = ap.parse_args()
    pac = {}
    for p in sorted(glob.glob(J("estado", "t2", a.lote, "pacotes-*.jsonl"))):
        for l in open(p, encoding="utf-8"):
            r = json.loads(l); pac[r["id"]] = (r["sha256_pacote"], os.path.basename(p))
    said = {}
    for p in sorted(glob.glob(J("estado", "t2", a.lote, "saida-*.jsonl"))):
        for n, l in enumerate(open(p, encoding="utf-8"), 1):
            l = l.strip()
            if not l: continue
            try: s = json.loads(l)
            except json.JSONDecodeError: print("linha nao-JSON", os.path.basename(p), n); continue
            if s.get("id") in pac: said[s["id"]] = s
    agora = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds")
    recs, cont = [], {"pertinente": 0, "nao_pertinente": 0, "duvida": 0, "reprovadas": 0, "faltantes": 0}
    for rid in sorted(pac):
        s = said.get(rid); erros = ["sem saida"] if s is None else conferir(s, pac[rid])
        if s is None: cont["faltantes"] += 1
        elif erros: cont["reprovadas"] += 1
        efet = "duvida" if erros else s["veredito"]; cont[efet] += 1
        recs.append({"id": rid, "lote": a.lote, "regra": REGRA, "brief": BRIEF, "modelo": a.modelo, "sha256_pacote": pac[rid][0],
                     "arquivo_pacote": pac[rid][1], "veredito_executor": (s or {}).get("veredito"), "veredito_efetivo": efet,
                     "motivo": (s or {}).get("motivo") if not erros else None, "eixos": (s or {}).get("eixos") if not erros else None,
                     "imunidade_ou_isencao_examinada": (s or {}).get("imunidade_ou_isencao_examinada") if not erros else None,
                     "excerto": (s or {}).get("excerto"), "nota": (s or {}).get("nota"), "erros_conferencia": erros, "conferido_em": agora})
    rev_p = J("auditoria", f"revisao-T2-{a.lote}.jsonl")  # revisao do orquestrador (so motivo/veredito de exclusao), com recibo proprio
    if os.path.exists(rev_p):
        rev = {json.loads(l)["id"]: json.loads(l) for l in open(rev_p, encoding="utf-8") if l.strip()}
        for r in recs:
            v = rev.get(r["id"])
            if not v: continue
            if r["veredito_efetivo"] != v["veredito"]: cont[r["veredito_efetivo"]] -= 1; cont[v["veredito"]] += 1
            r.update({"veredito_efetivo": v["veredito"], "motivo": v["motivo"], "revisao": {k: v[k] for k in ("revisor", "tipo", "data", "nota")}})
        print("revisao aplicada:", len(rev))
    for destino in (J("auditoria", f"triagem-T2-{a.lote}.jsonl"), J("dados", "t2", f"{a.lote}.jsonl")):
        os.makedirs(os.path.dirname(destino), exist_ok=True); tmp = destino + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp, destino)
    print(a.lote, cont)
    for r in recs:
        if r["erros_conferencia"]: print("REPROVADA", r["id"], r["erros_conferencia"])
    if a.calibrar:
        falhas = []
        for r in recs:
            reg = json.load(open(J("dados", "decisoes", r["id"] + ".json"), encoding="utf-8"))
            excl = reg["estado"] == "excluido"
            if excl and r["veredito_efetivo"] == "pertinente": falhas.append((r["id"], "EXC-07 do piloto saiu pertinente"))
            if not excl and r["veredito_efetivo"] == "nao_pertinente": falhas.append((r["id"], "mantido no piloto saiu nao_pertinente"))
            print(f"  {r['id']}  piloto={'excluido' if excl else 'mantido'}  T2={r['veredito_efetivo']}  eixos={r['eixos']}")
        print("CALIBRACAO", "APROVADA" if not falhas else "REPROVADA", falhas)


if __name__ == "__main__":
    main()
