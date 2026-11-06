---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
lote: F4F5 (lançamento; incidência e território)
alvo: analises/fichas/TES-27, TES-31, TES-19, TES-29, TES-30 (.md e .json, draft de 06/11/2026)
pacotes: estado/E4-3/pacote-F4_lancamento.json (27, 31); estado/E4-3/pacote-F5_incidencia_territorio.json (19, 29, 30)
destino-do-alvo: interno (pesquisa; nada a renderizar nem enviar)
metodo: conferência manual de cada afirmação contra a fonte própria (pacote, JSON da ficha, face das ementas em derivados/ementas-candidatos.jsonl, Cognitio, Planalto); não o pipeline `conferidor` (destino interno, formato do precedente TES-001)
saida-por-codigo: auditoria/antialucinacao-E43-F4F5.json (47 itens; cada `de` conferido por código como substring única da ficha)
---

# Antialucinação: lote F4F5 da E4-3

## 1. Veredito por ficha

| Ficha | Pior gravidade | [A CONFERIR] resolvidos | Veredito |
|---|---|---|---|
| TES-27 notificação do lançamento | **médio** (2) | 3 de 4 | Nada inventado. Mas a ficha toma o rótulo "2ª Vice-Presidência" do banco como se fosse o órgão. Daí conclui que duas das três favoráveis são admissibilidade e que "o único favorável de câmara com mérito" é 8097112. Na face do texto, 0323034 e 8011756 são acórdãos de mérito da **Terceira Câmara**. A tese sai **mais forte** do que a ficha diz. |
| TES-31 revisão de ofício (erro de direito) | **médio** (3) | 1 de 2 | Mesma armadilha: 0848075 é acórdão da Terceira Câmara em **mandado de segurança**, e a 2ª VP negou seguimento ao REsp do Município **pelo Tema 387**. Por isso o `[A CONFERIR]` do MS "diverge": há caso no material. As citações do REsp 1.130.545 (itens 2, 6 e 7 e a doutrina) conferem no teor. |
| TES-19 zona rural ou urbana | **médio** (3) | 3 de 3 | Mesma armadilha em 0505955, que é acórdão da Primeira Câmara, e em 8002511, que é da Quinta Câmara. Na prova, "falta de pelo menos dois melhoramentos" inverte a regra do art. 32, § 1º. A Súmula 473 também aparece numa favorável (8010153). Contagens, bloco Pojuca e precedentes conferem. |
| TES-29 bitributação entre municípios | leve | 3 de 5 | Sem erro. Contagens (13; câmaras 2/1/2/6/2), datas, duplicatas e a contrária 8077091 conferem; a ficha já tinha corrigido o rótulo 2ª VP desta. Ressalvas: a área nem sempre é nomeada, e a Lei 2.713 aparece com ano divergente nos textos do TJBA. MS 439 e Lei 2.713 ficam como limite. |
| TES-30 APP não edificável | leve | 3 de 4 | Sem erro de fato. Os precedentes do STJ conferem no teor. Os casos do TJBA são de **APA/ZPAM**, não de APP. Os limites de 0030481 se resolvem pela ementa (APA Lagoas e Dunas do Abaeté). O STJ não decidiu a prova no AREsp 2.594.742. STF: não localizado. |

**Nada grave no lote.** Não há citação inexistente, aspas falsas nem número que mude a conclusão. Os excertos do TJBA já tinham sido conferidos por código (602/602). Refiz por código a busca dos 72 excertos das cinco fichas na face do texto (ementas do laboratório e itens do pacote): 72/72. O Basanos confirmou nos índices todas as citações superiores das fichas. O único `fora_do_indice`, REsp 1.695.340/MG, é citação do **TJBA** dentro da ementa de 0555629 (texto alheio: divergência a investigar, não erro da ficha).

