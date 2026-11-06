---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
alvo: analises/teses/TES-001-imunidade-onus-da-destinacao.md (v4) e analises/fichas/TES-39-imunidade-reciproca-estatais.md (+ .json), lote F7
destino-do-alvo: interno (pesquisa; nada a renderizar nem enviar)
regra: estado/brief-antialucinacao-fichas-v1.md
metodo: conferência manual de cada afirmação contra a fonte própria, no formato do precedente auditoria/antialucinacao-TES-001-v1.md; números recontados por código sobre analises/teses/TES-001-tabela-v1.json (regenerada em 06/11, 10:58) e sobre a fatia TES002_a (tes002_ementas.json, a mesma lida por estado/E4-3/leitores/gen_t39.py); excertos «…» conferidos por código contra evidencias/ e dados/decisoes/; precedentes no Cognitio e nos portais do STF e do Planalto
saida-por-codigo: auditoria/antialucinacao-E43-F7.json (24 entradas; cada `de` conferido por código como trecho único e exato do .md)
---

# Antialucinação: lote F7 (TES-001 v4 e TES-39)

## 1. Veredito

**Nada grave nos dois documentos.** Não há citação inventada nem aspas falsas, e nenhum número muda uma conclusão.

O que foi conferido e bate:
- **Excertos literais:** os 52 trechos entre «…» (28 na TES-001, 24 na TES-39) foram localizados por código, ipsis litteris, nas evidências ou nos registros. Na TES-39, cada excerto está no registro do processo a que a ficha o atribui.
- **TES-001 v4, § 3:**
  - O agregado bate célula a célula com a tabela regenerada.
  - A contagem de 52 favoráveis em 57 processos com ônus no Município (b + c) também bate.
  - O universo é o declarado: 110 processos (41 *b*, 66 *c*, 3 *b*+*c*).
  - As 110 linhas do § 3.1 coincidem com a tabela em órgão, data, alínea, via, matéria, ônus e resultado. A única diferença é a grafia do nome do órgão.
- **Mudanças da v3 para a v4** (frontmatter `revisao`), todas conferidas no registro:
  - Entrou 0503944-29.2016: templo, Diocese, apelação do Município de Juazeiro, ônus do Município, favorável (DEC-TJBA-7e984fa65d9a).
  - 8003270-07.2025 passou a ônus "misto". Os ED do Município foram rejeitados em 25/11/2025 (DEC-TJBA-082c3674043f).
  - As 5 datas de sessão corrigidas batem com `ajustes-conferencia-it.jsonl`.
  - A frase "8 dos 11 pendentes da harmonização" bate com `releitura-h2.jsonl`: são 8 reclassificados e 3 duplicatas (EXC-04).
- **TES-39, camada T3:** a contagem bate.
  - 37 processos: 15 favoráveis, 20 desfavoráveis, 2 sem exame.
  - COELBA: 11 favoráveis, 17 desfavoráveis, 1 sem exame. A sequência por câmara também bate.
  - O JSON bate com o MD: `n_catalogo_fav` = 15, `n_acervo` = 98, e os `contrarias_ids` correspondem exatamente aos 20 processos desfavoráveis.
- **TES-39, camada E:** 130 decisões e 98 processos, sem os 4 de alínea *c*. A tabela por entidade bate (EMBASA 38/23, outras 25/7, CODEBA 21/11, URBIS 8/3, CONDER 4/3, INFRAERO 1/0, CHESF 1/0).
- **TES-39, linhas com "trajetória (releitura H2, 06/11)":** as três batem com os registros que citam.
  - 0500536-61.2015: ED acolhidos em parte em 12/08/2024, e o dispositivo passou de "provido" a "provido em parte" (DEC-TJBA-a320d38f47dc).
  - 8000200-86.2020: ED do Órgão Especial não acolhidos em 25/09/2024 (DEC-TJBA-8dc97d887723).
  - 0303373-71.2014: ED do Órgão Especial não acolhidos em 27/03/2024 (DEC-TJBA-0a49ea9f7548).
- **Temas 1.297 e 1.398 sem tese:** conferido no portal do STF em 06/11/2026.
  - Tema 1.297 (RE 1.479.602): «Acórdão de Repercussão Geral publicado - Publicado em: 16/04/2024», sem tese nem mérito julgado.
  - Tema 1.398 (RE 1.317.330): acórdão de RG publicado em 23/05/2025, sem tese.
  - O pilar da TES-39 ("sem tese: qualquer posição é provisória") continua atual.
