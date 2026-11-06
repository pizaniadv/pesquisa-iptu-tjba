"""Funcoes comuns (deterministicas) dos scripts da PESQUISA-IPTU.
limpar_html v1: remove estilos/XML do Word/comentarios/tags, desescapa entidades, normaliza espacos (preserva quebra de paragrafo).
mapa_espacos/achar: mesma regra de conferencia literal do validar.py (tolerancia SO a espacos colapsados)."""
import html, re

LIMPEZA_VERSAO = "limpar_html-v1"
_RE = [
    (re.compile(r"(?is)<!--.*?-->"), " "),
    (re.compile(r"(?is)<(style|script|xml)\b.*?</\1\s*>"), " "),
    (re.compile(r"(?is)<w:[^>]*>|</w:[^>]*>|<o:[^>]*>|</o:[^>]*>|<m:[^>]*>|</m:[^>]*>"), " "),
    (re.compile(r"(?i)<\s*(br|/p|/div|/li|/tr|/h\d)\b[^>]*>"), "\n"),
    (re.compile(r"(?s)<[^>]{0,2000}>"), " "),
]


def limpar_html(t):
    t = t or ""
    for rx, rep in _RE: t = rx.sub(rep, t)
    t = html.unescape(t).replace("\xa0", " ").replace("\r", "")
    t = re.sub(r"[ \t\f\v]+", " ", t)
    t = re.sub(r" *\n[ \n]*", "\n", t)
    return t.strip()


def mapa_espacos(t):
    out, pos, prev = [], [], False
    for i, ch in enumerate(t):
        if ch.isspace():
            if prev: continue
            out.append(" "); pos.append(i); prev = True
        else:
            out.append(ch); pos.append(i); prev = False
    return "".join(out), pos


def achar(txt, colap, pos, q):
    i = txt.find(q)
    if i >= 0: return i, i + len(q), "literal"
    qc = re.sub(r"\s+", " ", q).strip()
    if not qc: return None
    j = colap.find(qc)
    if j >= 0: return pos[j], pos[j + len(qc) - 1] + 1, "literal_espacos_colapsados"
    return None