**Padrão do lote (médio, três fichas).** É o mesmo achado do TES-16 no F1b. O banco grava `orgaoJulgador = 2ª VICE-PRESIDÊNCIA` para acórdãos de câmara. As fichas 27, 31 e 19 leram o rótulo como admissibilidade e rebaixaram os casos. A face do texto desmente em todos os quatro processos: 0323034, 8011756, 0848075 e 0505955 (8002511 é da Quinta Câmara). Nos quatro que têm decisão da 2ª VP no laboratório (0323034, 0848075, 0505955 e 8002511; só 8011756 não tem), ela é posterior e **inadmitiu ou negou seguimento ao REsp do Município**. O desfecho é sempre favorável ao contribuinte.

## 2. Afirmações problemáticas

### TES-27

**A-01: órgão e natureza das duas favoráveis "da 2ª Vice-Presidência".** **MÉDIO**, erro de fato (atribuição errada de órgão; contradição objetiva).
- Ficha, § 3: "**Atenção: as duas decisões da 2ª Vice-Presidência são juízo de admissibilidade de recurso especial ou extraordinário,** não julgamento de mérito. [...] O único favorável de câmara com mérito no catálogo é 8097112-77.2021.8.05.0001." Também "Câmaras e período" e § 7.
- Fonte: `derivados/ementas-candidatos.jsonl`.
  - DEC-TJBA-36064e1db420 (0323034): «Órgão Julgador: Terceira Câmara Cível» e «ACORDAM os magistrados integrantes da Terceira Câmara Cível do Estado da Bahia, em DAR PROVIMENTO ao apelo».
  - DEC-TJBA-8bccbd753cef (8011756): «ACORDAM os Desembargadores componentes da Terceira Câmara Cível do Tribunal de Justiça do Estado da Bahia, em NEGAR PROVIMENTO AO RECURSO», «Salvador/BA, 10 de dezembro de 2023». No pacote F5, o mesmo acórdão já consta com órgão Terceira Câmara (DEC-TJBA-6d3445652882); a TES-19 o rotula certo.
- Desdobramentos favoráveis que a ficha não registra:
  - em 0323034, a 2ª VP **inadmitiu** o REsp do Município (DEC-TJBA-48040539f9b3, 18/11/2024; Súmulas 282 e 356/STF; arts. 145, III, e 149 do CTN não prequestionados);
  - em 8011756, a Terceira Câmara rejeitou os embargos do Município (DEC-TJBA-78168ea199b7, 02/05/2024): «São nulos os lançamentos de tributação do IPTU, quando o imóvel teve seu cadastro alterado de rural para urbano, sem a prévia notificação do proprietário.»
- Por que médio: a conclusão de risco melhora (três acórdãos de câmara, não um), mas a tese não muda.

**A-02: contraditório, CF art. 5º, LV `[A CONFERIR]`.** Leve, resolvido. O inciso não está em 0323034, mas está em 8165454 (item 7): «em violação ao art. 5º, LV, da CF/1988 e ao devido processo legal». Texto do inciso conferido no Planalto.

**A-03: zona urbana `[A CONFERIR]`.** Leve, resolvido em parte. O CTN, art. 32, confere (Cognitio, Planalto). A ementa de 8011756 funda-se no contraditório («por afronta ao direito ao contraditório e ampla defesa da Contribuinte»), não no art. 32. A lei municipal de Camaçari continua não lida. A ementa ainda traz o apelante como Camaçari no cabeçalho e Lauro de Freitas no "Vistos" (divergência interna do TJBA, sem efeito na ficha).

**A-04: Tema 116, "cabendo-lhe comprovar".** Leve, ressalva (alcance de tese: `mij`).
- A frase está no campo "ementa" do cadastro `STJ:paradigmas:Tema-116`, que é a **questão submetida** («Questão referente à notificação do contribuinte...»), não a tese firmada. A TES-31 fez essa distinção para o Tema 387; aqui não.
- O ônus do contribuinte tem apoio no teor do REsp 1.111.124: o acórdão do TJPR que foi mantido dizia caber «ao contribuinte elidir a presunção de certeza e liquidez do título». Mas não é texto da tese.

