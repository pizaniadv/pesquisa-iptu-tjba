"""Busca o inteiro teor de decisoes-alvo pela pdpj-api do servidor de coleta (canal oficial, REST; so leitura; o servidor limita a <= 2 req/s).
Para cada registro: lista de documentos do processo -> escolhe as pecas decisorias (Acordao, Voto, Relatorio, Ementa, Decisao) juntadas
entre julgamento-60d e julgamento+45d (sem data: as 8 mais recentes desses tipos) -> baixa o texto (data lake; reserva pelo Portal v2).
Saida: evidencias/pdpj/<id>/documentos.json, <seq>-<tipo>.txt (+ .meta.json com sha256 e fonte_texto). Recibos: auditoria/pdpj-consultas.jsonl.
Uso: python -I scripts/pdpj_inteiro_teor.py --alvos estado/pdpj/alvos-<lote>.json"""
import argparse, datetime as dt, hashlib, json, os, re, time, urllib.error, urllib.parse, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
BASE = os.environ.get("PDPJ_API_BASE", "https://<servidor-pdpj-api>/u/{k}") + "/api/processos/{cnj}"  # servidor REST de leitura da PDPJ
TIPOS = re.compile(r"(?i)ac[óo]rd|voto|ementa|relat[óo]rio|decis")
TZ = dt.timezone(dt.timedelta(hours=-3))
ERRO_TXT = re.compile(r"(?i)erro ao tentar recuperar arquivo no codex|codex indispon|circuitbreaker|unauthorized|n[ãa]o possui acesso")  # a reserva do portal devolve o erro como se fosse texto


def chave():
    for l in open(os.environ["PDPJ_API_CHAVE_ARQ"], encoding="utf-8"):  # arquivo local com a chave (fora do repositorio)
        l = l.strip()
        if l and not l.startswith("#"): return l
    raise SystemExit("chave nao encontrada")


def get(url):
    for t in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "pesquisa-iptu"}), timeout=120) as r:
                return r.status, json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            corpo = e.read().decode("utf-8", "replace")[:300]
            if e.code in (429, 502, 503, 504) and t < 3: time.sleep(5 * (t + 1)); continue
            return e.code, {"erro_http": e.code, "corpo": corpo}
        except Exception as e:  # rede
            if t < 3: time.sleep(5 * (t + 1)); continue
            return 0, {"erro": str(e)[:300]}
        finally:
            time.sleep(0.6)


