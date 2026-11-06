---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
lote: E4-3 / F1a
alvo: analises/fichas/TES-04, TES-10, TES-11, TES-12, TES-13, TES-15 (.md e .json, draft de 06/11/2026)
pacote: estado/E4-3/pacote-F1a_execucao_processo.json
destino-do-alvo: interno (pesquisa; nada a renderizar nem enviar)
metodo: conferência manual contra a fonte própria (brief estado/brief-antialucinacao-fichas-v1.md; formato do precedente auditoria/antialucinacao-TES-001-v1.md)
saida-por-codigo: auditoria/antialucinacao-E43-F1a.json (26 itens; todo "de" conferido por código como trecho único e exato da ficha)
---

# Antialucinação: fichas E4-3, lote F1a

## 1. Veredito

**Nenhum achado grave nas seis fichas.** Nenhuma citação inventada e nenhuma aspa falsa. Todas as súmulas e teses do STJ e do STF transcritas na ficha batem letra por letra com o Cognitio (teor do campo `tese` ou do enunciado). As três íntegras do STJ marcadas como lidas também batem: Turma, data e trecho.

Na camada mecânica, um script cruzou cada linha com «citação» contra o pacote: 150 linhas (38 + 14 + 32 + 24 + 24 + 18, o mesmo número de excertos dos JSON), todas com número, data e trecho batendo. Duas acusaram câmara diferente do campo `orgao` do pacote (TES-11, 0323034 e 8030962), mas a própria ficha já diz que o acórdão da câmara está transcrito numa decisão da 2ª Vice-Presidência, e o texto confirma. As contagens de catálogo e acervo de cada ficha batem com o pacote e com o JSON da ficha.

O único **médio** está na TES-12. A ficha afirma que há divergência entre câmaras sobre o pagamento feito ao ente incompetente (Lauro de Freitas). A divergência existe, mas a ficha a apoia em dois processos que não a mostram (8014830 e 8006689). O que mostra é o 8055358-56.2024, da Primeira Câmara, que a ficha lista em outro lugar com outro trecho. O resto são ressalvas leves.

| Ficha | Pior gravidade | `[A CONFERIR]` resolvidos | Veredito |
|---|---|---|---|
| TES-04 | leve | 1 de 1 | segue; 1 ressalva |
| TES-10 | leve | 2 de 3 | segue; 2 ressalvas (Tema 1.184 não está truncado; Tema 1.428 é risco, não apoio) |
| TES-11 | leve | 1 de 1 | segue; 2 ressalvas |
| TES-12 | **médio** | 0 de 1 | segue com correção do apoio da "divergência" (§ 3) |
| TES-13 | leve | 1 de 2 | segue; 6 ressalvas pontuais |
| TES-15 | nenhum | 3 de 3 | segue |

## 2. Afirmações problemáticas

### TES-12

