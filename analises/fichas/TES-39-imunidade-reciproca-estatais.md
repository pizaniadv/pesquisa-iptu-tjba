---
tipo: ficha-de-tese
data: 2026-11-06
produzido-por: claude-code (executor F7, Opus)
versao-core: 1.0
status: draft
tese: 39
id: TES-002
---

# TES-39 (TES-002) · Imunidade recíproca de estatais e concessionárias no IPTU (art. 150, VI, *a*)

**Duas camadas, sempre separadas:**
- **(T3)** 37 processos de alínea *a* lidos pelo leitor Opus na base inteira (`analises/teses/TES-001-tabela-v1.csv`, `dados/decisoes/`).
- **(E)** 98 processos (130 decisões) da fatia `TES002_a`, lidos **só no nível de ementa** (`derivados/ementas-candidatos.jsonl`).

A fatia tem 134 decisões e 102 processos. Quatro desses processos são de alínea *c* (Abrigo do Salvador e afins, já na TES-001) e entraram pela palavra "Tema 437"; foram retirados.

**Mapa dos campos do JSON (não há pacote E4-3 para esta tese):** `n_catalogo_fav` = processos favoráveis da camada T3; `n_acervo` = processos da camada E; `n_acervo_fav` = desses, os com indício favorável por palavra em algum ato (§ 3.6; indício, não resultado).

## 1. Formulação
Se a estatal presta serviço público essencial, sem fim lucrativo e fora de concorrência (EMBASA, CODEBA como autoridade portuária, CONDER), e o imóvel está afetado a esse serviço, então o IPTU não incide pela imunidade recíproca (na camada E, só por ementa, têm indício favorável por palavra 23 dos 38 processos da EMBASA, 11 dos 21 da CODEBA e 3 dos 4 da CONDER, o que não é resultado; para a EMBASA há contrária na 3ª CC em 25/11/2024 e, na 4ª CC, apelação do Município provida em 02/2025 mas revertida por embargos de declaração em 06/2025, que restabeleceram a imunidade (0097379-11.2009), ver § "EMBASA" adiante; ajuste do orquestrador em 06/11/2026 após o fichamento). Se quem ocupa o imóvel é concessionária privada com fim lucrativo (COELBA), a imunidade só se sustenta, num TJBA dividido (na camada T3, 11 favoráveis e 17 desfavoráveis da COELBA), se o imóvel é bem público afetado ao serviço e a câmara aceita distinguir os Temas 385 e 437; o desfecho depende do Tema 1.297 (pendente) e, para estatais, do Tema 1.398 (sem tese).

## 2. Fundamento normativo
- **CF, art. 150, VI, *a*, e §§ 2º e 3º;** CF, art. 173, §§ 1º e 2º (regime das empresas privadas), usado pelas contrárias;
- **CF, art. 155, § 3º:** invocado pela COELBA e afastado (8000741-22.2020; 8002112-79.2022);
- **CTN, arts. 32 e 34** (posse com *animus domini*): base da tese da "mera detenção" (8002112-79.2022, ED; 8001007-60.2020);
- **Lei 8.987/1995, arts. 35, § 1º, e 36 (reversão dos bens) e art. 6º, § 1º (modicidade tarifária):** 0001165-60.2014 (que atribui a reversibilidade ao art. 14, dispositivo que trata da prévia licitação, e a modicidade ao art. 9º, § 3º); 8002321-09.2019 (art. 6º, § 1º);
- **Leis 8.630/1993 e 12.815/2013 (autoridade portuária):** CODEBA, 0034925-34.2005.

## 3. Como o TJBA decide
**Números (indício, não taxa; universo = indício IPTU-04 da trilha neutra).** Camada T3: 37 processos, 15 favoráveis, 20 desfavoráveis, os demais sem exame. A COELBA responde por 29. Camada E: 98 processos só por ementa (§ 3.6).

### 3.1 COELBA: divergência entre câmaras, e também no tempo (T3)
Na COELBA, 11 processos são favoráveis e 17 desfavoráveis. A divergência descrita no brief ("a 5ª reconhece; a 1ª e a 3ª negam") é **parcialmente** confirmada:

| Órgão | Favoráveis | Desfavoráveis | Sem exame | Sequência (data: resultado) |
|---|---|---|---|---|
| 1ª CC | 1 | 7 | 0 | 2023-08: desf; 2023-10: fav; 2024-06: desf; 2024-07: desf; 2025-05: desf; 2025-08: desf; 2025-10: desf; 2026-03: desf |
| 2ª CC | 0 | 1 | 0 | 2020-07: desf |
| 3ª CC | 4 | 4 | 0 | 2021-11: desf; 2022-11: fav; 2023-10: desf; 2024-02: fav; 2025-03: desf; 2025-10: desf; 2025-11: fav; 2025-12: fav |
| 4ª CC | 2 | 1 | 0 | 2021-08: fav; 2021-10: desf; 2025-08: fav |
| 5ª CC | 4 | 4 | 0 | 2021-05: desf; 2023-08: desf; 2024-08: desf; 2024-10 (ED): fav; 2025-04: fav; 2025-05: fav; 2025-07: fav; 2026-09: desf |
| Órgão Especial | 0 | 0 | 1 | 2024-03: s/exame |

O que os dados mostram:

- **5ª CC.** Negou nos 3 processos julgados de 2021 a 08/2024 (e também na apelação de 8002112-79.2022, em 02/04/2024, depois revertida) e reconheceu nas 4 seguintes, de 10/2024 a 07/2025, a primeira delas nos embargos de declaração de 8002112-79.2022 (30/10/2024): «A imunidade tributária constante do art. 150, VI, a, da Constituição Federal alcança o imóvel pertencente à União que se encontra em posse precária de concessionária de serviço público para ser utilizado na atividade-fim a qual essa se destina».
  - Depois vieram 0001165-60.2014, 0301824-70.2014 e 8002321-09.2019, todos de 2025. Exemplo: «7. O Município de Itaberaba não demonstrou que o imóvel seria utilizado para fins diversos da prestação do serviço público essencial, sendo incabível a cobrança do IPTU.»
  - Mas em 16/09/2026 (8000259-57.2018, agravo interno) a 5ª voltou a negar, pelo Tema 508 aplicado por analogia: «O Supremo Tribunal Federal, no julgamento do Tema 508 de repercussão geral, fixou entendimento de que sociedade de economia mista voltada à remuneração de capital de controladores ou acionistas não está abrangida pela imunidade tributária do art. 150, VI, "a", da Constituição, unicamente em razão das atividades desempenhadas, entendimento aplicável, por analogia, à concessionária de capital aberto que exerce atividade econômica com finalidade lucrativa.»
- **1ª CC.** Nega com constância (7 de 8). O critério é a natureza do sujeito: «O critério determinante é a natureza jurídica do sujeito e o caráter lucrativo de suas operações, independentemente do grau de competição no setor.» A exceção é 0500536-61.2015 (17/10/2023): «No julgamento do RE 1315581, sob relatoria do eminente Ministro Luís Roberto Barroso, restou concretizado o entendimento de que a concessionária de serviço público, ocupante de bem da União, que utiliza o imóvel na prestação de sua atividade-fim, faz jus à imunidade do IPTU incidente sobre tal bem.»
- **3ª CC.** Está dividida. Negou em 2021, 2023 e 2025: «Logo, sujeita-se à cobrança de IPTU, ainda que preste serviço público e o bem esteja afetado a esta finalidade, considerando o seu intuito lucrativo.» Reconheceu em 2022 (8002105-72.2020), em tutela em 2024 (8002930-34.2023) e no fim de 2025: «Compete ao ente tributante comprovar eventual desvio de finalidade do bem imóvel para afastar a imunidade.»
- **4ª CC.** Em 2025 reconheceu e pôs o ônus no Fisco: «2. O ônus de comprovar a desvinculação do imóvel de sua finalidade pública recai sobre o Fisco, presumindo-se a imunidade derivada da Carta Magna, em favor da concessionária.» Em 2021 tinha negado pelo Tema 508 (8000200-86.2020).
- **Fundamento das contrárias:** Temas 385 e 437 (concessionária com fim lucrativo) e Tema 508 (capital aberto). Exemplo: «O STF pacificou o seu entendimento acerca da controvérsia submetida a esta Turma Julgadora ao julgar os TEMAS 385 (RE nº 594.015/SP) e 437 (RE nº 601.720/RJ), ambos em sede de Repercussão Geral, consolidando a orientação jurídica da não aplicação do instituto da imunidade tributária sobre imóveis cedidos à pessoa jurídica de direito privado, em decorrência do intuito lucrativo dos concessionários, remetendo-os ao regime jurídico estabelecido no art. 173, §2º, da Constituição Federal.»
- **Fundamento das favoráveis:** distinção dos Temas 385/437 (serviço essencial em exclusividade; bem público afetado e reversível; posse precária sem *animus domini*), com RE 1.315.581, RE 1.272.751 e Rcl 32.717 do STF (`[A CONFERIR]`).