**A-05: REsp 1.933.514 `[A CONFERIR]`.** Leve, resolvido. Cognitio `STJ:integras:138564640`: AgInt no REsp, Segunda Turma, Rel. Min. Herman Benjamin, publicado em 04/11/2021, recurso especial **não conhecido** (barreiras: Súmula 7/STJ e Súmula 280/STF). Na origem (TJSP, Campinas), lançamento retroativo, feito por edital, por alteração de zoneamento, com «Cientificação do lançamento induvidosa, malgrado o disposto na Súmula 397 do STJ». A ementa do STJ (face, cabeçalho) registra: «SÚMULA 7 DO STJ. INCIDÊNCIA. [...] SÚMULA 280 DO STF. INCIDÊNCIA. ÔNUS DA PROVA DO RECEBIMENTO DO CARNÊ DO IPTU. CONTRIBUINTE. AUSÊNCIA DE COMPROVAÇÃO.» Não é precedente; é **sinal contrário**, a registrar ao lado do Tema 116, inclusive para lançamento retroativo.

**A-06: 8031040 é cognição sumária.** Leve, ressalva. É agravo de instrumento em embargos à execução: «PREENCHIMENTO DOS REQUISITOS AUTORIZADORES DA MEDIDA LIMINAR. AGRAVO CONHECIDO E PROVIDO.» A leitura da ficha (Súmula 397 aplicada ao carnê anual; vitória só na citação) confere com a ementa.

**Conferido sem problema.** Contagens (4 no catálogo, 3 favoráveis por questão e 1 contrária; acervo 698/787/146; DJEN 0; API 0) batem com o pacote e com o JSON. Súmulas 397 e 414 conferem no texto. Tema 116 / REsp 1.111.124/PR confere: Primeira Seção, Teori Albino Zavascki, 22/04/2009. O REsp 1.130.545, item 2, confere literalmente. O AREsp 2.757.364 confere: Segunda Turma, publicado em 25/08/2025, Súmula 284/STF, Belo Horizonte; a citação da "ciência inequívoca [...] via parcelamento" é literal. 8165454 e 8097112 conferem com a ementa. A classificação da amostra está certa (prescrição, possessórias, consumo, CODEBA).

### TES-31

**A-07: 0848075 "decisão da 2ª Vice-Presidência, [...] juízo de admissibilidade".** **MÉDIO**, erro de fato.
- Fonte: DEC-TJBA-39b3c01e0412, «Órgão Julgador: Terceira Câmara Cível», «APELAÇÃO CÍVEL em Mandado de Segurança 0848075-63.2016.8.05.0001», «ACORDAM os Desembargadores integrantes da Terceira Câmara Cível [...] em NEGAR PROVIMENTO À APELAÇÃO», «Salvador, 26 de junho de 2023».
- A decisão da 2ª VP é outra: DEC-TJBA-69c2b7f003d0, de 25/10/2023. Ela negou seguimento ao REsp do Município **com base no Tema 387**, dizendo o acórdão «em perfeita sintonia com a jurisprudência do Superior Tribunal de Justiça» (art. 1.030, I, "b", do CPC).
- É o sinal mais forte da ficha, e ela o perdeu: o próprio TJBA, ao filtrar o REsp, disse que o reenquadramento de padrão construtivo com dados já conhecidos é erro de direito **conforme** o Tema 387.

**A-08: § 5, mandado de segurança, "não há caso no material" `[A CONFERIR]`.** **MÉDIO**, resolvido: **diverge**. 0848075 é mandado de segurança contra revisão de ofício por «MODIFICAÇÃO DO PADRÃO CONSTRUTIVO», com segurança mantida.