- **Precedentes superiores:** as teses dos Temas 385, 437, 508, 644, 693 e 1.140 conferem com o Cognitio. A questão do Tema 1.297, sem tese, confere com o cadastro. Também conferem a Súmula 724/STF e a Súmula 352/STJ. A ementa do AgInt no REsp 1.968.035/RJ confere no inteiro teor. As duas ementas do STF do § 5 da TES-001 são literais em `evidencias/dirigida/stf-portal-2026-11-05.json`.
- **Walton:**
  - TES-001: as avaliações do § 6 são as gravadas em `auditoria/elenchos-TES-001-v3.json` e são coerentes com o que o dossiê mostra.
  - TES-39: WEAK_UNANSWERED_CQ é coerente. A CQ1 depende de precedentes do STF não abertos, e a CQ2 é a exceção do Tema 508, alegada e não rebatida.

**Pontos médios: 2 na TES-001 e 5 na TES-39.** São erros objetivos que não mudam a conclusão:
- **TES-001:** dois números do v3 ficaram sem atualizar depois da entrada de 0503944-29.2016 (A-01, A-02).
- **TES-39:**
  - a "reversão" da EMBASA na 4ª CC tem a direção trocada: a câmara acabou mantendo a imunidade (B-01, B-02);
  - data e órgão do sobrestamento de 8000741-22.2020 (B-03);
  - o RE sobrestado em 8002105-72.2020 é do Município, não da COELBA (B-04);
  - Lei 8.987/1995, art. 14 dado como reversibilidade; o art. 14 trata da licitação (B-05).

| Ficha | Pior gravidade | `[A CONFERIR]` resolvidos | Veredito |
|---|---|---|---|
| TES-001 v4 | médio | 1 de 5 (+1 parcial; 1 não localizado; 2 dependem de inteiro teor do TJBA e estão declarados) | aprovada com correções (aplicar A-01 e A-02) |
| TES-39 | médio | 3 de 7 (+3 só existência, metadados; 1 não localizado) | aprovada com correções (aplicar B-01 a B-05) |

## 2. TES-001 v4: afirmações problemáticas

### A-01: "18 processos de alínea *b* com via exceção e resultado favorável" · **MÉDIO** · conta errada
- **Dossiê** (§ 8, Templo): "(18 processos de alínea *b* com via exceção e resultado favorável, § 3.1)".
- **Fonte:** `TES-001-tabela-v1.json` regenerada, com alínea = b, via = excecao_pre_executividade e resultado = favoravel, dá **19** (20 com os de *b*+*c*). O 19º é 0503944-29.2016, que entrou na v4. O número é o da v3.
- **Texto certo:** "(19 processos de alínea *b* com via exceção e resultado favorável, § 3.1; 20 com os de *b*+*c*)".

### A-02: A1, CQ1 "alínea *b*, 28 com ônus no Município" · **MÉDIO** · conta errada
- **Dossiê** (§ 6, A1): "CQ1 answered (tabela: alínea *b*, 28 com ônus no Município)".
- **Fonte:** o § 3 da própria v4 e a tabela dão `b | municipio | 26 | 2 | 1 | 29`.
- **Texto certo:** "29 com ônus no Município". O status PLAUSIBLE não muda.

### A-03: Remissão errada · **LEVE**
- § 2: "As 5 derrotas da linha minoritária são todas desse tipo (§ 5)." As derrotas estão no **§ 4**.

### A-04: Data de 8009655-12.2018 · **LEVE** · inconsistência interna
- A linha do § 3.1 traz 2020-11-09, e o § 4 diz "04/11/2020 pela Decisão Proclamada".
- A fonte (`evidencias/pdpj/DEC-TJBA-c7e23238cce4/0049-Acórdão.txt`) diz: «DECISÃO PROCLAMADA … Salvador, 4 de Novembro de 2020.» Vale 04/11/2020.
- A correção é no registro (`datas.julgamento`), e a tabela se regenera. Este processo não estava entre as 5 datas corrigidas na v4. No JSON o item vai como `ressalva`: aplicar o `para` só no MD criaria divergência com `TES-001-tabela-v1.json` até o registro ser corrigido.

### A-05: 8003270-07.2025 na "linha minoritária" · **LEVE** · ressalva
- O § 4 tem o título "ônus do contribuinte" e continua listando 8003270-07.2025 como vitória "dentro da linha". Na v4, porém, o ônus desse processo passou a "misto".
- Fica bem como caso de fronteira, mas convém dizer isso.