### 3.2 Sobrestamento pelo Tema 1.297
A 2ª Vice-Presidência sobrestou, em 2025, recursos extraordinários em processos da COELBA do material (no exemplo, o RE é do Município de Serrolândia, vencido em 8002105-72.2020) até o julgamento do RE 1.479.602 (Tema 1.297): «Nessa compreensão, amparado no art. 1.030, inciso III, do Código de Ritos, é medida que se impõe o sobrestamento do Recurso Extraordinário interposto (ID 57054405), até o pronunciamento definitivo da Suprema Corte no Leading Case RE n.º 1.479.602 (Tema 1.297), que deu origem ao (TEMA 1.297).» O Órgão Especial reabriu admissibilidade já negada pelos Temas 385/437: «A superveniência do reconhecimento da repercussão geral no RE n.º 1.479.602 (Tema 1.297/STF), que trata da imunidade tributária recíproca sobre bens afetados à concessão de serviço público, justifica a revisão da decisão recorrida.» Há sobrestamento também em 8000741-22.2020, 8000244-71.2021 e 0301865-58.2014 (tabela § 3.5).

### 3.3 O estranhamento do Vice-Presidente
Em 0305624-06.2014.8.05.0113 (decisão de 31/03/2026), o STJ (Min. Benedito Gonçalves, AREsp 2.957.046/BA) devolveu os autos à origem para que se sobrestasse a tramitação até a publicação do acórdão paradigma do Tema 1.297. A 2ª Vice-Presidência questionou: «Nessa compreensão, causa estranheza a vinculação do presente caso ao Tema 1297/STF, porquanto este trata de fornecimento de energia elétrica e aquele trata de serviço público de transporte ferroviário.» E concluiu: «Ante o exposto, rogo, com a devida vênia, por esclarecimentos acerca da aplicação do Tema em referência, que se encontra afetado sob o rito da repercussão geral.»

O cadastro do Tema 1.297 no Cognitio (`STF:repercussao_geral:tema-1297`, conferido em 06/11/2026) confirma a premissa: a questão é «se o arrendamento de bem imóvel da União para concessionária de serviço público de transporte ferroviário afasta a imunidade tributária recíproca, com a consequente incidência de IPTU sobre o imóvel afetado à prestação do serviço». O caso de energia só entra por analogia. O Tema 1.398 (bens de **estatais** afetados a serviço público) está mais próximo da EMBASA e da CODEBA do que da COELBA, que é concessionária privada.

