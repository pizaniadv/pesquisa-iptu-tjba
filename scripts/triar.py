"""Triagem T1 (deterministica) dos acertos brutos da varredura neutra -> candidatos.
Uso: python -I scripts/triar.py --banco tjba
- Deduplica por sha256 da linha (EXC-04 bytes) e por identidade judicial (numero+tipo+data julgamento+orgao).
- Nivel de pertinencia (INDICIO, nao classificacao): A1 IPTU na ementa | A2 'Assunto: IPTU' no cabecalho |
  A3 Municipio parte + IPTU no texto | A4 so mencao no corpo (precedente citado / dado de fato).
- Extrai facetas indiciarias para estratificar o piloto: instancia, tipo, classe, municipio, eixos por palavra-chave,
  sinal do dispositivo e polo do Municipio no recurso. Tudo marcado como 'indicio_T1'.
Saida: dados/candidatos-<banco>.jsonl ; recibos de duplicata em auditoria/exclusoes-T1-<banco>.jsonl (regenerado a cada
execucao, gravacao atomica). Regra v2 (05/11/2026, achado GRAVE do Codex): so funde quando, alem de processo+tipo+data+
orgao, a CLASSE e o TEXTO (ementa+conteudo, espacos colapsados) sao iguais; ato distinto sob a mesma chave-base ganha id
proprio (chave-base + sha do texto). EXC-07 (mencao) NAO e decidida na T1 (protocolo v2).
"""
import argparse, json, os, re, hashlib, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RX_IPTU = re.compile(r"(?i)\biptus?\b|\bi\.p\.t\.u\b|predial\s+e\s+territorial\s+urban|imposto\s+predial|propriedade\s+predial|imposto\s+territorial\s+urbano")
RX_ASSUNTO = re.compile(r"(?i)assunto\s*:?\s*iptu")
RX_MUN_PARTE = re.compile(r"(?i)(apelante|apelad[oa]|agravante|agravad[oa]|recorrente|recorrid[oa]|impetrad[oa]|embargante|embargad[oa]|autor|r[ée]u|requerid[oa]|excepto)\s*:\s*(o\s+)?munic[ií]pio\s+d[eo]\s+([A-ZÀ-Ü][A-Za-zÀ-ü' ]{2,40}?)(?=\s+(advogad|procurador|apelad|agravad|recorrid|ac[oó]rd|$)|\s*[,;])")
RX_MUN = re.compile(r"(?i)munic[ií]pio\s+d[eo]\s+([A-ZÀ-Ü][A-Za-zÀ-ü']+(?:\s+(?:d[aeo]s?\s+)?[A-ZÀ-Ü][A-Za-zÀ-ü']+){0,3})")
RX_MUN_RECORRE = re.compile(r"(?i)(apelante|agravante|recorrente|embargante)\s*:\s*(o\s+)?munic[ií]pio")
DISP = [("parcial", re.compile(r"(?i)(dar|deu|d[aã]o|dou)\s+parcial\s+provimento|parcialmente\s+provid|provimento\s+parcial")),
        ("provido", re.compile(r"(?i)\b(dar|deu|d[aã]o|dou)\s+provimento|recurso\s+provido|apelo\s+provido")),
        ("desprovido", re.compile(r"(?i)negar\s+provimento|negou[-\s]se\s+provimento|nego\s+provimento|desprovid|improvid|n[aã]o\s+provid")),
        ("nao_conhecido", re.compile(r"(?i)n[aã]o\s+conhec(er|ido|eram|eu)")),
        ("concedida", re.compile(r"(?i)conceder?\s+a\s+seguran[cç]a|seguran[cç]a\s+concedida")),
        ("denegada", re.compile(r"(?i)denegar?\s+a\s+seguran[cç]a|seguran[cç]a\s+denegada"))]
