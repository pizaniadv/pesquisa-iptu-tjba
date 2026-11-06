"""Sonda de cobertura da API TJBA (so contagens): compara recortes de um dia/mes para achar subcontagem.
Uso: python -I scripts/sonda_tjba_api.py 2025-03-10"""
import json, sys, urllib.request
URL = "https://jurisprudenciaws.tjba.jus.br/graphql"
HDR = {"Content-Type": "application/json", "Origin": "https://jurisprudencia.tjba.jus.br", "Referer": "https://jurisprudencia.tjba.jus.br/"}
Q = "query($f:DecisaoFilter,$p:Int,$i:Int){ filter(decisaoFilter:$f,pageNumber:$p,itemsPerPage:$i){ itemCount orgaos{ key value } } }"


def cnt(dia, sg, tr, ac, mo, campo="dataPublicacao"):
    f = {"assunto": "", "orgaos": [], "relatores": [], "classes": [], "dataInicial": f"{dia}T00:00:00.000Z",
         "dataFinal": f"{dia}T23:59:59.999Z", "segundoGrau": sg, "turmasRecursais": tr, "tipoAcordaos": ac,
         "tipoDecisoesMonocraticas": mo, "ordenadoPor": campo}
    req = urllib.request.Request(URL, data=json.dumps({"query": Q, "variables": {"f": f, "p": 0, "i": 1}}).encode(), headers=HDR, method="POST")
    d = json.load(urllib.request.urlopen(req, timeout=120))
    return d.get("data", {}).get("filter", {}).get("itemCount") if "data" in d and d["data"] else d


dia = sys.argv[1]
for combo in [(True, True, True, True), (True, False, True, True), (False, True, True, True), (True, True, True, False), (True, True, False, True)]:
    print(combo, cnt(dia, *combo))
print("ordenado dataJulgamento", cnt(dia, True, True, True, True, "dataJulgamento"))