**A-12-01 · MÉDIO · atribuição errada de apoio (a conclusão fica de pé, os processos citados não a sustentam)**
- **Ficha** (§ 3, "O que distingue e o conflito em aberto"): "a Segunda Câmara nega efeito liberatório ao pagamento feito a Lauro de Freitas, enquanto a Primeira (8014830-49.2023) e a Quarta Câmaras (8006689-46.2020) protegeram o pagamento de boa-fé. Há divergência entre Câmaras sobre o efeito do pagamento ao ente incompetente."
- **Fonte** (ementas no acervo acervo local, pelos ponteiros de `dados/candidatos-tjba.jsonl`):
  - 8014830-49.2023 (`acordaos-2024-05.jsonl:1398`): "APELANTE: MUNICIPIO DE LAURO DE FREITAS [...] EMBARGOS À EXECUÇÃO [...] DOCUMENTAÇÃO EXISTENTE NOS AUTOS QUE MILITA EM FAVOR DA COBRANÇA PELO MUNICÍPIO DO SALVADOR. TEORIA DA APARÊNCIA. [...] VALIDADE DE PAGAMENTO EFETUADO." Quem perde é Lauro de Freitas, e a ementa não diz a quem se pagou.
  - 8006689-46.2020 (`acordaos-2024-10.jsonl:1577`): "AÇÃO DE REPETIÇÃO DE INDÉBITO TRIBUTÁRIO RELATIVO A IPTU [...] DOCUMENTAÇÃO EXISTENTE NOS AUTOS QUE APONTA PELA COMPETÊNCIA DO MUNICÍPIO DO SALVADOR [...] APELAÇÃO DO MUNICÍPIO DE LAURO DE FREITAS A QUE SE NEGA PROVIMENTO." É repetição contra o ente incompetente: o pagamento a ele é devolvido, não é tratado como liberatório.
  - 8055358-56.2024 (`acordaos-2024-11.jsonl:33838`; Primeira Câmara, 28/11/2024; "AGRAVADO: MUNICIPIO DE SALVADOR"): "**PAGAMENTO AO MUNICÍPIO DE LAURO DE FREITAS. TEORIA DA APARÊNCIA. INEXISTÊNCIA DE DOLO OU CULPA DA EXECUTADA. BOA FÉ DA CONTRIBUINTE. VALIDADE DE PAGAMENTO EFETUADO.** [...] AGRAVO DE INSTRUMENTO CONHECIDO E PROVIDO."
- **Leitura:** 8055358 é o espelho exato de 8045606-89.2026. Nos dois, Salvador executa e a contribuinte pagou a Lauro de Freitas. A Primeira Câmara (2024) validou o pagamento; a Segunda Câmara (2026) negou efeito liberatório. A divergência é real e é esta. A ficha cita 8055358 no subgrupo *b* só com a frase "É inconcebível que o contribuinte seja surpreendido...", e põe no lugar dele dois casos em que o vencido é Lauro de Freitas. O § 8 ("contra a cobrança de Salvador, o pagamento feito a Lauro de Freitas pode não liberar (2026)") e o risco "alto na disputa territorial" continuam corretos. O texto certo do apoio está no JSON.
- O alcance (qual linha prevalece) é questão para o MIJ, não para esta conferência.

**A-12-02 · LEVE · generalização.** Título do subgrupo *b*: "Salvador × Lauro de Freitas, Loteamento Marisol (10 processos)". Das 10 ementas, 6 nomeiam o Marisol (8000306, 8000188, 8001288, 8017356, 8008497, 8055358); as de 8004329, 8014830, 8006689 e 8008748 não. A disputa é a mesma (Salvador × Lauro); só o rótulo generaliza.

### TES-04

**A-04-01 · LEVE · generalização.** § 3: "Ausência de qualquer vínculo com o imóvel, provada por certidão registral (2): 0170321-17.2004, 8030976-84.2023." Só 8030976 fala em certidão ("certidão do cartório competente que atesta a inexistência de registro imobiliário"). O excerto de 0170321 diz só «Inexistência de relação jurídica de propriedade entre o apelado. Ilegitimidade passiva configurada.»

### TES-10

**A-10-01 · LEVE · declaração desatualizada.** § 4, Tema 1.184: "(item 1 da tese; o restante está truncado no acervo)". O campo `tese` de `STF:repercussao_geral:tema-1184` traz 731 caracteres, com os itens 2 (conciliação ou solução administrativa e protesto prévios) e 3. O item 1 transcrito está literal.

**A-10-02 · LEVE · alcance de precedente (amarelo, MIJ).** § 6, CQ2: "as decisões de 2026 apoiam a distinção na eficiência (Temas 1.184 e 1.428 do STF)". É o que as ementas do TJBA dizem (8000948-69.2020: "PRINCÍPIO CONSTITUCIONAL DA EFICIÊNCIA (ART. 37, CAPUT, DA CF/1988 E TEMAS 1.184 E 1.428 DO STF)"). Mas o Tema 1.428 (ARE 1.553.607) está pendente e sem tese, e a questão dele é "se a utilização dos parâmetros da Resolução CNJ nº 547/2024 para aferição de interesse de agir em execução fiscal viola a separação de poderes e a competência tributária do ente federativo, na hipótese de lei local fixar critérios diversos". É risco em aberto para a própria base normativa da distinção (art. 1º-A da Res. 547), e não apoio já firmado. O § 8 ("a distinção ainda não passou pelo STJ") deveria somar esse risco do lado do STF.