### 3.4 CODEBA, EMBASA e demais estatais (T3)
- **CODEBA** (0034925-34.2005, 5ª CC, 13/07/2021): é autoridade portuária e foi distinguida do Tema 385. «a apelada exerce a função de autoridade portuária, nos termos da Lei nº 8.630/1993 e da Lei nº 12.815/2013, prestando serviço público essencial de administração e exploração portuária, por delegação da União, exercendo atividade sem fins lucrativos.» e «entendo que o substrato fático da presente lide é distinta da tese consolidada pelo Tema 385 pelo STF em sede de recurso extraordinário com repercussão geral reconhecida, como o próprio Supremo reconheceu em sede do ARE nº 931099/BA, razão pela qual me alinho ao entendimento deste respeitável Tribunal de Justiça para reconhecer o direito da apelada à imunidade tributária recíproca prevista no art. 150, VI, a, da CF/88, nos moldes da sentença prolatada em primeiro grau, a qual deve ser mantida.»
- **EMBASA** (0804790-54.2015, 1ª CC, 2020; 8000744-14.2017, 4ª CC, 2020): imunidade reconhecida. «As empresas públicas e sociedades de economia mista prestadoras de serviço público de prestação obrigatória e exclusiva do Estado são abrangidas pela imunidade tributária recíproca prevista no art. 150, VI, a, da Constituição Federal.»
- **CONDER** (8001156-16.2021, 2ª CC, 2025): «4. A CONDER, como empresa pública vinculada ao Estado da Bahia, atua na execução de políticas públicas de desenvolvimento urbano e habitação, não configurando exploração de atividade econômica em regime concorrencial.»
- **SUDIC, autarquia** (8019519-43.2019, 2ª VP, 2022): ônus do Município, recurso extraordinário inadmitido (Súmula 279). «ser o ônus do poder tributante elidir a presunção de que o imóvel gerador do tributo se destina às finalidades institucionais da autarquia.»
- **Contrárias fora da COELBA:**
  - CNB, transporte hidroviário com tarifa (0413836-40.2012, 3ª CC, 2025): «Restou evidenciado nos autos que a CNB, embora vinculada ao Estado da Bahia, é sociedade de economia mista que exerce atividade empresarial com fins lucrativos – transporte hidroviário de passageiros e veículos –, mediante cobrança de tarifas, o que a afasta do alcance da imunidade tributária recíproca.»
  - URBIS (8027427-44.2025, 1ª CC, 2025), em exceção, com ônus do contribuinte: «Para a aplicação da imunidade tributária às sociedades de economia mista, é indispensável a comprovação inequívoca do exercício de serviço público essencial, em caráter de exclusividade, sem fins lucrativos e fora do regime de concorrência.»

