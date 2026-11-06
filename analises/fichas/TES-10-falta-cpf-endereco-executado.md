---
tipo: ficha-de-tese
data: 2026-11-06
produzido-por: claude-code (leitor Opus E4-3)
versao-core: 1.0
status: draft
tese: 10
---

# TES-10 — Falta de CPF, endereço ou qualificação do executado

## 1. Formulação

Se o Município ajuíza execução fiscal de IPTU sem o CPF/CNPJ ou sem endereço válido do executado e, intimado para emendar ou diligenciar, não supre a falta, então a execução se extingue sem mérito (arts. 321 e 485, III ou IV, do CPC; art. 1º-A da Resolução CNJ 547/2024, na redação da Resolução CNJ 617/2025, quanto ao CPF), mesmo diante da Súmula 558 e do Tema 876 do STJ, que decisões do TJBA de 2025-2026 afastam por distinção (7 decisões na linha b do § 3, 1 delas do catálogo; a distinção é expressa no texto de 3: 8000948-69.2020, 0502387-05.2017 e 0503918-55.2017; sem denominador).

## 2. Fundamento normativo (o que as decisões usam)

- LEF, art. 1º (aplicação subsidiária do CPC), art. 2º, § 5º, I (endereço "sempre que conhecido"), art. 6º (requisitos da inicial).
- CTN, art. 202, I ("sempre que possível").
- CPC, arts. 321 (emenda), 485, III (abandono), IV (pressuposto) e VI (interesse); art. 485, § 1º (intimação pessoal); art. 1.021, § 4º (multa no agravo interno).
- Lei 11.419/2006, art. 15 (CPF/CNPJ na inicial do processo eletrônico), afastada pelo Tema 876.
- CF, art. 37, caput (eficiência), invocado com os Temas 1.184 e 1.428 do STF.
- Resolução CNJ 547/2024, art. 1º-A (redação da Resolução CNJ 617/2025) e Consulta CNJ 0004754-38.2025.2.00.0000: citadas nas decisões; texto não localizado em fonte primária (atos.cnj.jus.br devolveu 403 em 06/11/2026; o Cognitio não tem resoluções do CNJ): `nao_localizado`.

## 3. Como o TJBA decide

**Números.** Catálogo: 6 processos (5 favoráveis e 1 parcial), nenhuma contrária no catálogo (recorte por palavra; indício, não taxa). Acervo 2020-2026: 100 decisões, 87 processos, 53 com indício favorável (recorte por palavra; indício, não taxa). A API (`IPTU AND "CPF"`) devolve 301 itens brutos; o DJEN com a frase "CPF IPTU" devolveu zero.

**Câmaras e período.** Primeira, Segunda e Quarta Câmaras no catálogo (2020), Quarta Câmara (2026); a amostra e a API somam Primeira, Segunda, Terceira e Quarta Câmaras em 2025-2026.

**Duas linhas, com épocas diferentes.**

*a) Endereço (2020): extinção quando a Fazenda, intimada, não indica endereço válido.*
- `0751427-84.2017.8.05.0001` — Primeira Câmara Cível, 10/02/2020: «Diante da impossibilidade de citação por correio por ausência de endereço válido, as demais modalidades de citação também se mostram obstadas, impondo a extinção da execução fiscal sem resolução do mérito.»
- `0309956-36.2013.8.05.0150` — Primeira Câmara Cível, 10/02/2020: «Diante da impossibilidade de citação por correio pela ausência de endereço válido, as demais modalidades de citação também se mostram obstadas»
- `0809385-33.2014.8.05.0001` — Primeira Câmara Cível, 09/03/2020: «Para fins de tentativa da citação pelo correio, mostra-se imperiosa que já na exordial conste o endereço do executado»
- `0310038-67.2013.8.05.0150` — Segunda Câmara Cível, 15/12/2020: «OPORTUNIZADO AO MUNICIPIO FORNECER NOVO ENDEREÇO DO EXECUTADO. INERCIA. SENTENÇA MANTIDA.»
- `0307221-30.2013.8.05.0150` — Quarta Câmara Cível, 11/02/2020 (resultado parcial): «a indicação correta do endereço do réu é requisito essencial à petição inicial, porquanto sua ausência inviabiliza a citação do demandado»

