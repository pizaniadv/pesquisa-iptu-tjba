"""Aplica as correcoes devolvidas pela antialucinacao (auditoria/antialucinacao-E43-<lote>.json) as fichas de analises/fichas/.
Cada item {"ficha", "de", "para"} troca o trecho exato `de` pelo `para` no .md e, se o mesmo trecho existir, no .json da ficha.
So aplica se `de` aparece EXATAMENTE uma vez no .md (senao lista para decisao manual). Itens sem `para` (ressalva) so se listam.
Original guardado em estado/E4-3/antes-antialucinacao/<ficha> (uma vez). Log: auditoria/aplicacao-antialucinacao.jsonl.
Depois rode scripts/conferir_fichas.py (os excertos citados no JSON tem de continuar literais).
Uso: python -I scripts/aplicar_antialucinacao.py <lote> [--aplicar]"""
import json, os, shutil, sys
from datetime import datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)


def main():
    lote = sys.argv[1]; aplicar = "--aplicar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    itens = json.load(open(J("auditoria", "antialucinacao-E43-%s.json" % lote), encoding="utf-8"))
    if isinstance(itens, dict): itens = itens.get("itens") or itens.get("correcoes") or []
    pasta = J("analises", "fichas"); antes = J("estado", "E4-3", "antes-antialucinacao"); os.makedirs(antes, exist_ok=True)
    cache, log, manual = {}, [], []
    for n, it in enumerate(itens):
        f = os.path.basename(it["ficha"]); f = f if f.endswith(".md") else f + ".md"
        de, para = it.get("de") or "", it.get("para")
        mdp = os.path.join(pasta, f) if os.path.exists(os.path.join(pasta, f)) else J("analises", "teses", f)  # TES-001 mora em analises/teses
        if not os.path.exists(mdp): manual.append((n, f, "ficha nao existe")); continue
        if para is None or para == de: manual.append((n, f, "sem texto novo (%s)" % it.get("tipo"))); continue
        md = cache.setdefault(mdp, open(mdp, encoding="utf-8").read())
        k = md.count(de)
        if k != 1: manual.append((n, f, "trecho aparece %d vezes" % k)); continue
        cache[mdp] = md.replace(de, para)
        jp = mdp[:-3] + ".json"; no_json = "sem_json"
        if os.path.exists(jp):
            jt = cache.setdefault(jp, open(jp, encoding="utf-8").read())
            de_j, para_j = json.dumps(de, ensure_ascii=False)[1:-1], json.dumps(para, ensure_ascii=False)[1:-1]
            kj = jt.count(de_j); no_json = {0: "trecho_ausente_no_json", 1: "aplicado"}.get(kj, "trecho_%d_vezes_no_json_nao_aplicado" % kj)
            if kj == 1: cache[jp] = jt.replace(de_j, para_j)
        # o recibo diz o que aconteceu no .md e no .json (revisao Codex, item 7)
        log.append({"lote": lote, "item": n, "ficha": f, "gravidade": it.get("gravidade"), "tipo": it.get("tipo"), "fonte": it.get("fonte"), "de": de, "para": para, "md": "aplicado", "json": no_json})
    print("aplicaveis", len(log), "| manuais", len(manual))
    for m in manual: print("  manual", m)
    if not aplicar: print("(simulacao; use --aplicar)"); return
    for p, t in cache.items():
        b = os.path.join(antes, os.path.basename(p))
        if not os.path.exists(b): shutil.copy2(p, b)
        with open(p, "w", encoding="utf-8", newline="") as fh: fh.write(t)
    agora = datetime.now().astimezone().isoformat(timespec="seconds")
    with open(J("auditoria", "aplicacao-antialucinacao.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
        for l in log: fh.write(json.dumps(dict(l, data=agora), ensure_ascii=False) + "\n")
        for m in manual: fh.write(json.dumps({"lote": lote, "item": m[0], "ficha": m[1], "manual": m[2], "data": agora}, ensure_ascii=False) + "\n")
    print("gravado")


if __name__ == "__main__":
    main()
