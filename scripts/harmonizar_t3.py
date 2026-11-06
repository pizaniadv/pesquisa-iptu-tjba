"""Harmonizacao T3 v1 (regra em metodologia/harmonizacao-t3-v1.md), aplicada por codigo sobre os registros dos leitores T3.
H1 admissibilidade: questao com materia_examinada=admissibilidade -> resultado sem_exame, natureza_beneficio null (inadmissao != adesao).
H2 so relatorio (sem decisao no texto): estado -> pendente (protocolo §5); exclusao removida; fila de inteiro teor.
H3 exclusoes T3 revisadas pelo orquestrador (confirmar/aplicar).
Cada mudanca guarda o valor anterior em registro['harmonizacao'] e vai para auditoria/harmonizacao-t3.jsonl.
Idempotente. Uso: python -I scripts/harmonizar_t3.py [--aplicar]   (sem --aplicar: so lista)"""
import glob, json, os, sys, datetime as dt
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
VERSAO = "harmonizacao-t3-v1"
SO_RELATORIO = {"8dc97d887723", "b8e0c9b26343", "94cb00837999", "a320d38f47dc", "7e984fa65d9a", "0a49ea9f7548", "5dbc2e887d80",
                "f9cce833ae9d", "fd5f8aeaf0cc", "082c3674043f", "57e8d3985cfb"}
EXCLUSOES = {  # id curto: (motivo, nota)
    "18be072403d0": ("EXC-05", "agravo so sobre TRSD; a imunidade de IPTU foi decidida no 1o grau e nao subiu"),
    "1936b99b9973": ("EXC-05", "so TRSD de 2014; IPTU apenas como exemplo"),
    "3e41c6f7c065": ("EXC-05", "controversia so sobre a TRSD de 2012"),
    "0f052270560a": ("EXC-05", "disputa so sobre a taxa de lixo"),
    "35567f0ac65a": ("EXC-05", "controversia so sobre a TRSD 2014-2016"),
    "2ee7163561e8": ("EXC-05", "agravo so sobre a TRSD 2009-2011; IPTU decidido na origem e nao devolvido (mesmo criterio de 18be072403d0)"),
    "dd4a54913e46": ("EXC-05", "so TRSD em jogo no recurso"),
    "e22abeb7703b": ("EXC-01", "isencao de tributos municipais a EMBASA; IPTU so em precedente transcrito"),
    "90a9eff007fb": ("EXC-07", "cobranca de divida privada em cumprimento de sentenca; Municipio nao e parte"),
}


def main():
    aplicar = "--aplicar" in sys.argv
    agora = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds")
    log, cont = [], {"H1": 0, "H2": 0, "H3": 0}
    for p in sorted(glob.glob(J("dados", "decisoes", "*.json"))):
        r = json.load(open(p, encoding="utf-8"))
        rv = (r.get("qualidade") or {}).get("revisor") or []
        if not any(x.get("quem") == "leitor-opus-t3" for x in rv): continue
        curto = r["id"].split("-")[-1]; mud = []
        for q in r["questoes"]:
            if q.get("materia_examinada") == "admissibilidade" and (q["resultado"] != "sem_exame" or q.get("natureza_beneficio")):
                mud.append({"regra": "H1", "questao": q["id"], "antes": {"resultado": q["resultado"], "natureza_beneficio": q.get("natureza_beneficio")}})
                q["resultado"] = "sem_exame"; q["natureza_beneficio"] = None; cont["H1"] += 1
        if curto in SO_RELATORIO and r["estado"] != "pendente":
            mud.append({"regra": "H2", "antes": {"estado": r["estado"], "exclusao": r.get("exclusao")}})
            r["estado"] = "pendente"; r.pop("exclusao", None)
            r.setdefault("qualidade", {}).setdefault("pendencias", []).append("texto e so relatorio, sem decisao: buscar o inteiro teor (PDPJ) — harmonizacao-t3-v1 H2")
            cont["H2"] += 1
        if curto in EXCLUSOES:
            mot, nota = EXCLUSOES[curto]
            if r["estado"] != "excluido" or (r.get("exclusao") or {}).get("motivo") != mot:
                mud.append({"regra": "H3", "antes": {"estado": r["estado"], "exclusao": r.get("exclusao")}})
                r["estado"] = "excluido"; r["exclusao"] = {"motivo": mot, "nota": nota + " (revisao do orquestrador, harmonizacao-t3-v1)"}
                cont["H3"] += 1
        if mud:
            r.setdefault("harmonizacao", []).append({"versao": VERSAO, "data": agora, "mudancas": mud})
            log.append({"id": r["id"], "versao": VERSAO, "data": agora, "mudancas": mud})
            print(r["id"], [m["regra"] for m in mud])
            if aplicar:
                tmp = p + ".tmp"; json.dump(r, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); os.replace(tmp, p)
    print(cont, "APLICADO" if aplicar else "(simulacao)")
    if aplicar and log:
        with open(J("auditoria", "harmonizacao-t3.jsonl"), "a", encoding="utf-8", newline="\n") as f:
            for l in log: f.write(json.dumps(l, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