*b) CPF (2025-2026): extinção por ausência de CPF, com distinção da Súmula 558 e do Tema 876.*
- `8001557-44.2021.8.05.0256` — Quarta Câmara Cível, 29/04/2026: «A ausência de fornecimento da referida identificação fulmina de ineficácia a atividade jurisdicional executiva, tornando o processo natimorto e inexequível.»
- `8008515-75.2023.8.05.0256` — Primeira Câmara Cível, 11/09/2026 (amostra): «AUSÊNCIA DE CPF DA EXECUTADA. INDISPENSABILIDADE PARA O DESENVOLVIMENTO VÁLIDO E REGULAR DO PROCESSO ELETRÔNICO.»
- `8000948-69.2020.8.05.0103` — Segunda Câmara Cível, publicado em 06/10/2026 (API): «DISTINÇÃO (DISTINGUISHING) DA SÚMULA 558 E DO TEMA 876/STJ FRENTE AO AMBIENTE DO PROCESSO ELETRÔNICO E ÀS FERRAMENTAS DE CONSTRIÇÃO PATRIMONIAL (SISBAJUD, RENAJUD, INFOJUD E SNIPER).»
- `0502387-05.2017.8.05.0103` — Segunda Câmara Cível, publicado em 06/10/2026 (API): «EFICÁCIA NORMATIVA VINCULANTE DA CONSULTA CNJ Nº 0004754-38.2025.2.00.0000.»
- `0503918-55.2017.8.05.0256` — Terceira Câmara Cível, publicado em 05/10/2026 (API): «TEMA 876 DO STJ. SÚMULA 558/STJ. DISTINGUISHING.»
- `8003697-83.2025.8.05.0103` — Quarta Câmara Cível, publicado em 02/10/2026 (API; baixo valor e CPF): «AUSÊNCIA DE INTERESSE DE AGIR E DE CPF DO DEVEDOR.»
- `8041504-92.2024.8.05.0000` — Segunda Câmara Cível, 28/03/2025 (amostra; ação rescisória do Município improcedente): «ÔNUS DO EXEQUENTE DE APRESENTAR CDA REGULAR. IMPOSSIBILIDADE DE CORREÇÃO DE OFÍCIO PELO JUDICIÁRIO.»

**A regra nos favoráveis.** Não é a falta do dado em si que extingue: é a falta do dado **depois** de intimação para emenda ou diligência não atendida. Na linha do CPF, o TJBA de 2025-2026 trata o dado como pressuposto do processo eletrônico (constrição por SISBAJUD, RENAJUD, INFOJUD e SNIPER) e diz que a Súmula 558 não alcança essa hipótese.

**As contrárias e o que as distingue (2 processos).**
- `8016313-04.2022.8.05.0004` — Terceira Câmara Cível, 09/09/2025 (amostra; recurso do Município provido): «A exigência de endereço na Certidão de Dívida Ativa condiciona-se ao conhecimento pela Fazenda Pública» — endereço desconhecido não autoriza indeferir a inicial (LEF, art. 2º, § 5º, I).
- `8001170-72.2022.8.05.0004` — Primeira Câmara Cível, 09/10/2025 (amostra; sentença anulada): «A extinção do processo por abandono exige a intimação pessoal da parte autora, o que não ocorreu no caso concreto, configurando nulidade da sentença»

