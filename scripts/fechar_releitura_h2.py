"""Fecha a releitura dos pendentes H2 (estado/brief-releitura-h2-v1.md): aplica aos registros o destino dado pelo leitor.
- duplicata_de  -> estado excluido, EXC-04 (o julgamento ja e outro registro);
- sem_decisao   -> com falta_baixar: continua pendente (pendencia com as pecas a baixar); sem falta_baixar: excluido, EXC-03;
- reclassificar -> texto do registro passa a ser o inteiro teor (concatenacao dos arquivos_do_ato, na ordem dada); o texto acervo local antigo
                   fica em evidencias/extracoes/<id>.F.txt (+ .F.meta.json); fonte.canal = PDPJ/DJEN com a fonte acervo local em procedencias;
                   registro do leitor gravado; validar.py roda em seguida.
O registro anterior fica inteiro em estado/t3/releitura-h2/antes/<id>.json. Log: auditoria/releitura-h2.jsonl. Idempotente pelo log.
Uso: python -I scripts/fechar_releitura_h2.py [--aplicar]"""
import glob, hashlib, json, os, shutil, subprocess, sys
from datetime import datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
DIR = J("estado", "t3", "releitura-h2")
LOG = J("auditoria", "releitura-h2.jsonl")


def gravar(p, obj):
    with open(p, "w", encoding="utf-8", newline="\r\n") as fh:  # convencao dos registros: CRLF, indent=1
        json.dump(obj, fh, ensure_ascii=False, indent=1)


def main():
    aplicar = "--aplicar" in sys.argv
    feitos = {json.loads(l)["id"] for l in open(LOG, encoding="utf-8")} if os.path.exists(LOG) else set()
    agora = datetime.now().astimezone().isoformat(timespec="seconds")
    # (validacao por registro, antes do recibo)
    for sp in sorted(glob.glob(os.path.join(DIR, "DEC-*.json"))):
        s = json.load(open(sp, encoding="utf-8")); rid = s["id"]
        if rid in feitos: print("ja", rid); continue
        rp = J("dados", "decisoes", rid + ".json"); r = json.load(open(rp, encoding="utf-8"))
        d = s["destino"]; mud = {"destino": d, "antes": {"estado": r.get("estado"), "exclusao": r.get("exclusao")}}
        if d == "duplicata_de":
            assert s.get("duplicata_de") and os.path.exists(J("dados", "decisoes", s["duplicata_de"] + ".json")), rid
            r["estado"] = "excluido"; r["exclusao"] = {"motivo": "EXC-04", "nota": "duplicata do julgamento registrado em %s (releitura H2 com inteiro teor, 06/11/2026): %s" % (s["duplicata_de"], s["motivo"])}
        elif d == "sem_decisao":
            if s.get("falta_baixar"):
                r["estado"] = "pendente"
                r.setdefault("qualidade", {}).setdefault("pendencias", []).append("releitura H2 (06/11/2026): ato decisório não baixado; baixar pelo PDPJ: " + json.dumps(s["falta_baixar"], ensure_ascii=False))
                mud["destino"] = "sem_decisao_falta_baixar"
            else:
                r["estado"] = "excluido"; r["exclusao"] = {"motivo": "EXC-03", "nota": "sem decisão verificável no inteiro teor (releitura H2, 06/11/2026): " + s["motivo"]}
        elif d == "reclassificar":
            arqs = s["arquivos_do_ato"]; assert arqs, rid
            partes = []
            for a in arqs:
                t = open(J(*a.replace("\\", "/").split("/")), encoding="utf-8").read()
                partes.append("=== " + a.replace("\\", "/") + " ===\n" + t.strip() + "\n")
            txt = "\n".join(partes); sha = hashlib.sha256(txt.encode("utf-8")).hexdigest()
            novo = s["registro"]; assert novo["id"] == rid, rid
            fonte_ant = r.get("fonte") or {}
            canal = "DJEN" if all("/djen/" in a.replace("\\", "/") for a in arqs) else "PDPJ"
            novo["fonte"] = {"canal": canal, "ponteiro": " + ".join(a.replace("\\", "/") for a in arqs), "sha256": sha, "sha256_texto": sha,
                             "procedencias": [dict(fonte_ant, papel="texto acervo local anterior (só relatório), em evidencias/extracoes/%s.F.txt" % rid)]}
            novo["estado"] = "classificado"; novo["exclusao"] = None
            mud["arquivos_do_ato"] = arqs; mud["sha256_texto_novo"] = sha
            if aplicar:
                for suf in (".txt", ".meta.json"):
                    src = J("evidencias", "extracoes", rid + suf); dst = J("evidencias", "extracoes", rid + ".F" + suf)
                    if os.path.exists(src) and not os.path.exists(dst): shutil.copy2(src, dst)
                with open(J("evidencias", "extracoes", rid + ".txt"), "w", encoding="utf-8", newline="\n") as fh: fh.write(txt)
                meta = {"id": rid, "sha256_texto": sha, "extracao": "inteiro teor (releitura H2, 06/11/2026): concatenação dos arquivos_do_ato, na ordem dada", "arquivos": arqs, "meta_anterior": rid + ".F.meta.json"}
                gravar(J("evidencias", "extracoes", rid + ".meta.json"), meta)
            r = novo
        else:
            raise SystemExit("destino desconhecido: %s %s" % (rid, d))
        print(mud["destino"], rid, s.get("duplicata_de") or "", (s.get("onus_tes001") or ""))
        if aplicar:
            os.makedirs(os.path.join(DIR, "antes"), exist_ok=True)
            snap = os.path.join(DIR, "antes", rid + ".json")
            if not os.path.exists(snap): shutil.copy2(rp, snap)  # nunca sobrescreve o original numa retomada (revisao Codex, item 5)
            gravar(rp, r)
            if d == "reclassificar":  # valida ANTES do recibo; reprovado -> restaura registro e texto e nao registra (revisao Codex r2, item 5)
                rc = subprocess.run([sys.executable, "-I", J("scripts", "validar.py"), rp]).returncode
                if rc != 0:
                    shutil.copy2(snap, rp)
                    for suf in (".txt", ".meta.json"):
                        f_ant = J("evidencias", "extracoes", rid + ".F" + suf)
                        if os.path.exists(f_ant): shutil.copy2(f_ant, J("evidencias", "extracoes", rid + suf))
                    raise SystemExit("validar.py reprovou %s (codigo %d): registro e texto restaurados, sem recibo" % (rid, rc))
            with open(LOG, "a", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps({"id": rid, "versao": "releitura-h2-v1", "data": agora, "brief": "estado/brief-releitura-h2-v1.md", **mud}, ensure_ascii=False) + "\n")
    if not aplicar: print("(simulacao; use --aplicar)")


if __name__ == "__main__":
    main()