### TES-11

**A-11-01 · LEVE · paráfrase que amplia.** § 4, rótulo do Tema 375: "(confissão em parcelamento não convalida vício de fato)". A tese diz o contrário como regra e só abre exceção: "Quanto aos aspectos fáticos [...] a regra é que não se pode rever judicialmente a confissão de dívida efetuada com o escopo de obter parcelamento [...]. No entanto [...] a matéria de fato constante de confissão de dívida pode ser invalidada quando ocorre defeito causador de nulidade do ato jurídico (v.g. erro, dolo, simulação e fraude)." A primeira frase, transcrita na mesma célula, está literal.

**A-11-02 · LEVE · inconsistência interna.** "**As contrárias e o que as distingue (7 processos de IPTU).**" Logo abaixo, a ficha diz que em 8030962-15.2024 "o tributo não aparece no excerto". O texto do pacote confirma: é decisão da 2ª Vice-Presidência que reproduz acórdão da Segunda Câmara sobre "PLANILHA DE CÁLCULO", sem IPTU no trecho.

### TES-13

**A-13-01 · LEVE · dispositivo.** Formulação: "(o espólio só se representa pelo inventariante ou administrador, art. 75, VII, do CPC)". O art. 75, VII, diz "o espólio, pelo inventariante;". O administrador provisório está no art. 614 ("O administrador provisório representa ativa e passivamente o espólio").

**A-13-02 · LEVE · data.** § 3: "a API chega a 29/09/2026". No pacote, a `tjba_api` da TES-13 inclui 0500978-96.2014, publicado em 2026-10-06 (é a homonímia da TES-04, que entrou pela busca "falecido").

**A-13-03 · LEVE · paráfrase com inferência (três lugares: § 2, § 3 e CQ2).** "aqui aplicou o art. 6º da LEF". A ementa de 8136168-20.2021 diz só "PETIÇÃO INICIAL QUE CUMPRE OS REQUISITOS DE LEI". Nem o pacote nem o acervo acervo local (texto de ementa e dispositivo, `acordaos-2024-04.jsonl:32051`) nomeiam o art. 6º. A leitura é plausível, mas não está escrita.

**A-13-04 · LEVE · metadado tratado como fato.** "Primeira Câmara Cível, 2021 (acórdão reproduzido em decisão da 2ª Vice-Presidência de 20/09/2021; ...)". O texto (pacote e acervo local) é o próprio acórdão da Primeira Câmara, com "Sala das Sessões," e sem data e sem nenhuma decisão da Vice-Presidência em volta. "2ª Vice-Presidência, 20/09/2021" é só o `orgao` e a data do banco (o problema conhecido de metadado do TJBA). "Extinção mantida, honorários afastados" está sustentado ("RECURSO PROVIDO. SENTENÇA REFORMADA, EM PARTE", com honorários "INADMISSIBILIDADE").

### TES-15

Nada a apontar. Conferidos e sustentados: art. 487, III, "a" (é a alínea que as próprias decisões citam: 8004549 e 8011503); art. 151, VI, e art. 922 (8011503); gratuidade "de ofício" (8011503); Tema 1.413 citado em 8006324; Súmula 409 e Tema 980 citados juntos em 8005537 ("Em igual acepção"); Lei 9.306/17 de Salvador (0531268); Itabuna (comarca 0113); quatro dos oito favoráveis são tutela; DJEN com 1 item (revisional de aluguel).

## 3. Conferido e sustentado (verde), por amostra relevante