**A-09: § 4, "o texto do PANGEA [...] traz a questão submetida, não a tese".** Leve, erro. No pacote, `stj-rr-387.texto` traz a questão **e**, logo depois, a tese ("A retificação de dados cadastrais do imóvel, após a constituição do crédito tributário, autoriza a revisão..."). Só o campo "ementa" do cadastro Cognitio é a questão.

**A-10: 0099207.** Leve, duas ressalvas.
- O "novo critério vale para fatos futuros" está na própria ementa (item 6), não só na tese resumida.
- O trecho citado no § 3 é a Quinta Câmara resumindo o REsp 1.130.545 (voz atribuída). O caso não é de reenquadramento: é diferença de IPTU de 1991, em que o Fisco revisou o lançamento por ter aplicado fator de correção de lei revogada (itens 2 e 3).

**A-11: rótulos e contexto.** Todos leves.
- 8031671 é «Tribunal Pleno» na face; "Órgão Especial" é o rótulo do banco.
- Em 0506118, a decisão de 19/12/2025 rejeita embargos; o «deu provimento» descreve o acórdão embargado.
- No § 5, "8036428 é agravo nesse contexto" afirma tutela, mas o § 3 da própria ficha diz que a ementa não revela a origem.

**A-12: Súmula 227/TFR `[A CONFERIR]`.** Não localizada em fonte própria. O Cognitio não tem TFR; as "Súmula 227" do STF e do STJ são outras (concordata; dano moral de pessoa jurídica). A transcrição no teor do REsp 1.130.545 (item 7) confere literalmente. O limite declarado pela ficha está correto.

**Conferido sem problema.** Tema 387 / REsp 1.130.545/RJ confere: Primeira Seção, Luiz Fux, julgado em 09/08/2010, DJe 22/02/2011, unânime, provimento ao Município. A tese confere literalmente, e os itens 6 e 7 e "sutil, mas incisiva" (Paulo de Barros Carvalho) estão no teor. O AREsp 2.995.053 confere: Segunda Turma, publicado em 28/10/2025, não conhecido pela Súmula 7, Porto Alegre, citação literal. As contagens batem (2 no catálogo; 41/50/8; mais 3 favoráveis fora do catálogo; API 5 brutos e 3 no pacote; DJEN 1, de Teixeira de Freitas). 8043120 e 8036428 batem com a API. "Concentração em Salvador" confere (os cinco favoráveis são de Salvador).

### TES-19

**A-13: 0505955 "2ª Vice-Presidência [...] Órgão de admissibilidade [...] pede o inteiro teor".** **MÉDIO**, erro de fato.
- Fonte: DEC-TJBA-399ea58540e0, Primeira Câmara Cível: «à unanimidade de votos, em conhecer e negar provimento ao recurso de apelação, mantendo a sentença». Município de Camaçari apelante; laudo pericial de atividade agrícola, pecuária e extração vegetal, sem os equipamentos do art. 32 do CTN.
- O REsp do Município foi inadmitido pela 2ª VP em 02/05/2024 (DEC-TJBA-4ecc7ec6badc).
- O limite do § 7 se resolve pela ementa.

**A-14: 8002511 e "Câmaras e período".** **MÉDIO** no quadro de câmaras, leve no item.
- 8002511 (DEC-TJBA-611f09ba5dbe) é «ACORDAM os Desembargadores integrantes da 5ª Câmara Cível», em agravo do Município contra liminar em mandado de segurança. A 2ª VP inadmitiu o REsp em 25/05/2023 (DEC-TJBA-2f87f7952e32, Súmula 7).
- Logo, a Quinta Câmara já está no catálogo, e não só "pela API, em 2026".

