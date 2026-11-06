"""Receptor local (127.0.0.1:8799, so esta maquina) para gravar pecas lidas no PJe 2G pelo Chrome assistido.
POST /salvar  JSON {processo, id_documento, tipo, html, texto, url_sem_ca} -> evidencias/pje2g/<cnj>/<id>-<tipo>.html/.txt/.meta.json (sha256).
Recibos em auditoria/pje2g-leituras.jsonl. Encerrar com Ctrl+C ou GET /fim. Uso: python -I scripts/receptor_pje.py"""
import datetime as dt, hashlib, json, os, re, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(RAIZ, *p)
TZ = dt.timezone(dt.timedelta(hours=-3))


class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "https://pje2g.tjba.jus.br")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Private-Network", "true")

    def do_OPTIONS(self):
        self.send_response(204); self._cors(); self.end_headers()

    def do_GET(self):
        self.send_response(200); self._cors(); self.end_headers(); self.wfile.write(b"ok")
        if self.path == "/fim": threading.Thread(target=self.server.shutdown).start()

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0)); d = json.loads(self.rfile.read(n).decode("utf-8"))
        cnj = re.sub(r"[^\d.-]", "", d.get("processo", "sem"))[:25]; did = re.sub(r"\D", "", str(d.get("id_documento", "0")))[:15]
        tipo = re.sub(r"\W+", "_", d.get("tipo", "doc"))[:30]
        pasta = J("evidencias", "pje2g", cnj); os.makedirs(pasta, exist_ok=True)
        base = os.path.join(pasta, f"{did}-{tipo}")
        h = (d.get("html") or "").encode("utf-8"); t = (d.get("texto") or "").encode("utf-8")
        open(base + ".html", "wb").write(h); open(base + ".txt", "wb").write(t)
        meta = {"processo": d.get("processo"), "id_documento": did, "tipo": d.get("tipo"), "sha256_html": hashlib.sha256(h).hexdigest(),
                "sha256_texto": hashlib.sha256(t).hexdigest(), "chars_texto": len(t.decode("utf-8")), "fonte": "PJe 2G TJBA (pje2g.tjba.jus.br), autos lidos com o titular logado (A1), Chrome assistido",
                "lido_em": dt.datetime.now(TZ).isoformat(timespec="seconds")}
        json.dump(meta, open(base + ".meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        with open(J("auditoria", "pje2g-leituras.jsonl"), "a", encoding="utf-8", newline="\n") as f: f.write(json.dumps(meta, ensure_ascii=False) + "\n")
        self.send_response(200); self._cors(); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps({"ok": True, "arquivo": os.path.basename(base), "chars": meta["chars_texto"]}).encode())

    def log_message(self, *a): pass


if __name__ == "__main__":
    print("receptor em 127.0.0.1:8799", flush=True)
    HTTPServer(("127.0.0.1", 8799), H).serve_forever()
