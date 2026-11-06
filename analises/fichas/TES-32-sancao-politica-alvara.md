---
tipo: ficha-de-tese
data: 2026-11-06
produzido-por: claude-code (leitor Opus E4-3)
versao-core: 1.0
status: draft
tese: 32
---

# TES-32 · Sanção política: alvará condicionado à quitação do IPTU

## 1. Formulação

Se o Município condiciona a expedição de alvará (de construção, reforma ou funcionamento), de guia de ITIV ou de certidão à quitação de débitos de IPTU, então a exigência é sanção política vedada (Súmulas 70, 323 e 547 do STF) e o contribuinte obtém o ato independentemente do pagamento.

## 2. Fundamento normativo

- **Súmulas 70, 323 e 547 do STF:** invocadas em 0510899-26.2016 e 8031036-03.2023; 8009256-87.2023 invoca só a Súmula 323; a sentença transcrita em 8065174-98.2020 invoca as três.
- **Lei Municipal nº 7.186/2006 (Salvador), art. 323, parágrafo único:** a norma que condiciona o alvará à regularidade tributária. Foi afastada em 8029958-13.2019.8.05.0001.
- **STJ, Tema 1113** (base de cálculo do ITBI/ITIV): cumulado em 8031036-03.2023. É tangencial à tese.
- O fundamento constitucional (livre exercício de atividade, devido processo) não está transcrito nos excertos; consta da ADI 173 (PANGEA).

## 3. Como o TJBA decide

**Números.**

- Catálogo: 1 processo favorável. Acervo 2020–2026: 9 processos (9 decisões) com a palavra, 1 com indício favorável (recorte por palavra; indício, não taxa).
- **O recorte subestimou muito.** Os 8 processos restantes estão todos na amostra (8): 4 favoráveis claros, 1 favorável em que o apelo do Município (só sobre honorários) foi desprovido (8065174) e 3 ruídos.
- A API do TJBA devolveu **0** para `IPTU AND "sanção política"`, embora o acervo tenha a expressão: prova de que a API subconta.
- `n_catalogo_fav` fica em 1; os demais são indício adicional.

**Câmaras e período.** Primeira, Segunda, Terceira (2 processos, mais o do catálogo) e Quinta Câmaras Cíveis; de 03/11/2020 a 09/07/2026. Metade (3 de 6: 8029958, 8009256, 8031036) é **remessa necessária** em mandado de segurança, com a sentença concessiva confirmada; os outros são apelação em mandado de segurança (0510899), agravo contra liminar em mandado de segurança (8028759) e apelação em ação ordinária (8065174).

**A regra dos casos favoráveis.** Condicionar ato administrativo à quitação de IPTU é meio indireto de cobrança e configura sanção política.

- **Alvará de construção.** 0510899-26.2016.8.05.0001, Terceira Câmara, 03/11/2020: «Entendimento adotado pelo Supremo Tribunal Federal, expresso pelas Súmulas 70, 323 e 547, todas no sentido de não admitir que o Poder Público atrele o exercício de direitos ao prévio pagamento de tributos»
- **Alvará de funcionamento em Salvador, com lei municipal afastada.**
  - 8029958-13.2019.8.05.0001, Quinta Câmara, 18/10/2023, remessa necessária: no caso, «o Município de Salvador, fundamentado no parágrafo único do art. 323 da Lei Municipal nº 7.186/2006, que condiciona a expedição de alvará de licença a regularidade tributária,» negou o alvará.
  - A Câmara: «A negativa de expedição do Alvará requerido, se mostra, em verdade, atitude que objetiva forçar a presença do contribuinte inadimplente na repartição tributária para coagi-lo a, por meio transverso, providenciar o pagamento dos tributos devidos.»
- **Alvará de construção e reforma em Camaçari.** 8009256-87.2023.8.05.0039, Segunda Câmara, 20/08/2024: «EXIGÊNCIA DE COMPROVAÇÃO DE REGULARIDADE FISCAL DE IPTU. CONDICIONAMENTO INDEVIDO. SÚMULA 323 DO SUPREMO TRIBUNAL FEDERAL. MEIO COERCITIVO DE COBRANÇA. JURISPRUDÊNCIA DO TEMA. SENTENÇA CONFIRMADA.»
- **Guia de ITIV.**
  - 8031036-03.2023.8.05.0001, Terceira Câmara, 17/07/2025: «A exigência de pagamento de IPTU como condição para a emissão da guia de ITIV configura sanção política vedada pelo STF»
  - 8028759-46.2025.8.05.0000, Terceira Câmara, 09/07/2026, agravo do Município desprovido: «EMISSÃO DE GUIA DE RECOLHIMENTO DE IMPOSTO DE TRANSMISSÃO INTER VIVOS (ITIV) CONDICIONADA À QUITAÇÃO DE DÉBITOS PRETÉRITOS DE IMPOSTO PREDIAL E TERRITORIAL URBANO (IPTU) E TAXA DE RESÍDUOS SÓLIDOS DOMICILIARES (TRSD). SANÇÃO POLÍTICA CONFIGURADA.»
