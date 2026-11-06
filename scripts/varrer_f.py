"""Varredura NEUTRA e exaustiva dos bancos JSONL de acervo local (TJBA/STJ/STF) por mencao a IPTU.

Uso:  python -I scripts/varrer_f.py --banco tjba --arquivos <glob> [--saida derivados/hits-tjba.jsonl]
- Le arquivo a arquivo (lotes leves), prioridade BelowNormal (psutil), rg como pre-filtro.
- Cada acerto vira: {banco, arquivo, linha, sha256_linha, familias[], registro}  (registro = JSON original).
- Recibo por arquivo em auditoria/buscas.jsonl (protocolo v1, consulta Q-NEUTRA-01).
- Idempotente: arquivo ja varrido (mesmo tamanho+mtime) e pulado; estado em estado/varredura.json.
O acervo acervo local e so lido. Nada e escrito fora da raiz do projeto.
"""
import argparse, glob, hashlib, json, os, re, subprocess, sys, datetime as dt

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTOCOLO = "v1"
CONSULTA = "Q-NEUTRA-01"
# familias neutras de vocabulario (protocolo v1, sec. 4). Sem termos de resultado.
FAMILIAS = {
    "F1_sigla": r"\biptus?\b|\bi\.p\.t\.u\b",
    "F2_predial_territorial": r"predial\s+e\s+territorial\s+urban",
    "F3_propriedade_predial": r"propriedade\s+predial",
    "F4_imposto_predial": r"imposto\s+predial",
    "F5_territorial_urbano": r"imposto\s+territorial\s+urbano",
}
PRE = r"(?i)(\biptus?\b|\bi\.p\.t\.u\b|predial\s+e\s+territorial|propriedade\s+predial|imposto\s+predial|territorial\s+urbano)"
RX = {k: re.compile(v, re.I) for k, v in FAMILIAS.items()}


def baixa_prioridade():
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS if os.name == "nt" else 10)
    except Exception as e:  # registra, nao aborta
        print("aviso: prioridade nao ajustada:", e, file=sys.stderr)


def agora():
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec="seconds")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--banco", required=True)
    ap.add_argument("--arquivos", required=True, help="glob dos JSONL")
    ap.add_argument("--saida", default=None)
    ap.add_argument("--max-arquivos", type=int, default=0, help="lote: quantos arquivos nesta passada (0=todos)")
    ap.add_argument("--refazer", action="store_true", help="apaga saida e estado do banco e varre de novo")
    a = ap.parse_args()
    baixa_prioridade()
    saida = a.saida or os.path.join(RAIZ, "derivados", f"hits-{a.banco}.jsonl")
    est_p = os.path.join(RAIZ, "estado", "varredura.json")
    est = json.load(open(est_p, encoding="utf-8")) if os.path.exists(est_p) else {}
    if a.refazer:  # reconstrucao limpa: apaga a saida e o estado deste banco
        if os.path.exists(saida): os.remove(saida)
        est = {k: v for k, v in est.items() if not k.startswith(a.banco + "|")}
    elif not os.path.exists(saida) and any(k.startswith(a.banco + "|") for k in est):
        sys.exit(f"saida {saida} ausente mas o estado diz que ha arquivos varridos: rode com --refazer")
    arqs = sorted(glob.glob(a.arquivos))
    feitos = 0
    for arq in arqs:
        st = os.stat(arq)
        chave = f"{a.banco}|{os.path.normcase(os.path.abspath(arq))}"   # '/' x '\' nao pode mudar a chave
        assin = f"{st.st_size}|{int(st.st_mtime)}"
        if est.get(chave, {}).get("assinatura") == assin:
            continue
        if chave in est:  # fonte mudou depois da varredura: acrescentar duplicaria acertos antigos
            sys.exit(f"{arq} mudou desde a varredura anterior: rode com --refazer para reconstruir {saida}")
        if a.max_arquivos and feitos >= a.max_arquivos:
            break
        ini = agora()
        cnt = subprocess.run(["rg", "-c", "", arq], capture_output=True)
        n_total = int(cnt.stdout.strip() or 0)
        proc = subprocess.run(["rg", "-n", "--no-filename", "-e", PRE, arq], capture_output=True)
        if proc.returncode not in (0, 1):
            erro = proc.stderr.decode("utf-8", "replace")[:500]
            with open(os.path.join(RAIZ, "auditoria", "buscas.jsonl"), "a", encoding="utf-8") as b:
                b.write(json.dumps({"consulta": CONSULTA, "protocolo": PROTOCOLO, "banco": a.banco, "arquivo": arq,
                                    "inicio": ini, "fim": agora(), "situacao": "erro", "erro": erro}, ensure_ascii=False) + "\n")
            continue
        n_hit = n_parse_err = 0
        fam_cont = {k: 0 for k in FAMILIAS}
        with open(saida, "a", encoding="utf-8") as out:
            for raw in proc.stdout.split(b"\n"):
                if not raw:
                    continue
                num, _, linha = raw.partition(b":")
                sha = hashlib.sha256(linha).hexdigest()
                try:
                    reg = json.loads(linha.decode("utf-8"))
                except Exception:
                    n_parse_err += 1
                    reg = None
                txt = linha.decode("utf-8", "replace")
                fams = [k for k, r in RX.items() if r.search(txt)]
                for k in fams:
                    fam_cont[k] += 1
                out.write(json.dumps({"banco": a.banco, "arquivo": arq, "linha": int(num), "sha256_linha": sha,
                                      "familias": fams, "registro": reg}, ensure_ascii=False) + "\n")
                n_hit += 1
        rec = {"consulta": CONSULTA, "protocolo": PROTOCOLO, "banco": a.banco, "fonte": "acervo local (acervo interno confirmado)",
               "arquivo": arq, "expressao": PRE, "familias": FAMILIAS, "campo": "linha JSON inteira (ementa+conteudo+metadados)",
               "inicio": ini, "fim": agora(), "registros_no_arquivo": n_total, "retornados": n_hit,
               "coletados": n_hit, "por_familia": fam_cont, "erros_parse": n_parse_err,
               "limite_conhecido": "nenhum (leitura integral do arquivo)", "situacao": "concluida"}
        with open(os.path.join(RAIZ, "auditoria", "buscas.jsonl"), "a", encoding="utf-8") as b:
            b.write(json.dumps(rec, ensure_ascii=False) + "\n")
        est[chave] = {"assinatura": assin, "fim": rec["fim"], "registros": n_total, "hits": n_hit}
        json.dump(est, open(est_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        feitos += 1
        print(f"{os.path.basename(arq)}: {n_total} registros, {n_hit} hits", flush=True)


if __name__ == "__main__":
    main()