| Afirmação | Fonte e verificação |
|---|---|
| Súmulas 112, 392, 393, 397 e 558 do STJ (texto entre aspas) | Cognitio `STJ:sumulas:*`: idênticas; Basanos: `existe_no_indice` para as cinco |
| Temas 108, 122 (com o "2-cabe à legislação municipal..."), 166, 248, 375 (texto integral na TES-15), 421, 702, 876 e 980 do STJ | Cognitio `STJ:precedentes:Tema-*`, campo `tese`: idênticos. Os Temas 108 e 702 aparecem na TES-04 só pela primeira frase, e o corte não muda o sentido |
| Tema 166 = REsp 1.045.472/BA; Tema 876 = REsp 1.455.091/AM | Basanos: `STJ:paradigmas:Tema-166` / `STJ:paradigmas-teor:201401188624-1365117` |
| Tema 1.184/STF, item 1 | `STF:repercussao_geral:tema-1184`: literal |
| AgInt no AREsp 2.659.697: Primeira Turma, publicado em 12/06/2025, trecho entre aspas | `STJ:integras:318751505`: "PRIMEIRA TURMA [...] Sessão Virtual de 03/06/2025 a 09/06/2025"; "Publicação: 2025-06-12"; trecho literal |
| REsp 2.216.800 diz o mesmo e tem barreira de não conhecimento | `STJ:integras:342853494`: Segunda Turma, 27/10/2025; cita o AREsp 2.659.697 como "Primeira Turma, julgado em 9/6/2025, DJEN de 12/6/2025"; o Diákrisis marca `nao_conhecimento` |
| Controvérsia 657/STJ (pendente), trecho entre aspas | PANGEA `stj-ct-657` no pacote: literal |
| IRDR 9/TJPR, trecho entre aspas | PANGEA `tjpr-irdr-9` no pacote: literal |
| TES-04: 8072682 tem a mesma agravante e o mesmo Município de 8071811 | as duas ementas: "AGRAVANTE: DALVA DIONISIO MENEZES [...] AGRAVADO: MUNICIPIO DE PORTO SEGURO" |
| TES-04: art. 90, § 4º, invocado e afastado (8003270); homonímia entre pessoas jurídicas | "ART. 90, § 4º, DO CPC. INAPLICABILIDADE"; "Vila Rica Empreendimentos Imobiliários Ltda. [...] Vila Rica Imobiliária Ltda." |
| TES-04: "As contrárias de 2025 dizem que, sem registro, a matéria pede dilação" | 8071811: "A alegação de ilegitimidade passiva demanda dilação probatória"; 8072682: "NECESSIDADE DE DILAÇÃO PROBATÓRIA" |
| TES-10: art. 1º-A da Res. CNJ 547/2024 (redação da Res. 617/2025) e Consulta CNJ 0004754-38.2025 citados nas decisões | 8000948-69.2020 e 0502387-05.2017 (ementas, API): literais |
| TES-10: 8041504 é rescisória do Município julgada improcedente; 8016313, recurso do Município provido; 8001170, sentença anulada | ementas da amostra |
| TES-11: 8010848 é da Quarta Câmara (o `orgao` do pacote diz 2ª Vice) e cita o art. 83 da Lei 7.186/2006 de Salvador | texto: "Quarta Câmara Cível [...] AGRAVADO: MUNICIPIO DE SALVADOR [...] ART. 83 DA LEI nº 7.186/2006" |
| TES-11: arts. 32, § 1º, e 148 do CTN alegados no DJEN 8074595; art. 293-B, § 3º, de Salvador em 0300084 | trechos do pacote |
| TES-12: MS nº 439 e acordo com intermediação do MP | 8004329 (acervo local): "SANADA PELO MANDADO DE SEGURANÇA Nº 439"; 8000188: "ACORDO ENTRE OS MUNICÍPIOS COM INTERMEDIAÇÃO DO MINISTÉRIO PÚBLICO" |
| TES-12: 8045606 tem Salvador executando e a executada que pagou a Lauro de Freitas | ementa (API): "execução fiscal ajuizada pelo Município de Salvador [...] pagamentos efetuados ao Município de Lauro de Freitas" |
| TES-13: 8001369 (morte em 2005; IPTU de 2015-2016; art. 6º do CC) | API: "faleceu em 2005 [...] (IPTU de 2015 e 2016)"; "(art. 6º do CC)" |
| Contagens: catálogo, acervo e contrárias de cada ficha | pacote: 25/522/138 (TES-04), 6/87/53 (TES-10), 21/76/24 (TES-11), 18/92/26 (TES-12), 18/385/85 (TES-13), 8/679/181 (TES-15); `contrarias_ids` dos JSON: 6, 2, 7, 3, 2, 7, iguais às listas das fichas; subgrupos da TES-04 (11+2+1+11=25) e da TES-12 (8+10=18) |
| Períodos e câmaras do catálogo | datas mínima e máxima e órgãos do pacote batem nas seis fichas (exceção: A-13-02, que é da API) |

