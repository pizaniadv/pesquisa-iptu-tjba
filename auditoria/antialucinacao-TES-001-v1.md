---
tipo: auditoria-antialucinacao
data: 2026-11-05
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
alvo: analises/teses/TES-001-imunidade-onus-da-destinacao.md (v1 piloto, 05/11/2026)
destino-do-alvo: interno (pesquisa; nada a renderizar)
metodo: conferência manual de cada afirmação contra a fonte própria (não o pipeline `conferidor`: destino interno e formato pedido trecho/fonte/gravidade)
---

# Antialucinação — TES-001 v1

## 1. Veredito

**Nada grave.** Nenhuma citação inventada, nenhuma aspa falsa, nenhum número errado. Os três excertos do § 5 são literais; a SV 52, a tese do Tema 693, o § 1º-A do art. 156 e o § 4º do art. 150 batem com a fonte; 443 e a composição do piloto batem com os dados.

Há **um erro objetivo de fato (médio)**, que convém corrigir antes de qualquer uso, porque recai justamente na variável que o dossiê usa para explicar a divergência (a via): o caso do sindicato (DEC-TJBA-4a49bc3601d8) foi decidido em **embargos à execução fiscal**, e não "na execução fiscal". Há também uma qualificação média (a "divergência quanto ao ônus") e cinco ressalvas leves.

## 2. Afirmações problemáticas

### A-01 — Via do caso do sindicato · **MÉDIO** · contradita (vermelho pelo contrato, por ser contradição objetiva) · espécie: deturpação de fato
- **Dossiê** (quatro lugares):
  - § 2 (b): "Em apelação na execução fiscal, a 4ª Câmara Cível (2024) manteve a extinção da execução";
  - § 3, tabela, linha 4a49: Via = "apelação na execução fiscal";
  - § 8, contra-analogia: "(i) a via (exceção, que exige prova de plano, × apelação na execução)";
  - § 10: "e defesa na própria execução".
- **Fonte** (`evidencias/extracoes/DEC-TJBA-4a49bc3601d8.txt`, ementa, início): "APELAÇÃO CÍVEL. DIREITO TRIBUTÁRIO. **EMBARGOS À EXECUÇÃO FISCAL**. IMPOSTO PREDIAL E TERRITORIAL URBANO - IPTU. BEM IMÓVEL. SINDICATO."
- **Por que importa:** embargos são ação autônoma, com cognição plena e dilação probatória. Não são "defesa na própria execução". A distinção real do piloto é **exceção (9d67, barrada por exigir dilação) × embargos (4a49, êxito)**. O fato verdadeiro reforça a hipótese do § 2 (a via decide), mas o dossiê descreve errado a via, que é o eixo da hipótese. O § 10 também deixa de mencionar os embargos como via de êxito.
- **Gravidade média, não grave:** a conclusão prática do § 13 ("não ir de exceção sem prova pré-constituída") continua de pé, e o documento é interno.

### A-02 — "Divergência quanto ao ônus" no caso do sindicato · **MÉDIO** · qualificação jurídica (amarelo: sinaliza, não trava)
- **Dossiê:** § 2 (b), título: "Sindicato, alínea *c*: divergência no TJBA"; e, sobre 9d67: "decidiu o contrário quanto ao ônus". Também na formulação estratégica: "tem apoio no TJBA para templos e divide o tribunal no caso do sindicato".
- **Fonte:**
  - 4a49 (o caso favorável do sindicato) não atribui ônus a ninguém. A ementa diz só "PRECEDENTE DO SUPREMO TRIBUNAL. DESVIO DE FINALIDADE DO BEM.NÃO VERIFICADO." Não há no texto disponível nenhuma frase sobre a quem cabia provar.
  - 9d67 (desfavorável): "1. Para o reconhecimento do direito à imunidade tributária, é indispensável o preenchimento dos requisitos previstos no art. 14 do CTN, cumulativamente, cuja comprovação incumbe ao contribuinte."
  - O único caso que põe o ônus no Município é 2f27 (templo, alínea *b*): "compete à Administração tributária demonstrar a eventual tredestinação do bem gravado pela imunidade."
- **Leitura:** a oposição explícita sobre ônus que o material mostra é **2f27 (b) × 9d67 (c)**, em alíneas diferentes. Na alínea *c*, há um favorável que não fala de ônus e um desfavorável que fala. "Decidiu o contrário quanto ao ônus" atribui ao 4a49 uma posição sobre ônus que o texto não traz. O próprio dossiê depois relativiza ("parece depender mais da via [...] do que de teses opostas sobre o ônus"), o que atenua. O que as três ementas sustentam: ônus no Município (2f27, *b*); ônus no contribuinte (9d67, *c*); nada sobre ônus (4a49, *c*).

