"""Gera visoes derivadas (nunca editar a mao): exports/decisoes.csv, exports/questoes.csv, exports/questao_tese.csv,
jurimetria/funil.json (cobertura da trilha neutra) e jurimetria/piloto-composicao.json (composicao do piloto, COM listas de IDs).
O piloto e amostra intencional estratificada por indicio: NAO se calcula taxa de exito sobre ele (protocolo v1 §8)."""
import csv, glob, json, os, collections, datetime as dt
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)


def val(x):
    if isinstance(x, dict) and "valor" in x: return f"[{x.get('motivo')}]"
    return x if x is not None else ""


def main():
    regs = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(J("dados", "decisoes", "*.json")))]
    os.makedirs(J("exports"), exist_ok=True); os.makedirs(J("jurimetria"), exist_ok=True)
    with open(J("exports", "decisoes.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(["id", "estado", "tribunal", "grau", "orgao", "classe", "especie_ato", "numero", "julgamento", "publicacao", "municipio", "completude", "leitura", "verificacao", "via", "exclusao", "n_questoes", "ponteiro"])
        for r in regs:
            i, d, c, q = r["identificacao"], r.get("datas", {}), r.get("contexto", {}), r.get("qualidade", {})
            w.writerow([r["id"], r["estado"], i["tribunal"], i["grau"], val(i.get("orgao")), val(i.get("classe")), i["especie_ato"], i["numero_processo"].get("original"),
                        val(d.get("julgamento")), val(d.get("publicacao")), val(c.get("municipio")), q.get("completude"), q.get("leitura"), q.get("verificacao"),
                        "|".join(r.get("via_descoberta", [])), (r.get("exclusao") or {}).get("motivo", ""), len(r.get("questoes", [])), r["fonte"]["ponteiro"]])
    with open(J("exports", "questoes.csv"), "w", newline="", encoding="utf-8-sig") as f, open(J("exports", "questao_tese.csv"), "w", newline="", encoding="utf-8-sig") as g:
        w = csv.writer(f); wt = csv.writer(g)
        w.writerow(["questao_id", "decisao_id", "tributo", "eixo", "subtema", "pergunta", "materia_examinada", "resultado", "objeto_do_resultado", "natureza_beneficio", "provisoriedade", "efeito_sobre_ato_anterior", "n_fundamentos", "chave_questao_comparavel"])
        wt.writerow(["questao_id", "tese_id"])
        for r in regs:
            for q in r.get("questoes", []):
                w.writerow([q["id"], r["id"], q["tributo"], q["eixo"], q.get("subtema", ""), q["pergunta"], q.get("materia_examinada"), q["resultado"], q.get("objeto_do_resultado", ""),
                            q.get("natureza_beneficio") or "", q.get("provisoriedade", ""), q.get("efeito_sobre_ato_anterior", ""), len(q.get("fundamento_determinante", [])), q.get("chave_questao_comparavel") or ""])
                for t in q.get("teses", []): wt.writerow([q["id"], t])
    with open(J("auditoria", "exclusoes-registros.jsonl"), "w", encoding="utf-8") as fx:  # visao gerada a partir dos registros
        for r in regs:
            if r["estado"] == "excluido":
                fx.write(json.dumps({"registro": r["id"], "motivo": (r.get("exclusao") or {}).get("motivo"), "nota": (r.get("exclusao") or {}).get("nota"), "ponteiro": r["fonte"]["ponteiro"]}, ensure_ascii=False) + chr(10))
    # composicao do piloto (unidade = questao; so IPTU; so registros nao excluidos)
    comp = collections.defaultdict(lambda: collections.defaultdict(list))
    piloto = [r for r in regs if any(x.get("quem") == "leitor-opus-piloto" for x in (r.get("qualidade") or {}).get("revisor") or [])]
    for r in piloto:  # so o piloto E3 (os registros da E4 tem tabela propria por tese)
        if r["estado"] == "excluido": continue
        for q in r.get("questoes", []):
            if q["tributo"] != "IPTU": continue
            comp[q["eixo"]][q["resultado"]].append(q["id"])
    out = {"gerado_em": dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds"),
           "universo": "piloto E3 (amostra intencional estratificada por indicio T1, semente 20261105) — NAO representativo",
           "unidade": "questao decidida (tributo=IPTU), registros nao excluidos", "taxa_de_exito": "nao calculavel por desenho (amostra dirigida)",
           "registros": len(piloto), "excluidos": [r["id"] for r in piloto if r["estado"] == "excluido"],
           "por_eixo": {e: {k: {"n": len(v), "ids": v} for k, v in d.items()} for e, d in sorted(comp.items())}}
    json.dump(out, open(J("jurimetria", "piloto-composicao.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # funil da trilha neutra (unidade = registro/linha), a partir dos recibos
    fun = collections.defaultdict(lambda: {"arquivos": 0, "registros_percorridos": 0, "acertos_brutos": 0})
    for l in open(J("auditoria", "buscas.jsonl"), encoding="utf-8"):
        b = json.loads(l)
        if b.get("calibracao") or not b.get("consulta", "").startswith("Q-NEUTRA"): continue
        k = b.get("banco"); fun[k]["arquivos"] += 1
        fun[k]["registros_percorridos"] += b.get("registros_no_arquivo") or b.get("percorridos") or 0
        fun[k]["acertos_brutos"] += b.get("retornados") or 0
    tri = {}
    for l in open(J("auditoria", "triagem.jsonl"), encoding="utf-8"):
        t = json.loads(l); tri[t["banco"]] = t  # ultima execucao vale
    json.dump({"unidade": "registro do banco (linha) -> candidato unico", "recibos": dict(fun), "triagem_T1_ultima": tri},
              open(J("jurimetria", "funil.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(regs), "registros exportados")


if __name__ == "__main__":
    main()