### 3.5 Tabela por processo (T3)
| Processo | Entidade | Órgão | Data | Via (indício) | Resultado no processo | Nota |
|---|---|---|---|---|---|---|
| 0413836-40.2012.8.05.0001 | CNB | 3ª CC | 2025-09-02 | embargos_execucao | desfavoravel |  |
| 0034925-34.2005.8.05.0001 | CODEBA | 5ª CC | 2021-07-13 | embargos_execucao | favoravel |  |
| 8000741-22.2020.8.05.0119 | COELBA (concessionária de energia) | 1ª CC | 2023-08-15 | acao_conhecimento_ou_outro | desfavoravel | feito sobrestado pelo Tema 1.297 (Órgão Especial, ED no agravo interno, 16/07/2025, DEC-TJBA-57e8d3985cfb); em 05/2026 a 2ª VP manteve as inadmissões e remeteu ARE ao STF e AREsp ao STJ (DJEN 617521669 e 623283948) |
| 0500536-61.2015.8.05.0244 | COELBA (concessionária de energia) | 1ª CC | 2023-10-17 | acao_conhecimento_ou_outro | favoravel | trajetória (releitura H2, 06/11): embargos de declaração acolhidos em parte em 12/08/2024 (DEC-TJBA-a320d38f47dc); o provimento passa a parcial |
| 8000244-71.2021.8.05.0119 | COELBA (concessionária de energia) | 1ª CC | 2024-06-04 | embargos_execucao | desfavoravel | RE sobrestado pelo Tema 1.297 (27/05/2025) |
| 8000297-35.2020.8.05.0233 | COELBA (concessionária de energia) | 1ª CC | 2024-07-16 | acao_conhecimento_ou_outro | desfavoravel |  |
| 0300365-78.2019.8.05.0105 | COELBA (concessionária de energia) | 1ª CC | 2025-05-13 | embargos_execucao | desfavoravel |  |
| 8000755-40.2020.8.05.0237 | COELBA (concessionária de energia) | 1ª CC | 2025-08-19 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8000839-36.2019.8.05.0056 | COELBA (concessionária de energia) | 1ª CC | 2025-10-23 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8000682-05.2019.8.05.0043 | COELBA (concessionária de energia) | 1ª CC | 2026-03-30 | embargos_execucao | desfavoravel |  |
| 8019135-17.2018.8.05.0000 | COELBA (concessionária de energia) | 2ª CC | 2020-07-01 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8008392-11.2019.8.05.0000 | COELBA (concessionária de energia) | 3ª CC | 2021-11-09 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8002105-72.2020.8.05.0137 | COELBA (concessionária de energia) | 3ª CC | 2022-11-22 | embargos_execucao | favoravel | RE sobrestado pelo Tema 1.297 (19/03/2025) |
| 8033936-93.2022.8.05.0000 | COELBA (concessionária de energia) | 3ª CC | 2023-10-23 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8002930-34.2023.8.05.0000 | COELBA (concessionária de energia) | 3ª CC | 2024-02-28 | tutela | favoravel | tutela (provisória); trajetória (releitura H2, 06/11): agravo de instrumento da concessionária desprovido em 16/05/2023 (DEC-TJBA-fd5f8aeaf0cc), revertido por embargos de declaração com efeito infringente em 28/02/2024 (DEC-TJBA-4621b7bf10d8) |
| 8000236-35.2019.8.05.0032 | COELBA (concessionária de energia) | 3ª CC | 2025-03-12 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8012084-08.2025.8.05.0000 | COELBA (concessionária de energia) | 3ª CC | 2025-10-15 | acao_conhecimento_ou_outro | desfavoravel |  |
| 8001007-60.2020.8.05.0199 | COELBA (concessionária de energia) | 3ª CC | 2025-11-13 | acao_conhecimento_ou_outro | favoravel |  |
| 8005052-96.2023.8.05.0201 | COELBA (concessionária de energia) | 3ª CC | 2025-12-10 | acao_conhecimento_ou_outro | favoravel | ônus do ente tributante |
| 8002710-41.2020.8.05.0000 | COELBA (concessionária de energia) | 4ª CC | 2021-08-04 | acao_conhecimento_ou_outro | favoravel | tutela em AI (provisória) |
| 8000200-86.2020.8.05.0119 | COELBA (concessionária de energia) | 4ª CC | 2021-10-27 | embargos_execucao | desfavoravel | trajetória (releitura H2, 06/11): embargos do Órgão Especial não acolhidos em 25/09/2024 (DEC-TJBA-8dc97d887723); embargos de declaração nesses embargos acolhidos com efeitos infringentes, à vista do reconhecimento superveniente da repercussão geral no Tema 1.297, para desconstituir a negativa de seguimento do RE e reservar novo juízo de admissibilidade (ementa no DJEN 321762668, disponibilizada em 10/07/2025; data da sessão não escrita no texto; sem registro próprio) |
| 8000964-84.2021.8.05.0136 | COELBA (concessionária de energia) | 4ª CC | 2025-08-05 | acao_conhecimento_ou_outro | favoravel | ônus do Fisco |
| 0303373-71.2014.8.05.0256 | COELBA (concessionária de energia) | 5ª CC | 2021-05-26 | execucao_fiscal_outro | desfavoravel | trajetória (releitura H2, 06/11): embargos do Órgão Especial não acolhidos em 27/03/2024 (DEC-TJBA-0a49ea9f7548) |
| 0305624-06.2014.8.05.0113 | COELBA (concessionária de energia) | 5ª CC | 2023-08-22 | acao_conhecimento_ou_outro | desfavoravel | 2ª VP pede esclarecimento sobre a vinculação ao Tema 1.297 (31/03/2026) |
| 8002112-79.2022.8.05.0271 | COELBA (concessionária de energia) | 5ª CC | 2024-04-02 | embargos_execucao | favoravel | apelação desfavorável (02/04/2024) revertida por ED com efeitos infringentes (30/10/2024) |
| 0301865-58.2014.8.05.0105 | COELBA (concessionária de energia) | 5ª CC | 2024-08-27 | embargos_execucao | desfavoravel | bem da própria concessionária; RE sobrestado pelo Tema 1.297 (19/05/2025) |
| 0001165-60.2014.8.05.0072 | COELBA (concessionária de energia) | 5ª CC | 2025-04-08 | acao_conhecimento_ou_outro | favoravel |  |
| 0301824-70.2014.8.05.0112 | COELBA (concessionária de energia) | 5ª CC | 2025-05-05 | acao_conhecimento_ou_outro | favoravel | Município não provou uso diverso |
| 8002321-09.2019.8.05.0027 | COELBA (concessionária de energia) | 5ª CC | 2025-07-16 | acao_conhecimento_ou_outro | favoravel |  |
| 8000259-57.2018.8.05.0212 | COELBA (concessionária de energia) | 5ª CC | 2026-09-16 | acao_conhecimento_ou_outro | desfavoravel |  |
| 0569016-78.2014.8.05.0001 | COELBA (concessionária de energia) | Órgão Especial | 2024-03-27 | acao_conhecimento_ou_outro | sem_exame | Órgão Especial reabre a admissibilidade do RE pelo Tema 1.297 (17/07/2025) |
| 8001156-16.2021.8.05.0201 | CONDER | 2ª CC | 2025-04-07 | execucao_fiscal_outro | favoravel |  |
| 0804790-54.2015.8.05.0001 | EMBASA | 1ª CC | 2020-06-08 | excecao_pre_executividade | favoravel |  |
| 8000744-14.2017.8.05.0076 | EMBASA | 4ª CC | 2020-10-16 | acao_conhecimento_ou_outro | favoravel |  |
| 8020692-92.2025.8.05.0000 | SEM habitacional em liquidação | 3ª CC | 2025-08-26 | excecao_pre_executividade | desfavoravel | exceção; ônus do contribuinte |
| 8019519-43.2019.8.05.0000 | SUDIC (autarquia) | 2ª Vice-Presidência | 2022-03-21 | embargos_execucao | sem_exame |  |
| 8027427-44.2025.8.05.0000 | URBIS | 1ª CC | 2025-11-06 | excecao_pre_executividade | desfavoravel | exceção; ônus do contribuinte; Tema 1.140 |