- **Certidão de não incidência de ITIV.** 8065174-98.2020.8.05.0001, Primeira Câmara, 04/02/2022: o relatório transcreve a sentença: «é defeso à administração impedir ou cercear a atividade do contribuinte, para compeli-lo ao pagamento de débito». O trecho do pacote não traz o resultado, mas o acórdão da mesma data no acervo (DEC-TJBA-15139248e0cd) decide «conhecer e negar provimento ao apelo, mantendo a sentença». O apelo do Município só pedia a redução dos honorários: o mérito (sanção política) ficou na sentença, sem revisão pela Câmara.

**Contrárias.** Nenhuma no pacote: DJEN com 0 retornos, API com 0, e nenhuma na amostra.

**Ruído e neutros.**

- 0046737-82.2019.8.05.0001: consumo.
- 8015177-76.2025.8.05.0000: alvará **judicial** em inventário.
- 8015030-26.2020.8.05.0000: admissibilidade de REsp sobre protesto de CDA com execução garantida, outra tese: «O ato do Agravante de promover o protesto do mesmo título, objeto de ação executiva, caracteriza-se como bis in idem»

## 4. Precedentes qualificados do STJ e do STF

- **STF, Súmula 70** (Cognitio `STF:sumulas:70`, conferida): "É inadmissível a interdição de estabelecimento como meio coercitivo para cobrança de tributo."
- **STF, Súmula 323** (Cognitio `STF:sumulas:323`, conferida): "É inadmissível a apreensão de mercadorias como meio coercitivo para pagamento de tributos."
- **STF, Súmula 547** (Cognitio `STF:sumulas:547`, conferida): "Não é lícito à autoridade proibir que o contribuinte em débito adquira estampilhas, despache mercadorias nas alfândegas e exerça suas atividades profissionais."
- **STF, Tema 31 de Repercussão Geral** (PANGEA `stf-rg-31`; leading case transitado em julgado). Tese no registro (íntegra): "É inconstitucional o uso de meio indireto coercitivo para pagamento de tributo – “sanção política” –, tal qual ocorre com a exigência, pela Administração Tributária, de fiança, garantia real ou fidejussória como condição para impressão de notas fiscais de contribuintes com débitos tributários." Leading case conferido: RE 565.048/RS, Plenário, rel. Min. Marco Aurélio, 29/05/2014, unânime (Cognitio `STF:paradigmas-teor:31-6911989`, teor): «Discrepa, a mais não poder, da Carta Federal a sanção política objetivando a cobrança de tributos – Verbetes nº 70, 323 e 547 da Súmula do Supremo.» O caso era a exigência de fiança, garantia real ou fidejussória para imprimir notas fiscais (ICMS, Lei 8.820/89 do RS).
- **STF, ADI 173** (PANGEA `stf-adi-173`): normas que condicionam atos da vida civil e empresarial à quitação de tributos caracterizam sanção política. Só a ementa do registro (PANGEA; também no Cognitio `STF:pangea:stf-adi-173`); o inteiro teor não está no Cognitio (Basanos: fora do índice). A ementa confere e traz o fundamento constitucional, item 3: «invocando, para tanto, o direito ao exercício de atividades econômicas e profissionais lícitas (art. 170, par. ún., da Constituição), a violação do devido processo legal substantivo [...]».
- **STF, ADI 3952** (PANGEA `stf-adi-3952`): é o **contra-caso**. Admite o cancelamento de registro especial de devedor contumaz, com proporcionalidade e devido processo. Inteiro teor não localizado no Cognitio (Basanos: fora do índice); a ementa do registro PANGEA confere com o que a ficha diz.

## 5. Via processual

- **Mandado de segurança.** É a via de 5 dos 6 favoráveis (3 remessas necessárias, 1 apelação e 1 agravo contra liminar, todos em mandado de segurança); o sexto (8065174) é apelação em ação ordinária.
- **Prova pré-constituída:** requerimento do alvará, da guia ou da certidão; ato ou documento de negativa que mostre que a razão é o débito de IPTU; certidão ou extrato do débito.
- **Ação ordinária com tutela** (8065174-98.2020), quando a prova da motivação não é documental.
- **Defesa do Município a antecipar:**
  - lei municipal que condiciona o ato (8029958 afastou);
  - débito vinculado ao próprio imóvel no ITIV (8028759 e 8031036 afastaram);
  - ilegitimidade do credor fiduciário (rejeitada em 8028759).

