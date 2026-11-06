---
tipo: brief-revisor
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: vigente
---

# Revisão independente do piloto — PESQUISA-IPTU

Você é revisor. **Não altere nenhum arquivo** (modo só leitura). Raiz: ``.

Objetivo: dizer se o piloto (E3) está correto e reprodutível antes da expansão. Leia `metodologia/protocolo-v1.md`, `metodologia/dicionario-de-dados.md`, `schemas/decisao.schema.json`, os scripts em `scripts/`, os 24 registros em `dados/decisoes/`, os textos em `evidencias/extracoes/`, os recibos em `auditoria/` e o dossiê `analises/teses/TES-001-imunidade-onus-da-destinacao.md`.

Verifique, com o arquivo e a linha de cada achado:
1. **Classificação:** para cada registro, o `resultado` por questão bate com o dispositivo e com quem recorreu? `materia_examinada`, `natureza_beneficio` e `efeito_sobre_ato_anterior` seguem o dicionário? Há exclusão (EXC-07) que não devia ser exclusão, ou o contrário?
2. **Rastreabilidade:** cada afirmação do dossiê TES-001 tem apoio no registro ou na fonte citada? Algo no dossiê vai além do texto disponível (só ementa)?
3. **Scripts:** a varredura (`varrer_f.py`), a triagem (`triar.py`), a deduplicação e o `validar.py` fazem o que o protocolo diz? Há caminho em que um registro some sem recibo, ou em que dois atos distintos são fundidos?
4. **Jurimetria:** algum número em `jurimetria/` ou no dossiê sugere taxa ou tendência que o desenho (amostra intencional) não permite?

Classifique cada achado como GRAVE (muda resultado, classificação ou conclusão), MÉDIO ou LEVE. Responda em português, em lista, começando pelos graves. Se não houver grave, diga isso expressamente.