**O que distingue.** A extinção se sustenta quando houve intimação (pessoal, no abandono) e inércia; cai quando o juiz indefere de plano por falta de endereço que a Fazenda não conhecia, ou extingue por abandono sem intimação pessoal. Na Terceira Câmara, convivem a anulação por endereço (8016313-04.2022) e a manutenção da extinção por CPF (0503918-55.2017): são questões distintas.

## 4. Precedentes qualificados do STJ e do STF

| Identificador | Tese (texto da fonte) | Fonte | Conferido |
|---|---|---|---|
| Súmula 558/STJ | "Em ações de execução fiscal, a petição inicial não pode ser indeferida sob o argumento da falta de indicação do CPF e/ou RG ou CNPJ da parte executada." | Cognitio `STJ:sumulas:558` | sim |
| Tema 876/STJ (REsp 1.455.091/AM) | "Em ações de execução fiscal, descabe indeferir a petição inicial sob o argumento da falta de indicação do CPF e/ou RG da parte executada (pessoa física), visto tratar-se de requisito não previsto no art. 6º da Lei nº 6.830/80 (LEF), cujo diploma, por sua especialidade, ostenta primazia sobre a legislação de cunho geral, como ocorre frente à exigência contida no art. 15 da Lei nº 11.419/06." (a fonte repete a frase para o CNPJ) | Cognitio `STJ:precedentes:Tema-876`; acórdão `STJ:paradigmas-teor:201401188624-1365117` | sim |
| Tema 1.184/STF (RE 1.355.208) | "1. É legítima a extinção de execução fiscal de baixo valor pela ausência de interesse de agir tendo em vista o princípio constitucional da eficiência administrativa, respeitada a competência constitucional de cada ente federado." (item 1 da tese; os itens 2 e 3 também estão no acervo: "2. O ajuizamento da execução fiscal dependerá da prévia adoção das seguintes providências: a) tentativa de conciliação ou adoção de solução administrativa; e b) protesto do título, salvo por motivo de eficiência administrativa, comprovando-se a inadequação da medida. 3. [...]") | Cognitio `STF:repercussao_geral:tema-1184` | sim (cadastro; acórdão não lido) |
| Tema 1.428/STF (ARE 1.553.607, RG) | questão, sem tese no acervo: "se a utilização dos parâmetros da Resolução CNJ nº 547/2024 para aferição de interesse de agir em execução fiscal viola a separação de poderes e a competência tributária do ente federativo, na hipótese de lei local fixar critérios diversos para o ajuizamento de cobrança de crédito" | Cognitio `STF:repercussao_geral:tema-1428` | confere (cadastro; pendente) |
| Tema 1.201/STJ (multa do art. 1.021, § 4º) | "1) O agravo interposto contra decisão do Tribunal de origem [...] quando apresentado contra decisão baseada em precedente qualificado oriundo do STJ ou do STF, autoriza a aplicação da multa prevista no art. 1.021, § 4º, do CPC [...]; 2) A multa prevista no art. 1.021, § 4º, CPC, não é cabível quando (i) alegada fundamentadamente a distinção ou a superação do precedente qualificado oriundo do STJ ou do STF ou (ii) a decisão agravada estiver amparada em julgado de tribunal de segundo grau; [...]" | Cognitio `STJ:precedentes:Tema-1201` | confere |
| Resolução CNJ 547/2024, art. 1º-A (Res. 617/2025) | ato normativo, não precedente; texto não localizado em fonte primária (atos.cnj.jus.br devolveu 403 em 06/11/2026; o acervo de legislação do Cognitio não tem resoluções do CNJ); a redação só aparece citada nas ementas do TJBA (8000948-69.2020, 0502387-05.2017, 0503918-55.2017) | — | `nao_localizado` |

PANGEA não trouxe nada para esta tese.
## 5. Via processual e prova

- Matéria de ordem pública: o próprio juízo extingue; em regra não há executado citado ("ausente a angularização"). A tese serve ao contribuinte em **contrarrazões** de apelação ou agravo interno do Município, ou em **exceção** quando já citado.
- Prova: certidões nos autos da intimação para emenda e do decurso do prazo; para abandono, a intimação pessoal (art. 485, § 1º).

