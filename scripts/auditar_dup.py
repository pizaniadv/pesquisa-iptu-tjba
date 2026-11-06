"""Audita fusoes EXC-04 'mesma identidade judicial' do TJBA: compara classe e tamanho do texto entre os pares."""
import json, collections, sys
def ler(ptr):
    arq, _, ln = ptr.rpartition(':'); ln = int(ln)
    with open(arq, 'rb') as fh:
        for i, raw in enumerate(fh, 1):
            if i == ln: return json.loads(raw.decode('utf-8'))
pares = [json.loads(l) for l in open('auditoria/exclusoes.jsonl', encoding='utf-8') if 'identidade' in l and 'JURISPRUD' in l]
import random; random.Random(7).shuffle(pares)
dif = 0; n = 0
for p in pares[:25]:
    a, b = ler(p['candidato']), ler(p['igual_a']); n += 1
    ca, cb = (a.get('classe') or {}).get('descricao'), (b.get('classe') or {}).get('descricao')
    same_id = a.get('id') == b.get('id'); same_txt = (a.get('conteudo') or '') == (b.get('conteudo') or '')
    if ca != cb or not same_txt: dif += 1
    print(same_id, same_txt, ca, '|', cb, len(a.get('conteudo') or ''), len(b.get('conteudo') or ''))
print('pares', len(pares), 'amostra', n, 'diferentes', dif)
