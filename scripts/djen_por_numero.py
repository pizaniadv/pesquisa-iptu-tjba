"""Busca no DJEN (comunicaapi.pje.jus.br, publico, so leitura) as comunicacoes de cada processo-alvo e guarda o texto integral publicado.
Saida: evidencias/djen/<id>/<idComunicacao>.json (resposta integral do item) e .txt (texto). Recibos: auditoria/buscas.jsonl (consulta Q-DJEN-NUM).
Uso: python -I scripts/djen_por_numero.py --alvos estado/pdpj/alvos-E4-IPTU04-1.json"""
import argparse, datetime as dt, hashlib, json, os, re, time, urllib.error, urllib.parse, urllib.request
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
API = "https://comunicaapi.pje.jus.br/api/v1/comunicacao"
TZ = dt.timezone(dt.timedelta(hours=-3))


def get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    for t in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "pesquisa-iptu/1.0", "Accept": "application/json"}), timeout=60) as r:
                return r.status, json.loads(r.read().decode("utf-8")), url
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and t < 4: time.sleep(4 * (t + 1)); continue
            return e.code, {"erro": e.read().decode("utf-8", "replace")[:300]}, url
        except Exception as e:
            if t < 4: time.sleep(4 * (t + 1)); continue
            return 0, {"erro": str(e)[:300]}, url
        finally:
            time.sleep(1.0)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--alvos", required=True); a = ap.parse_args()
    alvos = json.load(open(J(a.alvos), encoding="utf-8"))["alvos"]
    feitos = set()
    for al in alvos:
        num = re.sub(r"\D", "", al["processo"])[:20]
        pasta = J("evidencias", "djen", al["id"]); os.makedirs(pasta, exist_ok=True)
        itens, pag = [], 1
        if num in feitos:  # mesmo processo de outro alvo: reaproveita
            print(al["id"], al["processo"], "(mesmo processo de alvo anterior)"); continue
        while True:
            st, d, url = get({"numeroProcesso": num, "pagina": pag, "itensPorPagina": 100})
            lote = d.get("items") or [] if isinstance(d, dict) else []
            itens += lote
            if len(lote) < 100 or pag >= 10: break
            pag += 1
        feitos.add(num)
        for it in itens:
            iid = str(it.get("id") or it.get("hash") or hashlib.sha256(json.dumps(it, sort_keys=True).encode()).hexdigest()[:16])
            json.dump(it, open(os.path.join(pasta, iid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            txt = it.get("texto") or ""
            open(os.path.join(pasta, iid + ".txt"), "w", encoding="utf-8", newline="\n").write(txt)
        rec = {"data": dt.datetime.now(TZ).isoformat(timespec="seconds"), "consulta": "Q-DJEN-NUM", "banco": "djen", "id": al["id"], "processo": al["processo"],
               "url": url.split("?")[0] + "?numeroProcesso=" + num, "http": st, "retornados": len(itens),
               "datas": sorted({(i.get("data_disponibilizacao") or i.get("datadisponibilizacao") or "")[:10] for i in itens})[-6:],
               "tipos": sorted({(i.get("tipoDocumento") or i.get("tipoComunicacao") or "") for i in itens})}
        with open(J("auditoria", "buscas.jsonl"), "a", encoding="utf-8", newline="\n") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(al["id"], al["processo"], "http", st, "comunicacoes", len(itens), "tipos", rec["tipos"][:5], "ultimas", rec["datas"][-3:])


if __name__ == "__main__":
    main()