## 4. Itens `[A CONFERIR]`

| Ficha | Item | Resultado | Referência certa (nível de evidência) |
|---|---|---|---|
| TES-04 | REsp 2.116.283 (aplica Súmula 392 e Tema 166) | **confere** | `STJ:integras:333440766` (teor): Segunda Turma, publicado em 08/09/2025, rel. Min. Afrânio Vilela; "A indicação equivocada do sujeito passivo na CDA não constitui mero erro formal ou material, mas sim vício que inquina o título executivo". Ressalva: taxa de limpeza pública contra órgão da União sem personalidade jurídica, não IPTU |
| TES-10 | Tema 1.428/STF | **confere** (existe; pendente) | `STF:repercussao_geral:tema-1428` (cadastro): ARE 1.553.607; questão transcrita em A-10-02; sem tese |
| TES-10 | Tema 1.201/STJ (multa do art. 1.021, § 4º) | **confere** | `STJ:precedentes:Tema-1201` (tese): o agravo contra decisão baseada em precedente qualificado autoriza a multa, salvo distinção ou superação alegada com fundamento |
| TES-10 | Res. CNJ 547/2024, art. 1º-A (Res. 617/2025) e Consulta CNJ 0004754-38.2025 | **nao_localizado** | atos.cnj.jus.br devolveu 403; o Cognitio não tem resoluções do CNJ. Só a citação nas ementas do TJBA (registro derivado: serve para achar, não para conferir) |
| TES-11 | Regra do STJ: nulidade da CDA exige prejuízo | **confere (não qualificada)** | AgInt no AREsp 1.854.930 (`STJ:integras:193026273`, Primeira Turma, 16/06/2023; Súmulas 284/STF, 7 e 83/STJ); a frase vem do REsp 812.282/MA, reproduzido no AREsp 1.992.315 (`STJ:integras:162490967`). Nenhum repetitivo nem súmula localizado |
| TES-12 | Precedente do STJ sobre pagamento a ente incompetente ou bitributação municipal de IPTU | **nao_localizado** | busca no Cognitio (STJ): `partial_coverage`, só ISS e royalties. Ausência no acervo não é ausência no ordenamento |
| TES-13 | Tema 703/STJ | **confere** | `STJ:pangea:stj-rr-703` (cadastro): "constitui mera irregularidade, sanável [...] não viola a orientação fixada pela Súmula 392"; Tema 702 conferido no campo `tese` |
| TES-13 | IRDR 9/TJPR | **nao_localizado em fonte primária** | texto literal no PANGEA ("Transitado em julgado", 27/05/2024); portal do TJPR não aberto. Mesmo nível que a ficha já declarava |
| TES-15 | Tema 1.413/STJ | **confere** | `STJ:precedentes:Tema-1413`: questão "condenação do contribuinte ao pagamento de honorários [...] quitação extrajudicial do débito após o ajuizamento [...] mas antes de sua efetiva citação"; tese: "*Aguardando a publicação do acórdão do julgamento de mérito." |
| TES-15 | Súmula 409/STJ (dois lugares: § 2 e § 4) | **confere** | `STJ:sumulas:409`: "Em execução fiscal, a prescrição ocorrida antes da propositura da ação pode ser decretada de ofício (art. 219, § 5º, do CPC)." |
| TES-15 | Repetitivo sobre honorários na adesão ao parcelamento (0531268) | **confere (por conteúdo)** | Tema 400/STJ (`STJ:precedentes:Tema-400`): desistência dos embargos para aderir a parcelamento, honorários = bis in idem (encargo do DL 1.025/69). O TJBA o aplica "por analogia" e não dá o número; a identificação é por correspondência de conteúdo |