**A-15: § 5, prova, "falta de pelo menos dois melhoramentos do art. 32, § 1º".** **MÉDIO**, erro objetivo de direito que não muda a tese.
- O CTN, art. 32, § 1º (Planalto, via Cognitio) exige melhoramentos "em pelo menos 2 (dois) dos incisos" para haver zona urbana. 0570624 (item 3) diz o mesmo: «deve possuir, no mínimo, dois melhoramentos públicos».
- O contribuinte tem de provar que existe **no máximo um** melhoramento, ou seja, que faltam ao menos quatro dos cinco. Faltarem dois ainda deixa três, e o imóvel é urbano.

**A-16: Súmula 473 `[A CONFERIR]` (§ 2 e § 4).** Leve, resolvido.
- Texto conferido (Cognitio `STF:sumulas:473`).
- A súmula não é só da contrária 8055247. Está também na contrária 8052650 («AUTOTUTELA ADMINISTRATIVA. SÚMULA 473/STF.») e na **favorável** 8010153 («SÚMULA Nº 473 – STF»), que acolheu a exceção contra a reativação sem contraditório. A súmula ressalva «os direitos adquiridos».

**A-17: CF, art. 5º, LV `[A CONFERIR]`.** Leve, resolvido (Planalto). Nenhum excerto o cita.

**A-18: art. 15 do DL 57/1966.** Leve, ressalva (alcance: `mij`).
- O Planalto traz "exploração extrativa vegetal, agrícola, pecuária ou agro-industrial", sem vírgula entre "extrativa" e "vegetal". A ficha escreve "extrativa, vegetal", que é a pontuação da ementa do Tema 174.
- A diferença importa para a "lista fechada": na letra da lei, extração mineral ou de petróleo não está na lista. 0501145 (Petrobras, «EXTRAÇÃO DE PETRÓLEO E GÁS») venceu pela localização rural, INCRA e ITR.
- Vigência anotada no Planalto: "Revogado pela Lei nº 5.868, de 1972" e "Revogação suspensa pela RSF nº 9, de 2005".

**A-19: bloco Pojuca.** Leve, ressalva. 8010153 (Primeira Câmara, 03/04/2023) já é Petrobras × Pojuca, com baixa e reativação sem contraditório. O bloco começa antes de 2025.

**A-20: 8058846.** Leve, ressalva. A ementa diz «IMÓVEL APARENTEMENTE NÃO ABARCADO POR MELHORAMENTOS URBANOS. IMPOSSIBILIDADE, A PRINCÍPIO»: é cognição sumária, não "área rural sem serviços públicos" assentada.

**Conferido sem problema.** Contagens: 12 no catálogo (11 favoráveis e 1 parcial); 8030609 reformado em embargos; restam 11; acervo 1.067/1.203/140; API 19 brutos e 6 no pacote; DJEN 0. A amostra é toda ruído (8/8). O bloco Pojuca confere: cinco agravos, IPTU de 2012 a 2016, baixa em 2019 e reativação em 2020. Os resultados conferem (8052713 e 8052434 favoráveis; 8054777 favorável pelo procedimento; 8052650 e 8055247 contrárias), e a Segunda Câmara decidiu nos dois sentidos em 48 dias. 8030609 confere (acórdão de 29/04/2024; ED rejeitados em 04/09/2024; ED do Município acolhidos em 18/12/2024).

Precedentes:
- Tema 174 / REsp 1.112.646/SP: Primeira Seção, Herman Benjamin, 26/08/2009; ementa literal.
- Súmula 626: texto literal.
- Tema 138 / RE 594.296/MG: Plenário, Dias Toffoli; tese literal; o acórdão é datado "Brasília, 21 de setembro de 2011".
- AgInt no REsp 2.090.749: Segunda Turma, publicado em 18/12/2023; a citação «não se desincumbiu do ônus probandi» é literal.

### TES-29

**A-21: "Todos os 13 processos tratam da mesma área: o Loteamento Marisol".** Leve, ressalva.
- Onze ementas nomeiam Marisol.
- 8008800 diz Ipitanga e «Loteamento Marissol I e II» (ao relatar o MS 439).
- 8013249 não nomeia a área.