## 6. Walton e Élenchos

- **Argumento determinante:** o caso da execução eletrônica sem CPF é exceção à regra da Súmula 558 e do Tema 876, porque a Resolução CNJ 547/2024 (art. 1º-A) e o processo eletrônico tornam o CPF condição de eficácia da execução.
- **Esquema:** `ARG.SCH.WRM08.EXCEPTIONAL_CASE` (WRM2008, p. 344).
- **CQ1 (proponente):** é um tipo reconhecido de exceção? **Não respondida.** A exceção é reconhecida por câmaras do TJBA e por ato do CNJ, não pelo STJ; o Tema 876 continua firmado em lei federal (LEF, art. 6º) e o material não traz decisão do STJ que admita a distinção.
- **CQ2 (proponente):** há prova de que a regra não se aplica? Respondida em parte: o Tema 876 decidiu a prevalência da LEF sobre o art. 15 da Lei 11.419/06; as decisões de 2026 apoiam a distinção na eficiência (Temas 1.184 e 1.428 do STF) e na Consulta CNJ. O Tema 1.428 está pendente, sem tese, e discute se os parâmetros da Resolução CNJ 547/2024 podem prevalecer quando a lei local fixa critérios diversos: é risco em aberto para a própria base normativa da distinção, não apoio firmado (alcance: MIJ).
- **CQ3 (proponente):** há casos comparáveis? Respondida: Primeira a Quarta Câmaras em 2025-2026 (lista acima).
- **Status do motor:** `WEAK_UNANSWERED_CQ` (CQ1 pendente; respostas de origem LLM, a conferir).
- **Contra-analogia:** a do endereço (8016313-04.2022), em que a LEF dispensa o dado "sempre que conhecido"; o Município dirá que o CPF segue a mesma lógica.

## 7. Limites e o que falta

- Só ementas e inícios de relatório; inteiro teor não lido.
- DJEN zero para a frase; DJEN cobre só desde cerca de 2024; API subconta; 1º grau ausente.
- A Resolução CNJ 547/2024 e a Resolução 617/2025, a Consulta CNJ e o Tema 1.428 não foram lidos.
- A linha do endereço do catálogo é toda de 2020; a de 2025 (8016313-04.2022) aponta o contrário. Não há como dizer, pelo material, qual prevalece hoje.
- Sobreposição: parte da API mistura CPF e baixo valor (Tema 1.184), matéria da TES-03, excluída da lista; 8003697-83.2025 ficou porque a ementa nomeia o CPF.
- Um item da amostra (8113000-86.2021) é de espólio e está no catálogo da TES-13; não foi usado aqui.

## 8. Utilidade prática

- **Usar** em contrarrazões a recurso do Município contra sentença que extinguiu por falta de CPF após emenda não atendida, citando as câmaras de 2026.
- **Não usar** para pedir indeferimento de plano por falta de endereço: a LEF só o exige quando conhecido.
- **Risco:** a distinção ainda não passou pelo STJ; REsp do Município fundado no Tema 876 é previsível. Ganho prático limitado: o crédito não se extingue e pode ser reajuizado com o CPF, se não prescrito.

**Revisão pós-Codex (06/11/2026).** Item 3 do Codex, JSON: a chave `n_acervo_fav_indicio` passou a `n_acervo_fav` (53); `n_acervo` = 87 (total) sem mudança. Item 9 do Codex, formulação do MD: 'passou a afastar por distinção desde 2025-2026' → 7 decisões de 2025-2026 na linha b do § 3, 1 delas do catálogo, sem denominador (a formulação do JSON não tinha a frase). Registro: `auditoria/correcoes-pos-codex-e43.jsonl`; originais em `estado/E4-3/antes-pos-codex/`.
