"""Aplica aos registros (dados/decisoes/) os ajustes da conferencia de inteiro teor da TES-001
(analises/teses/TES-001-conferencia-inteiro-teor-v1.json). Regra: metodologia/harmonizacao-t3-v1.md (valor anterior guardado).
Cada operacao abaixo transcreve um item de "ajustes" do arquivo de conferencia; nada fora dele, salvo C2 (completude/leitura,
porque o inteiro teor foi lido na conferencia, como o proprio arquivo anota). Idempotente: o que ja tem o valor novo e pulado.
Log: auditoria/ajustes-conferencia-it.jsonl. Uso: python -I scripts/aplicar_conferencia_it.py [--aplicar]"""
import copy, glob, json, os, sys
from datetime import datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
VERSAO = "conferencia-inteiro-teor-v1"
REVISOR = {"quem": "conferencia-inteiro-teor-v1 (leitor Opus, PJe 2G + PDPJ)", "tipo": "automatizada", "data": "2026-11-06"}


def q(r, n):
    return next(x for x in r["questoes"] if x["id"].endswith("#Q%d" % n))


def prec(r, n, trecho):
    return next(p for p in q(r, n)["precedentes_usados"] if trecho in p["ref"])


def excerto_pdpj(texto, arquivo, rid):
    for p in glob.glob(J("evidencias", "pdpj", "*", arquivo)) + glob.glob(J("evidencias", "pje2g", "*", arquivo)):
        t = open(p, encoding="utf-8", errors="replace").read()
        i = t.find(texto)
        if i >= 0:
            rel = os.path.relpath(p, RAIZ).replace("\\", "/")
            return {"texto": texto, "voz": "relator", "localizador": "%s:%d-%d" % (rel, i, i + len(texto)), "conferido_no_original": True}
    raise SystemExit("excerto nao achado: %s %s" % (rid, arquivo))