**A-22: MS 439 `[A CONFERIR]`.** Limite confirmado. A ficha pode dizer mais:
- 8008800 diz que o MS foi «impetrando em 2015» e reconheceu a competência de Salvador sobre «a região de Ipitanga, especialmente, o Loteamento Marissol I e II»;
- 8013249: «DIVERGÊNCIA QUANTO AO MUNICÍPIO COMPETENTE SANADA PELO MANDADO DE SEGURANÇA Nº 439».
- Tribunal, partes e trânsito em julgado dependem do inteiro teor.

**A-23: Lei Estadual 2.713.** Leve, ressalva. Os próprios textos do TJBA divergem: 8012160 escreve «Lei nº. 2.713/62»; 8005873 e 8023542, «2.713/1969». A lei não foi localizada em fonte primária nesta conferência.

**A-24: 8015906 sob "MS 439".** Leve, ressalva. A ementa liga o marco de 2015 à «nova inscrição imobiliária pela prefeitura» e a «PRÉVIO RECONHECIMENTO JUDICIAL», sem nomear o MS 439.

**A-25: `[A CONFERIR]` normativos.** Leves, resolvidos.
- CF, art. 156, I, e CTN, art. 32: conferidos no Planalto. As ementas citam, em vez deles, o CTN, art. 7º (8023542) e os arts. 11, XVI, e 70, IV, da Constituição da Bahia (8012160).
- CTN, art. 164, III, e § 2º: conferidos.
- Súmula 280/STF: «Por ofensa a direito local não cabe recurso extraordinário.»

**Conferido sem problema.** Os 13 do catálogo conferem, todos favoráveis, por câmara: Primeira 2, Segunda 1, Terceira 2, Quarta 6, Quinta 2. Período de 06/03/2024 a 24/01/2025. Acervo 56/63/34; DJEN 4 brutos e 2 no pacote (um de TFF); API 0. As duplicatas conferidas são processos distintos. 8077091 é acórdão da Segunda Câmara («Conforme entendimento consolidado pelo TJBA»), e a ficha já o corrigiu. 8009354 confere: perícia, sentença desconstituída. 8044820 confere: suspensão pedida pelo próprio exequente. 8036679 confere (Seções Cíveis Reunidas, 15/08/2022), e o DJEN 8241501 também. O Tema 421 confere: REsp 1.185.036, Herman Benjamin, tese literal. A Quarta Câmara tem 6 favoráveis de 09/04 a 19/11/2024.

### TES-30

**A-26: Código Florestal, art. 4º, "define as APPs" `[A CONFERIR]`.** Leve, resolvido.
- No Planalto, o art. 3º, II, **define** APP e o art. 4º a **delimita** ("Considera-se Área de Preservação Permanente, em zonas rurais ou urbanas, para os efeitos desta Lei:").
- Os casos do TJBA não são de APP: 0030481 é «APA LAGOAS E DUNAS DO ABAETÉ», e em 0555629 a Prefeitura atestou «ÁREA DE PRESERVAÇÃO AMBIENTAL (APA)» (ZPAM). Só os casos do STJ tratam de APP. A analogia funciona, mas a ficha deve dizer qual regime está em cada caso.

**A-27: AREsp 2.594.742 `[A CONFERIR]`.** Leve, resolvido.
- Cognitio `STJ:integras:329917838`: AgInt no AREsp, Segunda Turma, Rel. Min. Marco Aurélio Bellizze, publicado em 19/08/2025; não conhecido pelas Súmulas 283 e 284/STF (razões dissociadas).
- Ficou de pé o acórdão do TJSP que rejeitou a exceção por «Necessidade de produção de provas». O STJ não "manteve" por juízo próprio sobre a prova.

**A-28: CPC, art. 300 `[A CONFERIR]`.** Leve, resolvido (Planalto, via Cognitio). A ementa só diz «TUTELA PROVISÓRIA DE URGÊNCIA».

