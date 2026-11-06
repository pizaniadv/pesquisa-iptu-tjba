---
tipo: ficha-de-tese
data: 2026-11-06
produzido-por: claude-code (leitor Opus E4-3)
versao-core: 1.0
status: draft
tese: 24
---

# TES-24 — Competência ou foro em causas de IPTU

## 1. Formulação

Se a causa do contribuinte discute elemento da obrigação de IPTU (base de cálculo, valor venal, repetição do indébito), então deve correr na vara da Fazenda Pública com competência tributária. Se a execução fiscal já foi proposta, a mudança posterior de domicílio do executado não desloca a competência.

**Advertência de leitura:** o material **não traz nenhuma decisão do TJBA favorável ao contribuinte** nesta tese. A formulação descreve uma regra de organização do processo, neutra quanto ao resultado, e não uma vitória do contribuinte.

## 2. Fundamento normativo

- Súmula 58/STJ (texto abaixo, conferido).
- Distribuição de competência entre as Varas da Fazenda Pública fiscais e administrativas de Salvador: lei de organização judiciária ou resolução do TJBA não lida [A CONFERIR].
- CPC, art. 46, § 5º: "A execução fiscal será proposta no foro de domicílio do réu, no de sua residência ou no do lugar onde for encontrado." O compilado do Planalto remete às ADI 5737 e 5492 (STF); o efeito delas sobre o § 5º não foi conferido aqui. O dispositivo não aparece no pacote.

## 3. Como o TJBA decide

**Números.** Catálogo: 0 favoráveis, 0 contrários. Acervo: 210 decisões, 194 processos, 23 processos com indício favorável (recorte por palavra; indício, não taxa). Na amostra (8) e nos 6 itens vistos da API, 13 dos 14 vêm de Turmas Recursais dos Juizados Especiais (incompetência pelo valor da causa em litígios de consumo ou locação que só mencionam o IPTU), sem pertinência com a relação tributária.

**Órgãos e período.** O único julgado pertinente é das Seções Cíveis Reunidas, de 2021. O resto vem das Turmas Recursais (2020 a 2026), fora do tema.

**Regra que aparece (neutra).** Ação revisional de valor venal com pedido de repetição é matéria tributária e cabe à vara fazendária fiscal.
- 0555415-68.2015.8.05.0001 (Seções Cíveis Reunidas, 01/07/2021), conflito negativo entre varas da Fazenda Pública de Salvador: "MATÉRIA COM EVIDENTE REPERCUSSÃO NA ESFERA TRIBUTÁRIA. COMPETÊNCIA DA VARA FAZENDÁRIA FISCAL (SUSCITADO)."

**Contrárias.** Nenhuma na mesma questão. Os casos dos Juizados sobre incompetência pelo valor (por exemplo, 0099343-53.2020.8.05.0001, Segunda Turma Recursal, 17/07/2024: "A COMPETÊNCIA DEVE SER FIRMADA PELO PROVEITO ECONÔMICO RECLAMADO.") são de compra e venda de imóvel entre particulares. Não servem como precedente para IPTU, porque falta identidade de causa.

**DJEN.** A frase "incompetência IPTU" devolveu 0 itens.

## 4. Precedentes qualificados do STJ e do STF

| Identificador | Teor | Fonte | Situação |
|---|---|---|---|
| STJ, Súmula 58 | "Proposta a execução fiscal, a posterior mudança de domicílio do executado não desloca a competência já fixada." | Cognitio `STJ:sumulas:58` | conferido. Neutra ou contrária ao executado que se muda |
| STJ, Tema 373 | execução fiscal da União na comarca do domicílio do devedor sem vara federal (art. 15, I, Lei 5.010/66) | PANGEA `stj-rr-373`; Cognitio `STJ:paradigmas:Tema-373` (leading case REsp 1.146.194) | conferido (tese): "A execução fiscal proposta pela União e suas autarquias deve ser ajuizada perante o Juiz de Direito da comarca do domicílio do devedor, quando esta não for sede de vara da justiça federal." **Não se aplica** à execução de IPTU municipal |

Nenhum precedente qualificado do material afirma competência favorável ao contribuinte em causa de IPTU.

## 5. Via processual

- Exceção ou preliminar de **incompetência** na contestação ou nos embargos (CPC); em conflito, **conflito de competência** suscitado pelo juízo.
- Para a ação do contribuinte (anulatória, revisional, repetição), distribuí-la desde logo na **vara fazendária fiscal**: evita o conflito e o atraso que se viu em 0555415-68.2015.
- **Prova:** basta a petição inicial e o pedido; a competência se define pela causa de pedir e pelo pedido.

## 6. Walton e Élenchos

- **Argumento determinante:** a causa que discute a base de cálculo do IPTU é classificada como causa tributária. A ação do contribuinte discute o valor venal. Logo, é tributária e cabe à vara fiscal.
- **Esquema:** `ARG.SCH.WRM08.VERBAL_CLASSIFICATION` (WRM2008, p. 319).
- **Perguntas críticas (ônus):**
  - CQ1, do proponente: que prova há de que o caso tem a propriedade F, com margem de dúvida? **Respondida quanto à classificação** (0555415-68.2015: a ação revisional de valor venal com repetição é "MATÉRIA COM EVIDENTE REPERCUSSÃO NA ESFERA TRIBUTÁRIA"); **não respondida quanto ao proveito do contribuinte**: nenhum julgado em que a classificação lhe tenha trazido resultado favorável. O WEAK mede a utilidade da tese, não a correção da classificação.
  - CQ2, do questionador: a classificação depende de suposição discutível sobre o uso das palavras? Não alegada.
- **Status devolvido pelo motor:** `WEAK_UNANSWERED_CQ` (CQ1 pendente; exceção não alegada: CQ2).

## 7. Limites e o que falta

- Tese vazia no catálogo. O recorte por palavra ("incompetência" com IPTU) captou ruído dos Juizados.
- O 1º grau está ausente, e é nele que as exceções de incompetência se decidem. A DJEN não devolveu nada. A API subconta e não é neutra (121 itens brutos; os 6 vistos são de Turmas Recursais dos Juizados Especiais).
- A lei de organização judiciária do TJBA e a distribuição entre varas fiscais e administrativas não foram lidas. Só ementa.

## 8. Utilidade prática

- **Quando usar:** só como cuidado de distribuição: propor a ação tributária de IPTU na vara fiscal.
- **Quando não usar:** como tese de defesa que gere vitória do contribuinte. Não há base no material, e a Súmula 58 impede deslocar a execução por mudança de domicílio.
- **Risco:** baixo valor estratégico. Recomenda-se rebaixar a tese no catálogo ou fundi-la com outra.

**Revisão pós-Codex (06/11/2026).** Item 3 do Codex, JSON: `n_acervo` 23 → 194 (era o subconjunto favorável; agora é o total de processos do recorte por palavra) e `n_acervo_fav` = 23. Item 9 do Codex, 'quase todas de Juizados Especiais' → 13 de 14 (amostra e API); API 'quase todos de consumo' → os 6 vistos. Registro: `auditoria/correcoes-pos-codex-e43.jsonl`; originais em `estado/E4-3/antes-pos-codex/`.