### A-03 — "Insubsistência da CDA (*b* e *c*)" · **LEVE** · generalização (amarelo)
- **Dossiê** (§ 2, Consequência observada): "extinção da execução e insubsistência da CDA (*b* e *c*), com honorários pelo Município por causalidade ([DEC-TJBA-4a49bc3601d8]#Q2)".
- **Fonte:** só o 4a49 diz "INSUBSISTÊNCIA DA CERTIDÃO DE DÍVIDA ATIVA. EXTINÇÃO DA EXECUÇÃO" e "HONORÁRIOS SUCUMBENCIAIS. CAUSALIDADE. MUNICÍPIO QUE DEU CAUSA AO AJUIZAMENTO DA AÇÃO. HONORÁRIOS SUCUMBENCIAIS MAJORADOS, NA FORMA DO ART. 85, §11 DO CPC/2015". O 2f27 (alínea *b*) diz só "EXCEÇÃO DE PREEXECUTIVIDADE ACOLHIDA. EXTINÇÃO DO FEITO EXECUTIVO.", sem CDA e sem honorários no texto disponível (busca por "DÍVIDA ATIVA" e "honor" no arquivo: zero ocorrências).
- **Leitura:** a extinção vale para *b* e *c*; a insubsistência da CDA e os honorários estão só no caso *c*. Detalhe: os honorários também foram **majorados** (art. 85, § 11), e o dossiê não diz.

### A-04 — "Agravo contra a rejeição da exceção" · **LEVE** · paráfrase com inferência (amarelo)
- **Dossiê** (§ 2 (b)): "Em agravo contra a rejeição da exceção de pré-executividade, a 3ª Câmara Cível (2021)".
- **Fonte** (9d67): "Vistos, relatados e discutidos os presentes autos do **Agravo Interno nos autos do Agravo de Instrumento** nº 8022379-51.2018.8.05.0000"; a ementa diz "DECISÃO MANTIDA". O texto não diz qual decisão foi mantida nem transcreve a rejeição. O próprio registro anota: "'decisao mantida' refere-se a decisao anterior nao transcrita (relator ou origem)".
- **Leitura:** a rejeição na origem é inferência plausível, não está escrita. A tabela do § 3 ("exceção de pré-executividade → agravo interno") está mais perto do texto. Data: 2021-06-08 é a do metadado do banco, e o texto não data a sessão (metadado TJBA = data do portal). "2021" fica com essa ressalva.

### A-05 — Tema 693 usado como apoio da alínea *c* em geral · **LEVE** · alcance de precedente (amarelo, **MIJ**)
- **Dossiê:** § 6: "Precedentes qualificados: SV 52 (alínea *c*, imóvel alugado); Tema 693 (alínea *c*, imóvel ocioso)", listados como **decisões favoráveis** desta tese, que trata de templo e sindicato.
- **Fonte** (`DEC-PANGEA-16443fd19693.txt`; mesmo texto na tese do RE 767.332 RG no Cognitio): "A imunidade tributária prevista no art. 150, VI, c, da CF/88 aplica-se aos bens imóveis, temporariamente ociosos, de propriedade **das instituições de educação e de assistência social sem fins lucrativos** que atendam os requisitos legais."
- **Leitura:** o § 4 transcreve certo. Mas a tese do Tema 693 cobre só educação e assistência social, não sindicato nem partido, e trata de imóvel ocioso, não de quem tem o ônus da prova. Usar o tema para o sindicato é extensão. Fica para o MIJ (alcance), não é erro de texto.

