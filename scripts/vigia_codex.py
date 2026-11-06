"""Vigia leve: testa 1 documento a cada 10 min (texto pelo canal do servidor de coleta). Quando o Codex do CNJ voltar a devolver texto de verdade,
roda pdpj_inteiro_teor.py sobre os alvos e sai. Teto: 8 h. Uso: python -I scripts/vigia_codex.py --alvos estado/pdpj/alvos-E4-IPTU04-1.json"""
import argparse, datetime as dt, os, re, subprocess, sys, time, urllib.request, json
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROVA = ("80136018720218050000", "b5855e34-97f9-5e98-8ea2-0bb0d4f62836")  # acordao de DEC-TJBA-54e2028fe848
ERRO = re.compile(r"(?i)codex indispon|circuitbreaker|unauthorized")


def chave():
    for l in open(os.environ["PDPJ_API_CHAVE_ARQ"], encoding="utf-8"):  # arquivo local com a chave (fora do repositorio)
        l = l.strip()
        if l and not l.startswith("#"): return l


def texto_ok(k):
    url = os.environ.get("PDPJ_API_BASE", "https://<servidor-pdpj-api>/u/{k}").format(k=k) + f"/api/processos/{PROVA[0]}/documentos/{PROVA[1]}/texto"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "pesquisa-iptu"}), timeout=120) as r:
            t = ((json.loads(r.read().decode("utf-8")).get("resultado") or {}).get("texto") or "")
    except Exception as e:
        return False, str(e)[:120]
    return (len(t) > 500 and not ERRO.search(t[:400])), t[:120].replace("\n", " ")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--alvos", required=True); a = ap.parse_args()
    k = chave(); fim = time.time() + 8 * 3600
    while time.time() < fim:
        ok, amostra = texto_ok(k)
        print(dt.datetime.now().strftime("%H:%M"), "OK" if ok else "indisponivel", "|", amostra, flush=True)
        if ok:
            r = subprocess.run([sys.executable, "-I", os.path.join(RAIZ, "scripts", "pdpj_inteiro_teor.py"), "--alvos", a.alvos], cwd=RAIZ)
            print("CODEX VOLTOU; busca concluida, saida", r.returncode, flush=True); return
        time.sleep(600)
    print("TETO DE 8 H SEM O CODEX", flush=True)


if __name__ == "__main__":
    main()
