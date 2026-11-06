"""Coleta a linha final de cada leitor T3 (determinacao do Opus sobre o onus da destinacao) a partir das transcricoes dos subagentes.
Le os .output (JSONL) do diretorio de tarefas da sessao, filtra os que receberam o brief-leitor-t3, pega o ultimo texto do assistente
e separa por ' | ' -> estado/t3/respostas-leitores.jsonl (fica no projeto; o diretorio de tarefas e temporario).
Uso: python -I scripts/coletar_respostas_t3.py <dir_tarefas>"""
import glob, json, os, re, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID = re.compile(r"^(DEC-[A-Z0-9]+-[0-9a-f]{12})\s*\|")


def textos(p):
    primeiro, ultimo = None, None
    for l in open(p, encoding="utf-8", errors="replace"):
        try: e = json.loads(l)
        except json.JSONDecodeError: continue
        if not isinstance(e, dict): continue
        m = e.get("message") or {}
        if not isinstance(m, dict): continue
        c = m.get("content")
        if isinstance(c, list): t = "\n".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
        elif isinstance(c, str): t = c
        else: continue
        if m.get("role") == "user" and primeiro is None and t: primeiro = t
        if m.get("role") == "assistant" and t.strip(): ultimo = t
    return primeiro or "", ultimo or ""


def main():
    out, n = [], 0
    for p in sorted(glob.glob(os.path.join(sys.argv[1], "agent-*.jsonl"))):
        ini, fim = textos(p)
        if "brief-leitor-t3-v1.1" not in ini: continue
        n += 1
        for l in fim.splitlines():
            l = l.strip()
            m = ID.match(l)
            if not m: continue
            partes = [x.strip() for x in l.split(" | ")]
            onus = next((x for x in partes if x.lower().startswith("ônus da destinação") or x.lower().startswith("onus da destinacao")), "")
            v = onus.split(":", 1)[1].strip() if ":" in onus else ""
            vl = v.lower()
            cat = ("misto" if ("munic" in vl and "contribu" in vl) else "municipio" if vl.startswith("munic") else
                   "contribuinte" if vl.startswith("contribu") else "nao_tratado" if vl.startswith("não tratado") or vl.startswith("nao tratado") else "outro")
            out.append({"id": m.group(1), "status": partes[1] if len(partes) > 1 else "", "n_questoes": partes[2] if len(partes) > 2 else "",
                        "resultados": partes[3] if len(partes) > 3 else "", "onus_texto": v, "onus": cat,
                        "duvida": " | ".join(partes[5:]) if len(partes) > 5 else "", "transcricao": os.path.basename(p)})
    dest = os.path.join(RAIZ, "estado", "t3", "respostas-leitores.jsonl")
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    import collections
    print("leitores", n, "linhas", len(out), "ids unicos", len({r["id"] for r in out}), collections.Counter(r["onus"] for r in out))


if __name__ == "__main__":
    main()