def recibo(d):
    with open(J("auditoria", "pdpj-consultas.jsonl"), "a", encoding="utf-8", newline="\n") as f: f.write(json.dumps(d, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--alvos", required=True); ap.add_argument("--so-lista", action="store_true"); a = ap.parse_args()
    k = chave(); alvos = json.load(open(J(a.alvos), encoding="utf-8"))["alvos"]
    for al in alvos:
        rid, cnj = al["id"], re.sub(r"\D", "", al["processo"])[:20]
        pasta = J("evidencias", "pdpj", rid); os.makedirs(pasta, exist_ok=True)
        st, d = get(BASE.format(k=k, cnj=cnj) + "/documentos")
        agora = dt.datetime.now(TZ).isoformat(timespec="seconds")
        res = d.get("resultado") if isinstance(d, dict) else None
        docs = (res or {}).get("documentos") or []
        dp = os.path.join(pasta, "documentos.json")
        if docs or not os.path.exists(dp):  # resposta vazia ou com erro nao apaga a lista boa ja gravada (revisao Codex, item 6)
            json.dump(d, open(dp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        else:
            json.dump(d, open(os.path.join(pasta, "documentos.ultima-falha.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        recibo({"data": agora, "consulta": "documentos", "id": rid, "processo": al["processo"], "http": st, "n_documentos": len(docs), "erro": d.get("erro") if isinstance(d, dict) else None})
        if not docs: print(rid, "SEM DOCUMENTOS", st, (d.get("erro") or d.get("erro_http")) if isinstance(d, dict) else ""); continue
        dec = [x for x in docs if TIPOS.search((x.get("tipo") or {}).get("nome", "") + " " + (x.get("nome") or ""))]
        jul = al.get("julgamento")
        if jul:
            j0 = dt.date.fromisoformat(jul[:10])
            sel = [x for x in dec if (x.get("dataHoraJuntada") or "")[:10] and -60 <= (dt.date.fromisoformat(x["dataHoraJuntada"][:10]) - j0).days <= 45]
        else: sel = []
        if not sel: sel = sorted(dec, key=lambda x: x.get("dataHoraJuntada") or "", reverse=True)[:8]
        if al.get("sequencias"):  # alvo pontual (releitura H2, 06/11): pecas indicadas pelo leitor, qualquer tipo
            sel = [x for x in docs if x.get("sequencia") in al["sequencias"]]
            json.dump([x["id"] for x in sel], open(os.path.join(pasta, "selecionados-pontuais.json"), "w", encoding="utf-8"))
        n_ok = 0
        if not al.get("sequencias"): json.dump([x["id"] for x in sel[:12]], open(os.path.join(pasta, "selecionados.json"), "w", encoding="utf-8"))
        if a.so_lista: print(rid, al["processo"], "docs", len(docs), "decisorios", len(dec), "selecionados", len(sel[:12])); continue
        for x in (sel if al.get("sequencias") else sel[:12]):
            st2, t = get(BASE.format(k=k, cnj=cnj) + "/documentos/" + urllib.parse.quote(str(x["id"])) + "/texto")
            r2 = (t.get("resultado") if isinstance(t, dict) else None) or {}
            txt = r2.get("texto") if isinstance(r2, dict) else None
            if txt is None and isinstance(t, dict): txt = t.get("texto")
            tipo = re.sub(r"\W+", "_", (x.get("tipo") or {}).get("nome", "doc"))[:30]
            base = os.path.join(pasta, f"{x.get('sequencia', 0):04d}-{tipo}")
            if os.path.exists(base + ".meta.json"):
                try: id_ant = json.load(open(base + ".meta.json", encoding="utf-8")).get("id_documento")
                except ValueError: id_ant = x["id"]  # meta parcial de execucao interrompida: refaz este mesmo documento (revisao Codex r2)
                if id_ant != x["id"]: base += "-" + str(x["id"])[:8]  # mesma sequencia e tipo, documento diferente (a lista do data lake repete sequencias)
            ok = bool(txt and txt.strip()) and not ERRO_TXT.search((txt or "")[:400])
            if ok and os.path.exists(base + ".txt") and os.path.exists(base + ".meta.json"): n_ok += 1; continue  # ja baixado (retomada; texto sem meta e refeito)
            if ok:
                b = txt.encode("utf-8"); n_ok += 1
                json.dump({"id_documento": x["id"], "idCodex": x.get("idCodex"), "sequencia": x.get("sequencia"), "tipo": (x.get("tipo") or {}).get("nome"),
                           "juntada": x.get("dataHoraJuntada"), "signatarios": x.get("signatarios"), "sha256_texto": hashlib.sha256(b).hexdigest(),
                           "fonte_texto": (r2.get("fonte_texto") if isinstance(r2, dict) else None) or (t.get("fonte_texto") if isinstance(t, dict) else None),
                           "processo": al["processo"], "consultado_em": dt.datetime.now(TZ).isoformat(timespec="seconds")},
                          open(base + ".meta.json.tmp", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                os.replace(base + ".meta.json.tmp", base + ".meta.json")  # meta tambem por troca atomica (revisao Codex r2)
                open(base + ".txt.tmp", "wb").write(b); os.replace(base + ".txt.tmp", base + ".txt")  # texto so depois do meta, por troca atomica (revisao Codex, item 6)
            recibo({"data": dt.datetime.now(TZ).isoformat(timespec="seconds"), "consulta": "texto", "id": rid, "processo": al["processo"], "documento": x["id"],
                    "tipo": (x.get("tipo") or {}).get("nome"), "http": st2, "ok": ok, "chars": len(txt or ""), "erro": (t.get("erro") or t.get("erro_http")) if isinstance(t, dict) and not ok else None})
        print(rid, al["processo"], "docs", len(docs), "decisorios", len(dec), "selecionados", len(sel if al.get("sequencias") else sel[:12]), "textos", n_ok)


if __name__ == "__main__":
    main()