### A-06 — J1: "amostra intencional de 4 casos" · **LEVE** · número ambíguo (amarelo)
- **Dossiê** (§ 8, J1): "não: amostra intencional de 4 casos".
- **Fonte** (`jurimetria/piloto-composicao.json`, IPTU-04): favorável_integral n = 6 (2 PANGEA + 4 TJBA: 2f27, 3b1f, 4a49, 4cbf); desfavorável n = 1 (9d67#Q2); sem_exame n = 1 (PANGEA 92184, Tema 1398).
- **Leitura:** "4" bate com os 4 favoráveis do TJBA no eixo, mas dois deles (3b1f e 4cbf, imunidade recíproca) o § 7 põe "fora desta tese". Para TES-001 (alíneas *b* e *c*), os acórdãos do TJBA são **3** (2 favoráveis, 1 desfavorável). O número não está errado, mas é ambíguo. O § 12 está correto.

### A-07 — Redação da alínea *b* na data dos fatos · **LEVE** · vigência, omissão que não falseia o texto (amarelo)
- **Dossiê:** § 1 "templo, art. 150, VI, *b*"; § 11 (Limites temporais) cita só a EC 116/2022.
- **Fonte** (Atlas, `constituicao-1988/art-150/caput/inc-VI/ali-b.md`): vigente: "b) entidades religiosas e templos de qualquer culto, inclusive suas organizações assistenciais e beneficentes; (Redação dada pela Emenda Constitucional nº 132, de 2023)"; e "a redação original era 'b) templos de qualquer culto;'".
- **Leitura:** o caso da Diocese (execução de 2014, julgado em 2022) correu sob a redação original ("templos de qualquer culto"). A EC 132/2023 ampliou a alínea *b* para "entidades religiosas". O § 11 deveria registrar também essa mudança, porque ela altera o enquadramento de uma Diocese, que é entidade e não templo. Não torna falsa nenhuma frase do dossiê.

## 3. Conferido e sustentado (verde)

| Afirmação do dossiê | Fonte e verificação |
|---|---|
| 2f27: 5ª Câmara Cível, 2022, Diocese, manteve sentença que acolheu exceção; ônus da tredestinação do Município, "inclusive locado" | ementa itens 2 e 3; dispositivo "CONHECER e NEGAR PROVIMENTO"; "Sala das sessões, de 2022"; meta 2022-03-16 |
| § 5, Q1 de 2f27 (aspas) | literal, `texto:1117-1401@sha256:e2b4925e96671e20`; conferido no arquivo |
| § 3 / § 8 A1: "a Fazenda não traz aos autos qualquer elemento" | literal, ementa item 3 |
| § 4: "lá a entidade era **locadora**" | inferência sustentada: "ainda que locado o imóvel [...] os rendimentos auferidos" (a Diocese recebe o aluguel) |
| 4a49: 4ª Câmara, 2024, lazer e recreação, "NÃO VERIFICADO", extinção, sentença mantida | ementa e dispositivo; § 5, Q1, literal (`texto:620-907`) |
| 9d67: 3ª Câmara, federação de trabalhadores, art. 14 do CTN, "presunção relativa" recusada, dilação probatória afasta a via | ementa itens 1, 2 e 3; § 5, Q2 e argumento rejeitado, literais (`texto:699-893`, `1091-1242`) |
| § 7: CODEBA, terreno de marinha da União, distinção dos Temas 385 e 437 (3b1f) | ementa item 3: "constituindo, inclusive, terreno de marinha [...] não há se falar em incidência do Tema 385 e 437 do STF" |
| § 7: EMBASA reconhecida em exceção de pré-executividade (4cbf) | dispositivo: "acolhendo a exceção de pré-executividade oposta pela agravante, extinguir a execução fiscal" |
| § 4: CF art. 150, § 4º, "relacionados com as finalidades essenciais" | Atlas `art-150.md` l. 150: "§ 4º - As vedações expressas no inciso VI, alíneas "b" e "c", compreendem somente o patrimônio, a renda e os serviços, relacionados com as finalidades essenciais das entidades nelas mencionadas." |
| § 4: CF art. 156, § 1º-A (EC 116/2022), aspas | Atlas `art-156/par-1-A.md` l. 57: idêntico, "(Incluído pela Emenda Constitucional nº 116, de 2022)" |
| CF art. 150, VI, *c* (entidades sindicais dos trabalhadores) | Atlas `ali-c.md` l. 86: "c) patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei;" |
| § 3 / § 8: "o art. 14 do CTN regula as entidades da alínea *c*" | Atlas `ctn/art-14.md` l. 87: "O disposto na alínea c do inciso IV do art. 9º é subordinado à observância dos seguintes requisitos pelas entidades nêle referidas"; art. 9º, IV, *c* (LC 104/2001) = partidos, sindicatos de trabalhadores, educação e assistência social |
| § 4: SV 52 (aspas) e "fala da alínea *c*, não da *b*" | `DEC-PANGEA-fee6cba8f601.txt`, idêntico (o espelho grafa ""c""); confirmado também no Cognitio `STF:sumulas:SV52` |
| § 4: Tema 693, aspas; RE 767.332 RG, julgado em 31/10/2013 | PANGEA 16443; Cognitio `STF:paradigmas-teor:693-4904092`: "31/10/2013 · PLENÁRIO", tese idêntica |
| § 7: Tema 1398 "só afetado, sem tese" | PANGEA 92184: "Há repercussão geral. Leading case: afetado"; portal STF (abaixo): sem tese |
| § 9: AI 8013836-78.2026, 1ª Câmara, julgado em 23/07/2026, aspas | Cognitio `TJBA:acordaos:1709896`: "PRIMEIRA CAMARA CÍVEL · Agravo de Instrumento · 8013836-78.2026.8.05.0000 · [...] 23/07/2026"; ementa: "Estatuto social e decisões administrativas de reconhecimento de imunidade pelo próprio fisco municipal." (literal). Está só em `fontes.json` (registro derivado), não em `dados/decisoes`: "fora do denominador" correto |
| § 12: 443 candidatos do TJBA (2020–2025) | `dados/candidatos-tjba.jsonl`: 9.956 linhas; com "IPTU-04" em `eixos_indicio`: **443**, 443 ids únicos; data_julgamento de 2020 a 2025 (57/52/85/70/73/106); 258 acórdãos e 185 monocráticas; 439 de 2º grau e 4 de turma recursal |
| § 12: composição IPTU-04 (4 fav. TJBA, 2 deles de recíproca; 1 desfav.; 1 sem exame; 2 qualificados fav.) | `piloto-composicao.json`: bate (6 fav. = 4 TJBA + 2 PANGEA; 1 desfav.; 1 sem_exame) |
| § 11: os três acórdãos só com ementa e dispositivo; precedente do STF não identificado | os três registros: `completude: ementa_e_dispositivo`; o texto do [CONTEUDO] repete a ementa e o dispositivo, sem voto |

## 4. Situação atual dos precedentes qualificados (pendência 3 do dossiê)

| Precedente | Espelho BNP (<ACERVO>/PANGEA, 21/07/2026) | Portal STF, lido em 05/11/2026 (WebFetch, nível metadados) | Situação |
|---|---|---|---|
| SV 52 | "APROVADO", atualização em 22/05/2025 | **não alcançado** (`sumariosumulas.asp` deu 400; a URL antiga deu 404) | texto confirmado em dois espelhos (BNP e Cognitio); situação no portal **não conferida**. Amarelo: segue pendente |
| Tema 693 | "Há repercussão geral com reafirmação de Jurisprudência. Leading case: transitado em julgado" (20/06/2024) | RE 767332, Min. Gilmar Mendes; RG reconhecida em 01/11/2013; "Trânsito em Julgado - em 04/12/2013"; a página exibe **também** o rótulo "Em definição" (provável rótulo residual: a reafirmação de jurisprudência e o trânsito constam), e o resumo não trouxe o campo "Tese" | mérito julgado (reafirmação); tese pelo campo TESE do RG no Cognitio; o rótulo "Em definição" deve ser conferido à mão no portal |
| Tema 1398 | "Há repercussão geral. Leading case: afetado" (29/05/2025) | leading case RE 1317330, Min. Dias Toffoli; RG em 17/05/2025; "Acórdão de Repercussão Geral publicado - Publicado em: 23/05/2025"; sem tese | pendente de mérito; "só afetado, sem tese" está correto hoje |

Ressalva: a página do portal passou por um modelo de resumo (WebFetch). Os rótulos acima são os que ele devolveu; antes de citar em peça, confirme abrindo a página.

## 5. O que não foi verificado

- As páginas de Walton, Reed e Macagno (2008) do § 8 (p. 314, 319, 327, 343, 344) e os rótulos `ARG.SCH.WRM08.*` e avaliações do Élenchos estão fora do escopo pedido e não foram conferidos.
- O inteiro teor dos três acórdãos não existe no acervo. Tudo foi conferido só pela ementa e pelo dispositivo, como o dossiê já declara.
- A situação da SV 52 no portal do STF não foi alcançada (§ 4).
- O teor do RE 767.332 RG no Cognitio "termina de forma abrupta no próprio acervo" (aviso do banco). A tese foi conferida pelo campo TESE, que está completo, e pela ementa da p. 1. A íntegra não foi lida.
- As fichas do Atlas usadas (`art-150`, `ali-b`, `ali-c`, `art-156/par-1-A`, `ctn/art-14`) estão com `status: rascunho`. As linhas transcritas (`> `) vêm da captura do compilado do Planalto. Não abri o Planalto diretamente.
- Os metadados de data do TJBA (julgamento = publicação no banco) não foram confrontados com a sessão real, que o texto não data.
- O MIJ não foi feito: o alcance da SV 52 e do Tema 693 para templo e sindicato, e o precedente-pilar 2f27, ficam para ele (pendência 5 do dossiê).