### A-06: STJ "não aberto" · **LEVE** · ressalva com encaminhamento ao MIJ
- O AgInt no REsp 1.968.035/RJ existe e está no Cognitio com inteiro teor (`STJ:integras:149072561`): STJ, 1ª Turma, Rel. Min. Regina Helena Costa, publ. 30/03/2022. O trecho transcrito no § 4 é literal da ementa, item II.
- O voto vai além: «A Corte Estadual concluiu que cabe à Fazenda Municipal elidir a presunção da entidade sindical, comprovando que ela não preenche os requisitos legais previstos no art. 14 do Código Tributário Nacional. No caso, verifico que o tribunal de origem adotou entendimento consolidado neste Superior Tribunal de Justiça.»
- Isso põe no Fisco também o ônus quanto ao art. 14, o que **tensiona a A4 restrita**: "requisitos do art. 14 por documento".
- Saber o alcance do precedente é juízo do MIJ, não meu (amarelo, `mij: true`).

## 3. TES-39: afirmações problemáticas

### B-01 e B-02: EMBASA na 4ª CC, "sinal de reversão" · **MÉDIO** · contradita (direção do fato)
- **Ficha:**
  - § 1: "e sinal de reversão na 4ª CC em 2025";
  - § 3.6: "Há sinal de reversão também na 4ª CC (0097379-11.2009, 2025; apelação do Município provida e depois embargos de declaração, com efeito a conferir)."
- **Fonte:**
  - DEC-TJBA-433f5ca201c4 (02/2025): a apelação do Município foi provida, com fundamento nos Temas 508 e 1.140.
  - DEC-TJBA-697b4e0f5e10 (06/2025), ementa, item 5: «Embargos de declaração providos para, reformando o acórdão embargado, negar provimento ao recurso apelativo interposto pelo Município de Salvador, mantendo incólume a sentença que reconheceu a imunidade tributária pleiteada pela Empresa Baiana de Águas e Saneamento S/A (Embasa).»
- **Leitura:** o "efeito a conferir" se resolve e inverte o sinal. A 4ª CC terminou **favorável** à EMBASA. A única contrária à EMBASA que resta na camada E é a da 3ª CC (0001957-92.2012).
- **Texto certo:** está em `antialucinacao-E43-F7.json`, itens § 1 e § 3.6.

### B-03: Sobrestamento de 8000741-22.2020 em "17/09/2025" · **MÉDIO** · contradita
- **Ficha** (§ 3.5, Nota): "RE sobrestado pelo Tema 1.297 (17/09/2025)".
- **Fonte:**
  - O sobrestamento é do **Órgão Especial**, em ED no agravo interno, julgado em **16/07/2025** (DEC-TJBA-57e8d3985cfb): «ACOLHER A PRELIMINAR SUSCITADA nos Embargos de Declaração opostos, determinando o sobrestamento do presente feito».
  - 17/09/2025 é a data da decisão da 2ª VP em **outro processo** (0569016-78.2014, DEC-TJBA-1163c83dfbfe).
  - Além disso, o laboratório mostra que o estado mudou depois. Os DJEN 617521669 (22/05/2026) e 623283948 (28/05/2026) registram que a 2ª VP manteve as decisões de inadmissão e remeteu o ARE ao STF e o AREsp ao STJ (AREsp 3.287.644/BA, distribuído em 08/2026).
- **Consequência:** o "sobrestado" pode estar superado, o que toca o § 8 ("pedir o sobrestamento pelo Tema 1.297 nos recursos"). Recomendo reler o processo.

### B-04: "sobrestar os recursos extraordinários da COELBA" · **MÉDIO** · atribuição errada
- **Ficha** (§ 3.2): "A 2ª Vice-Presidência passou, em 2025, a sobrestar os recursos extraordinários da COELBA … :" seguido do excerto de 8002105-72.2020.
- **Fonte:** em 8002105-72.2020 a COELBA venceu. O RE sobrestado é do **Município de Serrolândia**: `DEC-TJBA-d2bdd97aef57.txt` («APELANTE: MUNICIPIO DE SERROLANDIA … APELADO: … COELBA») e DEC-TJBA-67a2551dafc8 («RE do Município»).
- Em 8000244-71.2021 e 0301865-58.2014 o RE é, de fato, da COELBA.
- **Texto certo:** "os recursos extraordinários nos processos da COELBA (no exemplo, o RE é do Município de Serrolândia, vencido em 8002105-72.2020)".