## 6. Walton e Élenchos

**Argumento determinante (analogia):**

- **C1:** apreensão de mercadorias, interdição de estabelecimento e proibição de atividade como meio coercitivo de cobrança são vedadas (Súmulas 323, 70 e 547).
- **C2:** negar alvará, guia de ITIV ou certidão por débito de IPTU.
- C2 é semelhante a C1 no traço decisivo: o meio indireto de forçar o pagamento, fora da execução fiscal. Logo, C2 também é vedado.

**Esquema:** `ARG.SCH.WRM08.ANALOGY` (WRM2008, p. 315).

| CQ | Pergunta | Ônus | Ataque | Resposta no material |
|---|---|---|---|---|
| CQ1 | Há diferenças entre C1 e C2 que enfraquecem a semelhança? | questionador | undermine (semelhança) | **Respondida.** O Município alegou lei municipal expressa (8029958) e o vínculo do débito com o imóvel transmitido (8028759, 8031036); o TJBA rejeitou as duas diferenças. |
| CQ2 | A conclusão vale em C1? | proponente | undermine (premissa-base) | **Respondida.** Súmulas 70, 323 e 547 conferidas no Cognitio; Tema 31 de RG e ADI 173 no PANGEA. |
| CQ3 | Há caso C3, semelhante a C1, em que a conclusão não vale? | questionador | undercut | **Respondida.** ADI 3952 admite restrição ao devedor contumaz, mas com apuração do montante, devido processo e inadimplência preordenada. O débito comum de IPTU que trava um alvará não preenche esses requisitos. |

**Status devolvido pelo motor:** `PLAUSIBLE`, com todas as CQs respondidas. Respostas de origem LLM, a conferir.

**Contra-analogia.** O ponto de fuga é a ADI 3952 (na mesma linha, a ADI 4854, PANGEA: «A submissão de contribuintes inadimplentes a regime fiscal diferenciado, sem inviabilizar o exercício da atividade econômica, não configura sanção política ou meio oblíquo de cobrança»): se o Município provar inadimplência contumaz e estruturada, com procedimento próprio, a analogia enfraquece. Para IPTU residencial ou de pequeno empreendedor, não há sinal disso no material.

## 7. Limites e o que falta

- **Só ementa.** Do TJBA, o pacote traz ementa ou excerto curto; o inteiro teor dos acórdãos não foi lido. Resultado e fundamento foram inferidos do que a ementa diz.
- **DJEN desde cerca de 2024.** As publicações por frase cobrem só o período recente; os acórdãos aparecem só com ementa.
- **API do TJBA subconta e não é neutra.** A busca livre do portal (`tjba_api`) devolve poucos itens e muito ruído; não serve de denominador.
- **1º grau ausente.** Sentenças só aparecem quando publicadas no DJEN; não há base de 1º grau.
- **Lei municipal não lida.** Os artigos de lei municipal citados vêm das ementas; o texto das leis não foi conferido (vigência, redação, alterações).
- **Indício, não taxa.** Os números do acervo vêm de recorte por palavra na ementa; não medem a proporção de vitórias.
- O catálogo tem 1 processo; os demais favoráveis vêm da amostra do acervo (só ementa) e não foram catalogados nem conferidos pelo validador.
- O universo é pequeno (9 processos no recorte); não há contrária no pacote, o que pode refletir a busca e não a ausência no Tribunal.
- Os acórdãos do STF (RG 31, ADI 173, ADI 3952) não foram abertos no Cognitio.

## 8. Utilidade prática

- **Quando usar.** Negativa ou demora de alvará de construção, reforma ou funcionamento, de guia de ITIV (inclusive arrematação e alienação judicial) ou de certidão, motivada **apenas** por débito de IPTU ou TRSD.
- **Quando não usar.**
  - A negativa tem outra causa (urbanística, documental).
  - O pedido, na verdade, é para afastar a responsabilidade pelo débito em si (outra tese: sujeição passiva).
- **Risco.** Baixo no TJBA, pela convergência das câmaras e das súmulas do STF. O cuidado está na prova pré-constituída de que a única razão da negativa é o débito.

**Revisão pós-Codex (06/11/2026).** Item 3 do Codex, JSON: acrescentado `n_acervo_fav` = 1; `n_acervo` = 9 (total) sem mudança. Item 9 do Codex, 'via dominante' → 5 de 6 em mandado de segurança. Registro: `auditoria/correcoes-pos-codex-e43.jsonl`; originais em `estado/E4-3/antes-pos-codex/`.