### 3.6 Camada E: 98 processos só por ementa (não lidos)
Entidade por palavra na ementa; o "indício favorável" é o recorte por palavra da trilha, **não é resultado**.

| Entidade (por palavra na ementa) | Processos | Com indício favorável em algum ato |
|---|---|---|
| EMBASA | 38 | 23 |
| outras | 25 | 7 |
| CODEBA | 21 | 11 |
| URBIS | 8 | 3 |
| CONDER | 4 | 3 |
| INFRAERO | 1 | 0 |
| CHESF | 1 | 0 |

O que as ementas sugerem (hipóteses para a leitura T3, não achados):
- **EMBASA.** 23 dos 38 processos têm indício favorável por palavra em algum ato (tabela acima; indício, não resultado). Mas a 3ª CC negou em 0001957-92.2012 (25/11/2024): «A EMBASA, por ser uma sociedade anônima de economia mista, com fins lucrativos, não faz jus à imunidade tributária recíproca». Na 4ª CC não houve reversão: a apelação do Município foi provida (0097379-11.2009, 02/2025, DEC-TJBA-433f5ca201c4), mas os embargos de declaração da EMBASA foram providos (06/2025, DEC-TJBA-697b4e0f5e10): «Embargos de declaração providos para, reformando o acórdão embargado, negar provimento ao recurso apelativo interposto pelo Município de Salvador, mantendo incólume a sentença que reconheceu a imunidade tributária pleiteada pela Empresa Baiana de Águas e Saneamento S/A (Embasa).»
- **CODEBA.** 11 dos 21 processos têm indício favorável por palavra (indício, não resultado); a ementa do exemplo distingue o Tema 385. Exemplo: «INAPLICABILIDADE DO TEMA 385, DO SUPREMO TRIBUNAL FEDERAL. RECONHECIMENTO DE IMUNIDADE TRIBUTÁRIA DA CODEBA.»
- **URBIS.** Divisão em 2025 sobre exclusividade e concorrência (Tema 1.140, RE 1.320.054: imunidade da estatal delegatária de serviço essencial que não distribua lucros a acionistas privados nem ofereça risco ao equilíbrio concorrencial; alcance ao MIJ). Exemplo: «atua em regime concorrencial com agentes privados do setor de construção civil, não preenchendo o requisito da exclusividade exigido pela jurisprudência consolidada do STF»
- **Outras** (25 processos): terminal rodoviário (SINART), ferrovia e terreno de marinha, entre outros; CHESF e INFRAERO têm linha própria na tabela (1 processo cada). Não foram classificadas.

