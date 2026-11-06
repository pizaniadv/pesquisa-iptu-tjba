"""Validador de registros de decisao (camada de CODIGO, antes de qualquer revisao por modelo).
Uso: python -I scripts/validar.py [dados/decisoes/<id>.json ...]   (sem argumento: todos)
1. Valida contra schemas/decisao.schema.json.
2. Para cada excerto (fundamento_determinante, argumentos_rejeitados, fatos_relevantes, dispositivo): procura o texto
   como substring LITERAL de evidencias/extracoes/<id>.txt (com tolerancia SO a espacos em branco colapsados);
   achado -> grava localizador 'texto:ini-fim@sha256' e conferido_no_original=true; nao achado -> REPROVA.
3. Confere fonte.sha256_texto contra o .meta.json e que o leitor nao marcou 'verificado'.
Reescreve o JSON com os localizadores e grava recibo em auditoria/verificacoes.jsonl. Codigo de saida 1 se algum reprovar."""
import json, os, re, sys, glob, datetime as dt
import jsonschema
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = json.load(open(os.path.join(RAIZ, "schemas", "decisao.schema.json"), encoding="utf-8"))


def mapa_espacos(t):
    """texto com espacos colapsados + mapa de posicao para o original."""
    out, pos, prev_sp = [], [], False
    for i, ch in enumerate(t):
        if ch.isspace():
            if prev_sp: continue
            out.append(" "); pos.append(i); prev_sp = True
        else:
            out.append(ch); pos.append(i); prev_sp = False
    return "".join(out), pos


def achar(txt, colap, pos, q):
    i = txt.find(q)
    if i >= 0: return i, i + len(q), "literal"
    qc = re.sub(r"\s+", " ", q.strip())
    j = colap.find(qc)
    if j >= 0: return pos[j], pos[j + len(qc) - 1] + 1, "literal_espacos_colapsados"
    return None


def excertos(reg):
    for q in reg.get("questoes", []):
        for k in ("fundamento_determinante", "argumentos_rejeitados"):
            for e in q.get(k, []) or []: yield f"{q['id']}.{k}", e
    for e in (reg.get("contexto") or {}).get("fatos_relevantes", []) or []: yield "contexto.fatos_relevantes", e
    for e in reg.get("dispositivo", []) or []: yield "dispositivo", e


def validar(p):
    reg = json.load(open(p, encoding="utf-8")); erros = []; avisos = []
    try:
        jsonschema.validate(reg, SCHEMA)
    except jsonschema.ValidationError as e:
        erros.append(f"schema: {e.message[:300]} @ {'/'.join(map(str, e.absolute_path))}")
    rid = reg.get("id", "?")
    tp = os.path.join(RAIZ, "evidencias", "extracoes", rid + ".txt")
    mp = os.path.join(RAIZ, "evidencias", "extracoes", rid + ".meta.json")
    if not os.path.exists(tp): erros.append("texto de extracao ausente"); return reg, erros, avisos, 0
    txt = open(tp, encoding="utf-8").read(); colap, pos = mapa_espacos(txt)
    meta = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
    sha = meta.get("sha256_texto")
    if (reg.get("fonte") or {}).get("sha256_texto") not in (None, sha): erros.append("fonte.sha256_texto diverge do .meta.json")
    reg.setdefault("fonte", {})["sha256_texto"] = sha
    n = 0
    for onde, e in excertos(reg):
        q = (e.get("texto") or "")
        if len(q.strip()) < 12: erros.append(f"{onde}: excerto curto demais para conferencia"); continue
        r = achar(txt, colap, pos, q)
        if not r:
            erros.append(f"{onde}: excerto NAO achado literalmente: {q[:120]!r}"); e["conferido_no_original"] = False; continue
        ini, fim, modo = r; e["localizador"] = f"texto:{ini}-{fim}@sha256:{(sha or '?')[:16]}"; e["conferido_no_original"] = True; n += 1
        if modo != "literal": avisos.append(f"{onde}: achado com espacos colapsados")
    Q = reg.get("qualidade") or {}
    if Q.get("leitura") == "inteiro_teor_lido" and Q.get("completude") != "inteiro_teor":
        erros.append("leitura=inteiro_teor_lido exige completude=inteiro_teor (use disponivel_lido_integralmente)")
    if reg.get("estado") != "excluido":
        for q in reg.get("questoes", []):
            if q.get("resultado", "").startswith("favoravel") and not q.get("natureza_beneficio"):
                erros.append(f"{q['id']}: resultado favoravel sem natureza_beneficio")
            if not q.get("resultado", "").startswith("favoravel") and q.get("natureza_beneficio"):
                erros.append(f"{q['id']}: natureza_beneficio preenchida em resultado nao favoravel")
    if reg.get("estado") == "verificado" and not (reg.get("qualidade") or {}).get("verificacao") == "antialucinacao_aprovada":
        erros.append("estado=verificado sem antialucinacao aprovada")
    return reg, erros, avisos, n


def main():
    arqs = sys.argv[1:] or sorted(glob.glob(os.path.join(RAIZ, "dados", "decisoes", "*.json")))
    ruim = 0
    for p in arqs:
        reg, erros, avisos, n = validar(p)
        if not erros:
            json.dump(reg, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        else:
            ruim += 1
        rec = {"data": dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds"), "verificacao": "validar.py",
               "registro": os.path.basename(p), "aprovado": not erros, "excertos_conferidos": n, "erros": erros, "avisos": avisos,
               "revisor": {"quem": "scripts/validar.py", "tipo": "automatizada"}}
        open(os.path.join(RAIZ, "auditoria", "verificacoes.jsonl"), "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(("OK  " if not erros else "REPROVADO ") + os.path.basename(p), n, "excertos", "; ".join(erros)[:600])
    sys.exit(1 if ruim else 0)


if __name__ == "__main__":
    main()