# (registro, descricao do campo, funcao que le o valor atual, funcao que grava o novo, valor novo)
def ops():
    P = "Q4 desfavoravel com objeto praticamente esvaziado: debitos de IPTU cancelados administrativamente como imunes (voto, III.2); perda do objeto por parcelamento (PAD/PPI 2567000-0/2025) alegada e nao enfrentada"
    return [
        ("DEC-TJBA-54e2028fe848", "datas.julgamento", lambda r: r["datas"]["julgamento"], lambda r, v: r["datas"].__setitem__("julgamento", v), "2021-10-26"),
        # antialucinacao F7 (A-04, 06/11): Decisao Proclamada "Salvador, 4 de Novembro de 2020." (evidencias/pdpj/DEC-TJBA-c7e23238cce4/0049-Acórdão.txt)
        ("DEC-TJBA-c7e23238cce4", "datas.julgamento", lambda r: r["datas"]["julgamento"], lambda r, v: r["datas"].__setitem__("julgamento", v), "2020-11-04"),
        ("DEC-TJBA-741220024f98", "datas.julgamento", lambda r: r["datas"]["julgamento"], lambda r, v: r["datas"].__setitem__("julgamento", v), "2024-10-29"),
        ("DEC-TJBA-741220024f98", "contexto.exercicios", lambda r: r["contexto"]["exercicios"], lambda r, v: r["contexto"].__setitem__("exercicios", v), ["2016", "2017", "2018"]),
        ("DEC-TJBA-833447ef42a8", "datas.julgamento", lambda r: r["datas"]["julgamento"], lambda r, v: r["datas"].__setitem__("julgamento", v), "2025-06-18"),
        ("DEC-TJBA-833447ef42a8", "Q1.precedentes_usados[REsp 825496].uso", lambda r: prec(r, 1, "825496")["uso"], lambda r, v: prec(r, 1, "825496").__setitem__("uso", v), "aplicacao_determinante"),
        ("DEC-TJBA-833447ef42a8", "Q1.precedentes_usados[TJMG 5041504].uso", lambda r: prec(r, 1, "5041504")["uso"], lambda r, v: prec(r, 1, "5041504").__setitem__("uso", v), "aplicacao_determinante"),
        ("DEC-TJBA-02bbc8cc1826", "datas.julgamento", lambda r: r["datas"]["julgamento"], lambda r, v: r["datas"].__setitem__("julgamento", v), "2025-11-17"),
        ("DEC-TJBA-02bbc8cc1826", "qualidade.pendencias(+Q4)", None, None, "APPEND", ("qualidade", "pendencias", lambda r: P)),
        ("DEC-TJBA-02bbc8cc1826", "Q1.precedentes_usados(+AgInt REsp 1.706.777)", None, None, "APPEND_PREC", (1, {"ref": "STJ, AgInt no REsp 1.706.777/SC, Rel. Min. Herman Benjamin, 2ª Turma, DJe 16/10/2018", "uso": "aplicacao_determinante"})),
        ("DEC-TJBA-9d673755fc33", "Q2.precedentes_usados(+2 AgRg)", None, None, "APPEND_PREC", (2, {"ref": "STJ, AgRg no AREsp 789.362/SP, Rel. Min. Humberto Martins, 2ª Turma, DJe 13/11/2015", "uso": "aplicacao_determinante"})),
        ("DEC-TJBA-9d673755fc33", "Q2.precedentes_usados(+2 AgRg)b", None, None, "APPEND_PREC", (2, {"ref": "STJ, AgRg no AREsp 105.288/SP, Rel. Min. Humberto Martins, 2ª Turma, DJe 28/03/2012", "uso": "aplicacao_determinante"})),
        ("DEC-TJBA-9d673755fc33", "Q2.subtema(+uso proprio)", lambda r: q(r, 2)["subtema"], lambda r, v: q(r, 2).__setitem__("subtema", v),
         "SUFIXO", "; imóvel em uso próprio (sede da entidade sindical, terreno doado pelo Município); presunção relativa rejeitada"),
        ("DEC-TJBA-9d673755fc33", "qualidade.pendencias(decisao mantida)", None, None, "APPEND", ("qualidade", "pendencias", lambda r: "resolvida na conferência de inteiro teor: decisão mantida = interlocutória da 9ª Vara da Fazenda Pública de Salvador que indeferiu a exceção; agravo interno declarado prejudicado no voto")),
        ("DEC-TJBA-261b7411ef90", "Q1.precedentes_usados(+2 AgInt)", None, None, "APPEND_PREC", (1, {"ref": "STJ, AgInt no REsp 1.875.655/SP, Rel. Min. Og Fernandes, 2ª Turma, DJe 15/03/2021", "uso": "referencia_incidental"})),
        ("DEC-TJBA-261b7411ef90", "Q1.precedentes_usados(+2 AgInt)b", None, None, "APPEND_PREC", (1, {"ref": "STJ, AgInt no AREsp 1.284.672/SP, Rel. Min. Mauro Campbell Marques, 2ª Turma, DJe 10/09/2018", "uso": "referencia_incidental"})),
        ("DEC-TJBA-261b7411ef90", "Q1.objeto_do_resultado", lambda r: q(r, 1)["objeto_do_resultado"], lambda r, v: q(r, 1).__setitem__("objeto_do_resultado", v),
         "mantida a tutela que suspendeu a cobrança das parcelas do parcelamento e a exigibilidade dos créditos de IPTU"),
        ("DEC-TJBA-e3b4aef87c1f", "datas.julgamento", lambda r: r["datas"]["julgamento"], lambda r, v: r["datas"].__setitem__("julgamento", v), "2025-06-30"),
        ("DEC-TJBA-e3b4aef87c1f", "Q2.subtema(trecho do onus)", lambda r: q(r, 2)["subtema"], lambda r, v: q(r, 2).__setitem__("subtema", v),
         "TROCA", ("ônus da prova da destinação com o contribuinte, que a cumpriu por prova documental pré-constituída",
                   "ônus dividido: a entidade demonstrou documentalmente os requisitos e a destinação por prova documental pré-constituída; o ônus de provar o não atendimento/desvio de finalidade é do fisco (voto do agravo), reafirmado nos ED")),
        ("DEC-TJBA-e3b4aef87c1f", "contexto.exercicios", lambda r: r["contexto"]["exercicios"], lambda r, v: r["contexto"].__setitem__("exercicios", v), ["2019", "2020"]),
        ("DEC-TJBA-e3b4aef87c1f", "contexto.diplomas_municipais", lambda r: r["contexto"]["diplomas_municipais"], lambda r, v: r["contexto"].__setitem__("diplomas_municipais", v),
         ["Lei Municipal nº 8.814/2015 (Salvador), juntada pela excipiente"]),
        ("DEC-TJBA-bed5fa300da4", "Q1.precedentes_usados", lambda r: q(r, 1)["precedentes_usados"], lambda r, v: q(r, 1).__setitem__("precedentes_usados", v), [
            {"ref": "STJ, REsp 1.698.305/RJ, Rel. Min. Herman Benjamin, 2ª Turma, DJe 19/12/2017", "uso": "aplicacao_determinante"},
            {"ref": "TJPE, Remessa Necessária Cível 5466366, Rel. Ricardo de Oliveira Paes Barreto, 2ª Câmara de Direito Público, j. 13/02/2020", "uso": "aplicacao_determinante"},
            {"ref": "STJ, EDcl no AgRg no REsp 1.078.751/SC, Rel. Min. Benedito Gonçalves, 1ª Turma, DJe 27/10/2010", "uso": "referencia_incidental"}]),
        ("DEC-TJBA-bed5fa300da4", "Q2.efeito_sobre_ato_anterior", lambda r: q(r, 2)["efeito_sobre_ato_anterior"], lambda r, v: q(r, 2).__setitem__("efeito_sobre_ato_anterior", v), "reforma"),
        ("DEC-TJBA-bed5fa300da4", "Q3.objeto_do_resultado", lambda r: q(r, 3)["objeto_do_resultado"], lambda r, v: q(r, 3).__setitem__("objeto_do_resultado", v),
         "honorários de 15% sobre o proveito econômico, 70% a cargo do Município e 30% da embargante (sentença: 10% recíprocos)"),
    ]