### B-05: "Lei 8.987/1995, art. 14 (reversibilidade)" · **MÉDIO** · citação legal errada
- **Ficha** (§ 2): "**Lei 8.987/1995, art. 14 (reversibilidade) e art. 6º, § 1º (modicidade tarifária):** 0001165-60.2014; 8002321-09.2019;".
- **Fonte (Planalto, l8987cons.htm):**
  - art. 14: «Toda concessão de serviço público, precedida ou não da execução de obra pública, será objeto de prévia licitação…»;
  - a reversão está no art. 35, § 1º («Extinta a concessão, retornam ao poder concedente todos os bens reversíveis…») e no art. 36.
- **Origem do erro:** o acórdão 0001165-60.2014 é que diz «reversível ao poder concedente, conforme art. 14 da Lei nº 8.987/1995» e põe a modicidade no art. 9º, § 3º. A ficha reproduziu a citação do TJBA como fundamento normativo próprio.
- **Texto certo:** está no JSON, item § 2. Ele mantém a voz do TJBA identificada.

### B-06: 8002930-34.2023 sem a trajetória H2 · **LEVE**
- A releitura H2 achou o AI da concessionária **desprovido em 16/05/2023** (DEC-TJBA-fd5f8aeaf0cc). Ele foi revertido pelos ED com efeito infringente de 28/02/2024 (DEC-TJBA-4621b7bf10d8).
- A ficha registra a trajetória em três processos e omite esta. O resultado final da linha (favorável, provisório) está certo.

### B-07: § 3.3 "o STJ devolveu o recurso especial … para conformação" · **LEVE**
- A fonte (DEC-TJBAAPI-ac9aab88f3e5) diz que no **AREsp** 2.957.046/BA o Min. Benedito Gonçalves «determinou o retorno dos autos … a fim de que proceda o sobrestamento da tramitação dos autos até publicação do acórdão paradigma no Tema 1297/STF».
- Foi devolução para sobrestamento, não para conformação.

### B-08: Tema 1.398 · **LEVE** · ressalva (alcance ao MIJ)
- O título no portal do STF confere com a ficha: «Garantia de imunidade tributária para fins de incidência de IPTU em relação a bens imóveis de estatais afetados à prestação de serviço público». O leading case é o RE 1.317.330, e o acórdão de RG foi publicado em 23/05/2025, sem tese.
- A questão, porém, fala de imóvel de **sociedade de economia mista**, «à luz dos artigos 150; VI, "a"; e 155; § 3º». A ficha não traz o leading case.
- A menção ao art. 155, § 3º (energia) sugere caso de energia. Por isso, a frase do § 3.3 de que o Tema 1.398 "está mais próximo da EMBASA e da CODEBA do que da COELBA" é juízo de alcance e vai ao MIJ.

### B-09 a B-12: Leves
- **B-09, Tema 644:** a tese diz «imóveis de sua propriedade **e por ela utilizados**»; a ficha diz só "imóveis próprios".
- **B-10, § 3.6 "Outras":** a ficha lista CHESF e INFRAERO como "outras", mas eles têm linha própria na tabela.
- **B-11, JSON da ficha:**
  - o `formulacao` é a versão anterior ao ajuste do orquestrador no § 1 (JSON de 01:10, MD de 11:00);
  - `precedentes` omite RE 918.700, ARE 947.142 AgR, ADPF 858, RE 1.395.601 AgR, Rcl 70.570 e REsp 1.089.827;
  - `excertos` tem 24 entradas, e `conferencia-fichas-e43.jsonl` registra 23 (diferença não explicada; os 24 conferem nesta rodada).
  - Não entra no JSON de aplicação, porque o `de` tem de ser trecho do MD. Fica para o orquestrador regenerar o JSON.
- **B-12, 8002112-79.2022:** a coluna Data traz a data da apelação desfavorável (2024-04-02) com o resultado dos ED (30/10/2024). A nota explica, mas a data da coluna é a do ato que não prevaleceu.

### Leves sem correção de texto
- 0001957-92.2012 (EMBASA, 3ª CC, "25/11/2024"): a data é o metadado do banco, que rotula o órgão como 2ª VP. O texto é acórdão da 3ª CC.
- Os registros H2 0a49ea9f7548, 8dc97d887723 e fd5f8aeaf0cc estão em `dados/decisoes/`, mas não entram na tabela regenerada. O script só inclui atos com leitura de ônus T3, e esses não têm `onus_tes001`. A ficha os cita por id, o que é legítimo, mas eles não pesam nas contagens.