**A-29: STF `[A CONFERIR]`.** Não localizado. A busca no Cognitio só deu resultados exploratórios (Código Florestal, demolição em APP). Ausência no acervo não é ausência no ordenamento.

**A-30: 0030481, limite do § 7.** Leve. A ementa já diz «ÁREA NÃO EDIFICÁVEL. APA LAGOAS E DUNAS DO ABAETÉ. RESTRIÇÃO ABSOLUTA IMPOSTA AO BEM.»: a restrição é legal. Falta só a extensão sobre o imóvel.

**A-31: 0555629, precedente do STJ citado pelo TJBA.** Leve, ressalva (texto alheio).
- A ementa invoca o REsp 1.695.340/MG (Segunda Turma, Mauro Campbell Marques, DJe 24/09/2019): o gravame de APP «esvazia completamente o direito à propriedade».
- O Basanos deu `fora_do_indice`, com 4 citantes no acervo e um AREsp homônimo: divergência a investigar antes de qualquer uso.
- Os ED do Município foram rejeitados (19/10/2021).

**A-32: AgInt no REsp 2.062.845, desfecho.** Leve, ressalva. O STJ deu provimento ao Município e devolveu os autos «para cotejo da situação fática». A regra e a exceção citadas pela ficha conferem literalmente.