def main():
    aplicar = "--aplicar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    regs, log = {}, {}
    for op in ops():
        rid, campo = op[0], op[1]
        r = regs.setdefault(rid, json.load(open(J("dados", "decisoes", rid + ".json"), encoding="utf-8")))
        novo = op[4]
        if novo == "APPEND":
            sec, k, fn = op[5]
            atual = r.setdefault(sec, {}).setdefault(k, []) or []
            r[sec][k] = atual
            item = fn(r)
            if item in atual: print("ja", rid, campo); continue
            antes = copy.deepcopy(atual); atual.append(item)
        elif novo == "APPEND_PREC":
            n, item = op[5]
            qq = q(r, n); atual = qq.get("precedentes_usados") or []
            qq["precedentes_usados"] = atual
            if any(p["ref"] == item["ref"] for p in atual): print("ja", rid, campo); continue
            antes = copy.deepcopy(atual); atual.append(item)
        elif novo == "TROCA":
            antes = op[2](r); de, para = op[5]
            if para in antes: print("ja", rid, campo); continue
            if de not in antes: raise SystemExit("trecho nao achado: %s %s" % (rid, campo))
            op[3](r, antes.replace(de, para))
        elif novo == "SUFIXO":
            antes = op[2](r); suf = op[5]
            if antes.endswith(suf): print("ja", rid, campo); continue
            op[3](r, antes + suf)
        else:
            antes = copy.deepcopy(op[2](r))
            if antes == novo: print("ja", rid, campo); continue
            op[3](r, copy.deepcopy(novo))
        log.setdefault(rid, []).append({"campo": campo, "antes": antes})
        print("muda", rid, campo, "| antes:", json.dumps(antes, ensure_ascii=False)[:90])
    # C2: completude e leitura (inteiro teor lido na conferencia)
    for rid, r in regs.items():
        ql = r["qualidade"]
        if ql.get("completude") != "inteiro_teor" or ql.get("leitura") != "inteiro_teor_lido":
            log.setdefault(rid, []).append({"campo": "C2 qualidade.completude/leitura", "antes": {"completude": ql.get("completude"), "leitura": ql.get("leitura")}})
            ql["completude"], ql["leitura"] = "inteiro_teor", "inteiro_teor_lido"
            print("muda", rid, "C2 completude/leitura")
        if REVISOR not in ql.setdefault("revisor", []) and rid in log:
            ql["revisor"].append(REVISOR)
    print("registros com mudanca:", len(log), "operacoes:", sum(len(v) for v in log.values()))
    if not aplicar:
        print("(simulacao; use --aplicar)"); return
    agora = datetime.now().astimezone().isoformat(timespec="seconds")
    with open(J("auditoria", "ajustes-conferencia-it.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
        for rid, muds in log.items():
            fh.write(json.dumps({"id": rid, "versao": VERSAO, "data": agora, "fonte": "analises/teses/TES-001-conferencia-inteiro-teor-v1.json", "mudancas": muds}, ensure_ascii=False) + "\n")
    for rid in log:
        with open(J("dados", "decisoes", rid + ".json"), "w", encoding="utf-8", newline="\r\n") as fh:  # convencao dos registros: CRLF
            json.dump(regs[rid], fh, ensure_ascii=False, indent=1)
    print("gravado")


if __name__ == "__main__":
    main()