EIXOS = {
    "IPTU-01": r"zona\s+urbana|expans[aã]o\s+urbana|\bitr\b|destina[cç][aã]o\s+rural|im[oó]vel\s+rural",
    "IPTU-02": r"sujei[cç][aã]o\s+passiva|sujeito\s+passivo|possuidor|compromiss[aá]rio|dom[ií]nio\s+[uú]til|locat[aá]rio|ilegitimidade\s+passiva",
    "IPTU-03": r"arremata|sucess[aã]o|aliena[cç][aã]o\s+fiduci|credor\s+fiduci|responsabilidade\s+tribut",
    "IPTU-04": r"imunidade",
    "IPTU-05": r"isen[cç][aã]o",
    "IPTU-06": r"valor\s+venal|planta\s+gen[eé]rica|base\s+de\s+c[aá]lculo|metragem|[aá]rea\s+constru",
    "IPTU-07": r"progressiv|al[ií]quota",
    "IPTU-08": r"majora[cç][aã]o|anterioridade|noventena|decreto|legalidade",
    "IPTU-09": r"notifica[cç][aã]o|carn[eê]|lan[cç]amento",
    "IPTU-10": r"prescri[cç][aã]o|decad[eê]ncia|intercorrente",
    "IPTU-11": r"execu[cç][aã]o\s+fiscal|\bcda\b|certid[aã]o\s+de\s+d[ií]vida|pr[eé][-\s]?executividade",
    "IPTU-12": r"penhora|bem\s+de\s+fam[ií]lia|constri[cç]",
    "IPTU-13": r"tutela|liminar|suspens[aã]o\s+da\s+exigibilidade|certid[aã]o\s+(positiva|negativa)",
    "IPTU-14": r"repeti[cç][aã]o\s+de\s+ind[eé]bito|restitui[cç][aã]o|compensa[cç][aã]o",
    "IPTU-15": r"honor[aá]rios|multa|juros",
    "IPTU-17": r"taxa\s+de\s+(coleta|lixo|limpeza)|res[ií]duos\s+s[oó]lidos|ilumina[cç][aã]o\s+p[uú]blica|cosip|\bitbi\b",
}
RX_EIXOS = {k: re.compile(v, re.I) for k, v in EIXOS.items()}


CORTE_MUN = re.compile(r"(?i)\s+(advogad|proc|apelad|apelant|agravad|agravant|recorrid|recorrent|embargad|interessad|ac[oó]rd|relator|vistos|ementa|e\s+outr|requerid)\w*.*$")


def limpa_mun(x):
    x = re.split(r"[\r\n\t]", x)[0]
    x = re.sub(r"(?i)\s+(contra\s+senten|proc\b).*$", "", x)
    x = CORTE_MUN.sub("", x).strip(" .,;:-")
    return x.upper() or None