Limite declarado e confirmado nas seis fichas: inteiro teor do TJBA não lido; DJEN só desde cerca de 2024; API subconta; 1º grau ausente; lei municipal não lida.

## 5. Walton

| Ficha | Status | Coerência com o que a ficha mostra |
|---|---|---|
| TES-04 | PLAUSIBLE | coerente: a CQ1 aponta casos com registro presentes na lista; a CQ2 (Temas 702/703) é respondida pela própria tese do 702 ("a massa falida tem exclusivamente personalidade judiciária") |
| TES-10 | WEAK_UNANSWERED_CQ | coerente: a CQ1 está pendente de verdade (nenhuma decisão do STJ admite a distinção); A-10-02 reforça |
| TES-11 | PLAUSIBLE | coerente: as CQ1 e CQ2 apontam casos que estão na ficha (0501232, 8001009, 8016361, 0502098); CQ3 em aberto e declarada |
| TES-12 | WEAK_UNANSWERED_CQ | coerente: a CQ3 (desmembramento; pagamento ao ente incompetente) não é rebatida no material. Com A-12-01, a divergência fica mais nítida, não menos |
| TES-13 | WEAK_UNANSWERED_CQ | coerente: a CQ2 (8136168 e Controvérsia 657) segue pendente; ajustar a redação conforme A-13-03 |
| TES-15 | PLAUSIBLE | coerente, com observação: a CQ2 é "respondida pelo recorte do argumento" (vale só para a causa de suspensão presente e o crédito que ela abrange). Restringir o alcance é resposta legítima a uma pergunta de conflito de regra; não é vício |

As páginas de Walton, Reed e Macagno (2008) e os rótulos `ARG.SCH.WRM08.*` não foram conferidos (fora do escopo, como no precedente).

## 6. O que não foi verificado

- Inteiro teor dos julgados do TJBA. No acervo acervo local, o `conteudo` dos casos abertos (8014830, 8006689, 8055358, 8004329, 8136168, 0807782 e as ementas do subgrupo Marisol) é só ementa e dispositivo, sem voto.
- Os excertos do TJBA já tinham sido conferidos por código como literais (`conferencia-fichas-e43.jsonl`, 602/602) e não foram reconferidos. Aqui conferi paráfrase, número, câmara, data e contagem.
- Detalhes que estão além do trecho do pacote (truncado em 1.500 caracteres) e não foram procurados: "gleba loteada em 1.275 lotes" (TES-12, 8008966) e o "trecho cortado no pacote" de 8030962 (TES-11).
- Resolução CNJ 547/2024 e 617/2025 e Consulta CNJ 0004754-38.2025: portal fora do alcance (403).
- Portais do STF, do STJ e do TJPR não abertos. Situação atual dos temas pelo cadastro do Cognitio (que não prova vigência: "O acervo não prova vigência atual").
- Os dispositivos de lei foram conferidos no Cognitio (texto compilado do Planalto, status DRAFT) só onde houve dúvida (CPC, arts. 75 e 614). Os demais (CTN, arts. 34, 130, 135, 202, 203 e 204; LEF, art. 2º, §§ 5º, 6º e 8º; CPC, arts. 321, 485 e 922) foram aceitos pela citação literal nas ementas do TJBA, não pela lei.
- O alcance dos precedentes (Tema 1.428 contra a distinção do CPF; qual linha prevalece na disputa Salvador × Lauro; Tema 400 por analogia ao IPTU municipal) fica para o MIJ.
