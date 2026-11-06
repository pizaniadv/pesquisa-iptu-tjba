"""Exporta de <ACERVO>/PANGEA/pangea.db (somente leitura) os precedentes qualificados com mencao a IPTU.
Consulta Q-NEUTRA-PANGEA-01 (FTS5). Saida: evidencias/pangea-iptu.jsonl + recibo em auditoria/buscas.jsonl."""
import sqlite3, json, hashlib, os, datetime as dt
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPR = 'iptu OR iptus OR "predial e territorial" OR "imposto predial" OR "propriedade predial" OR "territorial urbano"'
c = sqlite3.connect("file:" + os.environ.get("PANGEA_DB", "<ACERVO>/PANGEA/pangea.db") + "?mode=ro", uri=True)
cols = [r[1] for r in c.execute('pragma table_info(precedentes)')]
ini = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat(timespec='seconds')
rows = list(c.execute(f"select {','.join(cols)} from precedentes where precedentes match ?", (EXPR,)))
total = c.execute('select count(*) from precedentes').fetchone()[0]
with open(os.path.join(RAIZ, 'evidencias', 'pangea-iptu.jsonl'), 'w', encoding='utf-8') as f:
    for r in rows:
        d = dict(zip(cols, r)); s = json.dumps(d, ensure_ascii=False, sort_keys=True)
        d['_sha256'] = hashlib.sha256(s.encode('utf-8')).hexdigest(); d['_fonte'] = '<ACERVO>/PANGEA/pangea.db (espelho BNP/CNJ)'
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
rec = {"consulta": "Q-NEUTRA-PANGEA-01", "protocolo": "v1", "banco": "pangea", "arquivo": "<ACERVO>/PANGEA/pangea.db", "expressao": EXPR,
       "campo": "FTS5 (todas as colunas)", "inicio": ini, "registros_no_arquivo": total, "retornados": len(rows), "coletados": len(rows),
       "limite_conhecido": "so precedentes qualificados; espelho de 21/07/2026", "situacao": "concluida"}
open(os.path.join(RAIZ, 'auditoria', 'buscas.jsonl'), 'a', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False) + '\n')
print(len(rows), 'de', total)