def norm_num(n):
    return re.sub(r"\D", "", n or "")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--banco", required=True); a = ap.parse_args()
    src = os.path.join(RAIZ, "derivados", f"hits-{a.banco}.jsonl")
    out_p = os.path.join(RAIZ, "dados", f"candidatos-{a.banco}.jsonl")
    vistos_sha, vistos_id = {}, {}
    cont = collections.Counter(); n = 0
    exc_p = os.path.join(RAIZ, "auditoria", f"exclusoes-T1-{a.banco}.jsonl")
    exc = open(exc_p + ".tmp", "w", encoding="utf-8")
    bases = {}
    with open(src, encoding="utf-8") as f, open(out_p + ".tmp", "w", encoding="utf-8") as out:
        for line in f:
            h = json.loads(line); n += 1; r = h.get("registro") or {}
            ptr = f"{h['arquivo']}:{h['linha']}"
            if h["sha256_linha"] in vistos_sha:
                exc.write(json.dumps({"motivo": "EXC-04", "nota": "bytes identicos", "candidato": ptr, "igual_a": vistos_sha[h['sha256_linha']]}, ensure_ascii=False) + "\n")
                cont["dup_bytes"] += 1; continue
            vistos_sha[h["sha256_linha"]] = ptr
            if a.banco == "tjba":
                ident = "|".join([norm_num(r.get("numeroProcesso")), r.get("tipoDecisao") or "", (r.get("dataJulgamento") or "")[:10], (r.get("orgaoJulgador") or {}).get("nome", "")])
            elif a.banco == "cmt":  # varios acordaos por edicao do DOM: 'arquivo' NAO identifica o ato
                ident = "|".join([str(r.get("edicao") or ""), str(r.get("processo") or ""), str(r.get("recorrente") or ""),
                                  str(r.get("relator") or ""), (r.get("ementa") or "")[:160]])
            else:  # STJ/STF: cada registro aponta um .md proprio; identidade = arquivo + classe + numero
                ident = "|".join([str(r.get("arquivo") or h["sha256_linha"]), str(r.get("classe") or r.get("classe_sigla") or ""),
                                  str(r.get("numero_processo") or r.get("processo_numero") or r.get("numero_tema") or r.get("numero") or "")])
            em = r.get("ementa") or r.get("tese") or r.get("enunciado") or r.get("indexacao") or ""
            co = r.get("conteudo") or r.get("descricao") or ""; cab = (em[:2500] + " " + co[:2500])
            classe_s = (r.get("classe") or {}).get("descricao") if isinstance(r.get("classe"), dict) else str(r.get("classe") or "")
            sha_txt = hashlib.sha256(re.sub(r"\s+", " ", (em + " " + co)).strip().encode("utf-8")).hexdigest()
            chave_ato = ident + "|" + (classe_s or "") + "|" + sha_txt
            if chave_ato in vistos_id:
                exc.write(json.dumps({"motivo": "EXC-04", "nota": "mesmo ato: chave-base + classe + texto identicos (republicacao/reingestao)", "candidato": ptr, "igual_a": vistos_id[chave_ato]}, ensure_ascii=False) + "\n")
                cont["dup_ident"] += 1; continue
            vistos_id[chave_ato] = ptr
            if ident in bases:   # mesma chave-base, ato DISTINTO -> id proprio
                cont["mesma_base_ato_distinto"] += 1
                id_semente = ident + "|" + sha_txt
            else:
                bases[ident] = ptr; id_semente = ident
            if RX_IPTU.search(em): nivel = "A1"
            elif RX_ASSUNTO.search(cab): nivel = "A2"
            elif RX_MUN_PARTE.search(cab) or RX_MUN.search(cab[:1500]): nivel = "A3"
            else: nivel = "A4"
            cont[nivel] += 1
            mun = RX_MUN.search(cab)
            texto = em + " " + co
            disp = [k for k, rx in DISP if rx.search(texto[-4000:] if len(texto) > 4000 else texto)]
            eixos = [k for k, rx in RX_EIXOS.items() if rx.search(em or co[:6000])]
            num = r.get("numeroProcesso") or ""
            cid = ("DEC-TJBA-" if a.banco == "tjba" else f"DEC-{a.banco.upper().replace('-', '')[:8]}-") + hashlib.sha256(id_semente.encode()).hexdigest()[:12]
            out.write(json.dumps({
                "id": cid, "ponteiro": ptr, "sha256_linha": h["sha256_linha"], "nivel_T1": nivel,
                "numero_processo": num or str(r.get("numero_processo") or r.get("processo_numero") or r.get("numero_tema") or r.get("numero") or ""), "instancia": r.get("instancia"), "tipo": r.get("tipoDecisao"),
                "classe": (r.get("classe") or {}).get("descricao") if isinstance(r.get("classe"), dict) else r.get("classe"),
                "orgao": (r.get("orgaoJulgador") or {}).get("nome") if isinstance(r.get("orgaoJulgador"), dict) else r.get("orgao"),
                "relator": (r.get("relator") or {}).get("nome") if isinstance(r.get("relator"), dict) else r.get("relator"),
                "data_julgamento": (r.get("dataJulgamento") or r.get("julgamento_data") or "")[:10], "data_publicacao": (r.get("dataPublicacao") or "")[:10],
                "municipio_indicio": limpa_mun(mun.group(1)) if mun else None,
                "municipio_recorre_indicio": bool(RX_MUN_RECORRE.search(cab)),
                "dispositivo_indicio": disp, "eixos_indicio": eixos,
                "tem_conteudo": bool(co), "tam_texto": len(texto), "sha256_texto_norm": sha_txt, "chave_base": ident, "familias": h["familias"], "indicio": "T1-deterministico"
            }, ensure_ascii=False) + "\n")
    exc.close()
    os.replace(out_p + ".tmp", out_p); os.replace(exc_p + ".tmp", exc_p)   # atomico: so substitui no fim
    rec = {"etapa": "T1", "versao_regra": "v2", "banco": a.banco, "brutos": n, **cont, "candidatos_unicos": n - cont["dup_bytes"] - cont["dup_ident"]}
    open(os.path.join(RAIZ, "auditoria", "triagem.jsonl"), "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(json.dumps(rec, ensure_ascii=False))


if __name__ == "__main__":
    main()