## 4. Precedentes qualificados do STJ e do STF
| Identificador | Tese ou questão | Fonte | Conferido |
|---|---|---|---|
| Tema 385 (RE 594.015) | imunidade recíproca não se estende a empresa privada arrendatária de imóvel público que explora atividade econômica com fins lucrativos | PANGEA `stf-rg-385` | sim (espelho) |
| Tema 437 (RE 601.720) | incide IPTU sobre imóvel de pessoa jurídica de direito público cedido a pessoa jurídica de direito privado, devedora do tributo | PANGEA `stf-rg-437` | sim (espelho) |
| Tema 508 (RE 600.867) | sociedade de economia mista com ações em bolsa, voltada à remuneração do capital, não está abrangida pela imunidade | Cognitio `STF:paradigmas-teor:508-753969848` (tese) | sim |
| Tema 1.297 (RE 1.479.602) | arrendamento de imóvel da União a concessionária de **transporte ferroviário**; RG reconhecida, sem tese | Cognitio `STF:repercussao_geral:tema-1297` (cadastro) | sim (cadastro; não está no PANGEA) |
| Tema 1.398 (RE 1.317.330) | «Garantia de imunidade tributária para fins de incidência de IPTU em relação a bens imóveis de estatais afetados à prestação de serviço público» (a questão fala de imóvel de sociedade de economia mista, à luz dos arts. 150, VI, a, e 155, § 3º, da CF); RG reconhecida (acórdão publicado em 23/05/2025), sem tese em 06/11/2026 | PANGEA `stf-rg-1398`; Cognitio `STF:repercussao_geral:tema-1398`; portal do STF | sim (cadastro e portal) |
| Tema 644 (ECT) | imunidade da ECT alcança o IPTU de imóveis de sua propriedade e por ela utilizados, sem distinção a priori entre os afetados ao serviço postal e à atividade econômica | PANGEA `stf-rg-644` | sim (espelho) |
| Tema 1.140 (RE 1.320.054, Metrô-SP) | «As empresas públicas e as sociedades de economia mista delegatárias de serviços públicos essenciais, que não distribuam lucros a acionistas privados nem ofereçam risco ao equilíbrio concorrencial, são beneficiárias da imunidade tributária recíproca prevista no artigo 150, VI, a, da Constituição Federal, independentemente de cobrança de tarifa como contraprestação do serviço.»; invocado nos casos URBIS, EMBASA (0097379-11.2009) e COELBA (distinção em 8001007-60.2020); é o pilar da formulação para estatais (alcance ao MIJ) | Cognitio `STF:paradigmas-teor:1140-755857209` (tese) | sim (tese) |
| RE 1.315.581; RE 1.272.751; Rcl 32.717; RE 918.700; ARE 947.142 AgR; ADPF 858 | precedentes citados pelas favoráveis | citados nos votos do TJBA; existência conferida no portal do STF (metadados): RE 1.315.581 (Barroso), RE 1.272.751 (Toffoli; há AgR), Rcl 32.717 (Fux; o voto de 8002321-09.2019 a dá a Alexandre de Moraes), RE 918.700 (Barroso), ARE 947.142 (Toffoli; há AgR), ADPF 858 (Nunes Marques) | existência sim; teor `[A CONFERIR]` |
| RE 1.395.601 AgR; Rcl 70.570 | citados pelas contrárias (1ª CC) | citados nos votos; existência conferida no portal do STF (metadados): RE 1.395.601 (Fachin; há AgR), Rcl 70.570 (Fachin) | existência sim; teor `[A CONFERIR]` |
| STJ REsp 1.089.827/RJ | posse precária de concessionária | citado (5ª CC, 0001165-60.2014, como «Rel. Min. Regina Helena Costa, DJe 13.08.2018») | não localizado no Cognitio nem conferido no portal do STJ `[A CONFERIR]` |