**Conferido sem problema.** Contagens: 2 no catálogo; 107/134/21; API 2 brutos e 1 no pacote; DJEN 0. A amostra confere (ruído e uma contrária pertinente). 0526259 confere (Primeira Câmara, 13/06/2022, apelação do contribuinte improvida) e 8042604 também (Quinta Câmara, pandemia, falta de prova pré-constituída). O AgInt no AREsp 2.345.529 confere (Segunda Turma, publicado em 25/09/2024, Guarujá, Súmula 7; citação literal), e o AREsp 1.723.597 também (Herman Benjamin, publicado em 06/04/2021, TJSP/Serra Negra, «inexequibilidade absoluta de uso»; Súmula 7). O Tema 1010 confere (tese sobre a faixa de APP de curso d'água em área urbana consolidada): não pertinente, como a ficha diz.

## 3. Walton

| Ficha | Status | Coerência com a própria ficha |
|---|---|---|
| TES-27 | PLAUSIBLE | Coerente. A correção A-01 reforça a CQ1: são três acórdãos de câmara. A CQ3 aberta, "ciência inequívoca", está bem posta. |
| TES-31 | PLAUSIBLE | Coerente. A CQ1 ganha uma prova que a ficha não usou: a 2ª VP aplicou o Tema 387 **a favor** do contribuinte (0848075). |
| TES-19 | PLAUSIBLE | Coerente, desde que restrito à destinação agropecuária **provada**, como a ficha faz. A queda a WEAK para destinação industrial é correta. |
| TES-29 | PLAUSIBLE | Coerente para Lauro de Freitas × área administrada por Salvador com prova documental. A contra-analogia (8077091) está correta. |
| TES-30 | PLAUSIBLE | Coerente como esquema. A ficha condiciona a prova pericial da restrição total, e a base (3 favoráveis, 1 contrária) justifica o risco médio a alto. |

## 4. Tabela dos [A CONFERIR]

| Ficha | Item | Resultado | Referência certa / texto da fonte |
|---|---|---|---|
| TES-27 | CF, art. 5º, LV | **confere** | Inciso no Planalto. Citado expressamente em 8165454, item 7: «em violação ao art. 5º, LV, da CF/1988». |
| TES-27 | CTN, art. 32, e lei municipal de perímetro (8011756) | **confere** (CTN); lei municipal: limite | CTN art. 32 e § 1º (Planalto). A ementa funda-se no contraditório. Lei de Camaçari não lida. |
| TES-27 | REsp 1.933.514 | **confere** (existe); não é precedente | AgInt no REsp 1.933.514, Segunda Turma, 04/11/2021, não conhecido (Súmulas 7/STJ e 280/STF, na face); Campinas; «ÔNUS DA PROVA DO RECEBIMENTO DO CARNÊ DO IPTU. CONTRIBUINTE.»: sinal contrário. |
| TES-27 | Mandado de segurança | **não localizado** no material desta tese | Limite mantido (0848075, MS da TES-31, é sobre erro de direito, não notificação). |
| TES-31 | Súmula 227/TFR | **não localizado** em fonte própria | Só a transcrição no teor do REsp 1.130.545, item 7, que confere. |
| TES-31 | Mandado de segurança | **diverge** | Há caso: 0848075, «APELAÇÃO CÍVEL em Mandado de Segurança», Terceira Câmara; REsp do Município com seguimento negado pelo Tema 387. |
| TES-19 | CF, art. 5º, LV | **confere** | Inciso no Planalto; não está nos excertos. |
| TES-19 | Súmula 473/STF (§ 2) | **confere** | `STF:sumulas:473`. Invocada por 8055247, por 8052650 e pela favorável 8010153. |
| TES-19 | Súmula 473/STF (§ 4) | **confere** | Idem. |
| TES-29 | CF, art. 156, I; CTN, art. 32 | **confere** | Planalto. As ementas citam o CTN, art. 7º (8023542) e a Constituição da Bahia, arts. 11, XVI, e 70, IV (8012160). |
| TES-29 | MS 439 (tribunal, partes, trânsito) | limite (inteiro teor TJBA) | A ementa de 8008800 diz «impetrando em 2015», região de Ipitanga, «Loteamento Marissol I e II». |
| TES-29 | CTN, art. 164, III | **confere** | "de exigência, por mais de uma pessoa jurídica de direito público, de tributo idêntico sôbre um mesmo fato gerador". |
| TES-29 | Súmula 280/STF | **confere** | "Por ofensa a direito local não cabe recurso extraordinário." |
| TES-29 | MS 439 e Lei 2.713/1969 (base real) | **não localizado** (Lei 2.713); MS: limite | Ano divergente nos textos do TJBA (2.713/62 × 2.713/1969). |
| TES-30 | CPC, art. 300 | **confere** | "A tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo." |
| TES-30 | Lei 12.651/2012, art. 4º | **confere**, com ajuste | O art. 3º, II, define APP; o art. 4º delimita. Os casos do TJBA são APA/ZPAM. |
| TES-30 | STF | **não localizado** | Busca exploratória sem pertinência. |
| TES-30 | AREsp 2.594.742 | **confere** (existe), com ajuste | AgInt no AREsp, Segunda Turma, 19/08/2025; Súmulas 283 e 284/STF; o STJ não decidiu a prova. |

## 5. O que não foi verificado

- **Inteiro teor do TJBA:** não está no laboratório. Conferi ementa e face do texto (cabeçalho, ementa, dispositivo).
- **Lei municipal:**
  - Camaçari (perímetro urbano; TES-27 e TES-19);
  - Salvador (padrão construtivo, Planta Genérica, ZPAM; TES-31 e TES-30);
  - Plano Diretor de Pojuca (TES-19).
- **Lei Estadual da Bahia 2.713** (ano e texto) e **MS 439** (TES-29).
- **Súmula 227/TFR** em fonte própria.
- **STF sobre IPTU em APP:** acervo telegráfico; fonte oficial não consultada.
- **REsp 1.695.340/MG**, citado pelo TJBA em 0555629: fora do índice do Basanos, não aberto.
- **Vigência atual dos precedentes:** o acervo não prova ausência de superação posterior. Nenhum sinal de superação foi visto.
- **Os 602 excertos do lote E4-3:** não refiz a conferência dos que estão fora destas cinco fichas. Os 72 destas fichas foram reconferidos por código (72/72).