## 4. Tabela dos `[A CONFERIR]`

### TES-001 v4 (5)
| # | Item | Resultado | Referência |
|---|---|---|---|
| 1 | Desfecho do agravo 8001605-53.2024 (seq. 57 e 58) | limite declarado (inteiro teor do TJBA fora do laboratório) | — |
| 2 | SV 52: situação no portal | `nao_localizado` nesta rodada: o Cognitio devolve a Súmula 52 comum, e o portal deu HTTP 400 | — |
| 3 | Tema 693: rótulo "Em definição" | **confere**: o portal mostra «Há repercussão geral com reafirmação de Jurisprudência», rótulo «Em definição», e «Trânsito em Julgado - em 04/12/2013». A tese confere no Cognitio | portal STF, tema.asp?num=693; `STF:paradigmas-teor:693-4904092` |
| 4 | Precedentes do STJ citados no TJBA | **parcial**: AgInt no REsp 1.968.035/RJ **confere** (teor; ver A-06); Súmula 352/STJ **confere**; REsp 825.496/DF `nao_localizado`; REsp 1.698.305/RJ `nao_localizado` (a busca acha só o EAREsp 1.698.305, penal); AgRg no AREsp 789.362/SP e 105.288/SP não abertos | `STJ:integras:149072561`; `STJ:sumulas:352` |
| 5 | Retratações do Abrigo do Salvador | limite declarado (TJBA) | — |

A Súmula 724/STF, que a ficha marca como "espelho", confere no Cognitio (`STF:sumulas:724`).

### TES-39 (7)
| # | Item | Resultado | Referência |
|---|---|---|---|
| 1 | § 3.1: RE 1.315.581, RE 1.272.751, Rcl 32.717 | existência **confere** (metadados): RE 1.315.581 (Barroso), RE 1.272.751 (Toffoli; há AgR), Rcl 32.717 (Fux; o voto de 8002321-09.2019 a dá a Alexandre de Moraes). Teor não lido | portal STF |
| 2 | § 3.5: ED nos ED de 8000200-86.2020 | **confere** (ementa): acolhidos com efeitos infringentes, à vista do Tema 1.297, para desconstituir a negativa de seguimento do RE. Disponibilizada em 10/07/2025 | `evidencias/djen/DEC-TJBA-8dc97d887723/321762668.json` |
| 3 | § 3.6: Tema 1.140 (URBIS) | **confere** (tese) | `STF:paradigmas-teor:1140-755857209` |
| 4 | § 4: Tema 1.140 | **confere**: RE 1.320.054 (Metrô-SP). É o pilar da formulação para estatais e vai ao MIJ | idem |
| 5 | § 4: RE 1.315.581; RE 1.272.751; Rcl 32.717; RE 918.700; ARE 947.142 AgR; ADPF 858 | existência **confere** (metadados; RE 918.700 Barroso, ARE 947.142 Toffoli com AgR, ADPF 858 Nunes Marques). Teor não lido | portal STF |
| 6 | § 4: RE 1.395.601 AgR; Rcl 70.570 | existência **confere** (metadados; ambos Fachin; há AgR no RE). Teor não lido | portal STF |
| 7 | § 4: STJ REsp 1.089.827/RJ | `nao_localizado`: o Cognitio não tem o documento, e o portal do STJ deu HTTP 403. O TJBA o cita como «Rel. Min. Regina Helena Costa, DJe 13.08.2018» | `DEC-TJBA-c73afa1ef253.txt` |

## 5. O que não foi verificado
- Inteiro teor de qualquer acórdão do STF. As teses e os cadastros foram lidos no Cognitio, e a existência dos processos no portal.
- REsp 1.089.827, REsp 825.496, REsp 1.698.305 e os dois AgRg no AREsp, no portal do STJ (bloqueado, HTTP 403).
- Situação atual da SV 52 no portal. A regra é a mesma da Súmula 724, que confere, mas o enunciado da SV 52 não foi lido nesta rodada.
- Os votos da COELBA no inteiro teor, além dos trechos citados. A ficha declara isso.
- O estado atual dos processos após 05/2026, fora dos DJEN que já estão no laboratório.