## 5. Via processual
- **Ação anulatória ou declaratória, com tutela, e embargos à execução:** são as vias da COELBA na camada T3: pela via indicada na tabela do § 3.5, 20 dos 29 processos são ação de conhecimento ou outra, 7 são embargos à execução, 1 é tutela e 1 é execução fiscal. Nelas se prova a afetação do imóvel (subestação), a titularidade pública e a reversibilidade. A 5ª CC aceitou estender a declaração a imóveis de mesma destinação (0001165-60.2014, embargos de declaração).
- **Exceção de pré-executividade:** funciona para EMBASA, CODEBA e CONDER quando a condição é objetiva (camada E). Falhou para URBIS e para a SEM habitacional, que não provaram de plano exclusividade e ausência de concorrência (8027427-44.2025; 8020692-92.2025).
- **Prova:**
  - natureza da entidade: estatuto e composição do capital (Tema 508);
  - afetação do imóvel ao serviço;
  - titularidade pública e contrato de concessão (cláusula de reversão);
  - ausência de concorrência.

## 6. Walton e Élenchos
**Argumento determinante (COELBA):** "imóvel público afetado a serviço essencial prestado em exclusividade por concessionária é imune; os Temas 385/437 não se aplicam".

| Item | Avaliação |
|---|---|
| Esquema | `ARG.SCH.WRM08.PRECEDENT` (WRM2008, p. 344) |
| CQ1 (proponente): a regra se aplica? | **unanswered**: os precedentes do STF que sustentam a distinção (RE 1.315.581, RE 1.272.751, Rcl 32.717) não foram conferidos |
| CQ2 (questionador): o caso é legítimo? | **unanswered**: exceção alegada e não rebatida (Tema 508 e natureza lucrativa; 8000839-36.2019; 8000259-57.2018) |
| CQ3 (questionador) | não alegada |
| Status do motor (06/11/2026) | **WEAK_UNANSWERED_CQ** |

Para EMBASA, CODEBA e CONDER o argumento é outro (estatal sem fim lucrativo em serviço essencial). Na camada E, 37 dos 63 processos dessas três entidades têm indício favorável por palavra (não é resultado); o argumento não foi avaliado aqui.

## 7. Limites e o que falta
- 98 processos só com ementa; a camada T3 tem, na maior parte, ementa e dispositivo.
- Os votos e acórdãos da COELBA não foram conferidos no inteiro teor.
- acervo local vai até 12/2025; a API de 2026 subconta; o DJEN não foi usado; o 1º grau está ausente; a lei municipal não foi lida.
- O resultado por processo vem da T3 (com a correção de 8002112-79.2022) e passou pela antialucinação em 06/11/2026 (`auditoria/antialucinacao-E43-F7.md`; nada grave, correções aplicadas); revisão humana pendente.
- O Tema 1.297 e o Tema 1.398 estão sem tese: qualquer posição é provisória.

## 8. Utilidade prática
- **Quando usar:**
  - EMBASA, CODEBA (autoridade portuária) e CONDER: em exceção, se a condição estatal e a afetação constam de documento;
  - COELBA: em ação anulatória ou embargos, distribuída à 5ª CC ou à 4ª CC, com prova de bem público afetado e reversível; e pedir o sobrestamento pelo Tema 1.297 nos recursos.
- **Quando não usar:** COELBA na 1ª CC (7 de 8 contrárias); bem da própria concessionária (0301865-58.2014); estatal em regime concorrencial (CNB; URBIS na 1ª CC).
- **Risco:** reviravolta pelo Tema 1.297 ou pelo Tema 1.398, e a própria 5ª CC voltou a negar em 09/2026.

**Revisão pós-Codex (06/11/2026).** Item 3 do Codex, JSON: acrescentado `n_acervo_fav` = 47; `n_acervo` = 98 (total) sem mudança. A `nota_campos` e o mapa de campos do § 3 dizem o que é o novo campo. Item 9 do Codex, formulação (MD e JSON): 'posição majoritária nas ementas' → 23 de 38 (EMBASA), 11 de 21 (CODEBA) e 3 de 4 (CONDER) com indício por palavra; 'TJBA dividido' → 11 × 17 na COELBA; 5ª CC 'passou a reconhecer' → 3 negativas e depois 4 favoráveis; 'passou a sobrestar' → sobrestou em processos do material; EMBASA 'maioria', CODEBA 'linha estável', 'vias dominantes' e 'maioria do material' → contagens da camada E e da tabela do § 3.5. Registro: `auditoria/correcoes-pos-codex-e43.jsonl`; originais em `estado/E4-3/antes-pos-codex/`.
