"""Correcao pos-Codex (rodada 2, estado/codex-revisao-e43-r2.md, item 2), 06/11/2026.
Preliminar de admissibilidade do RECURSO (dialeticidade) que foi EXAMINADA e REJEITADA nao e `sem_exame`: o dicionario
(metodologia/dicionario-de-dados.md, linha 36) reserva `sem_exame` a questao nao examinada, e a H1 da harmonizacao cobre recurso
inadmitido. Resultado pelo lado do contribuinte, sem confundir com merito:
- recurso do contribuinte conhecido (preliminar do Municipio rejeitada) -> favoravel_integral, natureza processual;
- recurso do Municipio conhecido (preliminar do contribuinte rejeitada) -> desfavoravel.
materia_examinada continua `admissibilidade`. Log com o valor anterior em auditoria/correcoes.jsonl. Idempotente.
Uso: python -I scripts/corrigir_preliminar_admissibilidade.py [--aplicar]"""
import json, os, sys
from datetime import datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
ALVOS = [("DEC-TJBA-fd5f8aeaf0cc#Q1", "favoravel_integral", "processual", "preliminar de dialeticidade do Municipio rejeitada; agravo da contribuinte conhecido"),
         ("DEC-TJBA-eec4d6425623#Q2", "desfavoravel", None, "preliminar de dialeticidade da contribuinte rejeitada; agravo do Municipio conhecido")]


def main():
    aplicar = "--aplicar" in sys.argv; agora = datetime.now().astimezone().isoformat(timespec="seconds")
    for qid, res, nat, motivo in ALVOS:
        rid = qid.split("#")[0]; p = J("dados", "decisoes", rid + ".json"); r = json.load(open(p, encoding="utf-8"))
        q = next(x for x in r["questoes"] if x["id"] == qid)
        assert q["materia_examinada"] == "admissibilidade", qid
        if q["resultado"] == res and q.get("natureza_beneficio") == nat: print("ja", qid); continue
        antes = {"resultado": q["resultado"], "natureza_beneficio": q.get("natureza_beneficio")}
        q["resultado"], q["natureza_beneficio"] = res, nat
        r.setdefault("qualidade", {}).setdefault("pendencias", []).append("pos-Codex r2 (06/11/2026): %s -> %s (%s)" % (qid.split("#")[1], res, motivo))
        print("muda", qid, antes, "->", res, nat)
        if aplicar:
            with open(p, "w", encoding="utf-8", newline="\r\n") as fh: json.dump(r, fh, ensure_ascii=False, indent=1)
            with open(J("auditoria", "correcoes.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps({"data": agora, "origem": "revisao Codex E4-3 rodada 2 (estado/codex-revisao-e43-r2.md), item 2", "alvo": qid, "antes": antes,
                                     "depois": {"resultado": res, "natureza_beneficio": nat}, "motivo": motivo + "; sem_exame so para questao nao examinada (dicionario)",
                                     "nota": "substitui a decisao de manter registrada na linha anterior deste log (rodada 1)"}, ensure_ascii=False) + "\n")
    if not aplicar: print("(simulacao; use --aplicar)")


if __name__ == "__main__":
    main()
