---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
lote: F2 (família F2_sujeicao_passiva)
alvo: analises/fichas/TES-07-sujeicao-passiva-contribuinte (.md/.json), TES-23-desapropriacao-imissao-na-posse (.md/.json), TES-25-promitente-comprador-sem-posse (.md/.json)
pacote: estado/E4-3/pacote-F2_sujeicao_passiva.json
destino-do-alvo: interno (pesquisa; nada a renderizar, nada a enviar)
metodo: conferência manual de cada afirmação contra a fonte própria (brief-antialucinacao-fichas-v1; precedente antialucinacao-TES-001-v1). Não usei o pipeline `conferidor`: o destino é interno e o formato pedido é trecho, fonte e gravidade.
---

# Antialucinação: lote F2 (TES-07, TES-23, TES-25)

## 1. Veredito

| Ficha | Pior gravidade | `[A CONFERIR]` resolvidos | Veredito |
|---|---|---|---|
| TES-07 | **médio** (1) + 13 itens leves (A-02 a A-14) | 6 de 9 (7 marcas, duas delas com dois itens cada) | Sem nada grave. Corrigir a contagem de ruído da API e aplicar as leves. |
| TES-23 | leve (11 itens no JSON, B-01 a B-11) | 2 de 3 | Sem nada grave nem médio. Ajustes de paráfrase e inferência. |
| TES-25 | leve (6 itens, C-01 a C-06), um deles de alcance (MIJ) com peso real | 0 de 2 (1 não localizado, com análogo civil achado; 1 é limite declarado) | Sem nada grave nem médio. O ponto do STJ sobre a "promessa irretratável" deve ir ao MIJ antes de a tese ser usada. |

**Comum às três fichas.** Nenhuma citação inventada e nenhuma aspa falsa. Cada `«...»` do `.md` está no pacote, sob o número de processo a que a ficha o atribui (cruzamento por código: 0 divergências). Bate também cada câmara e data de julgamento ou publicação citada, com duas exceções: o órgão de 8016415-67.2024 e o de 0562941-23.2014. Nos dois casos o pacote registra outro órgão, e a ficha aponta isso de forma correta e declarada. Os números do acervo, do DJEN e da API, e as contagens por câmara e período, batem com o pacote. A única exceção é a da TES-07 (A-01). Precedentes superiores conferidos no teor ou na tese: Tema 122, Tema 1.158, AgInt no REsp 1.950.739, Súmulas 392, 393 e 399, Tema 166, Temas 385, 437 e 1.184 do STF. Os espelhos do AREsp 3.117.209 e do REsp 2.201.074 também foram conferidos, mas têm a ementa cortada no próprio acervo.

**Ressalva transversal (leve, nas três).** Várias paráfrases trazem fato ou consequência que o excerto não contém. Exemplos: "honorários pela causalidade" e "Rendeu certidão positiva com efeitos de negativa" (TES-23), "O negócio tinha sido anulado" (TES-25) e "(imóvel arrematado por terceiro)" (TES-07). Elas vêm do campo `tese` do catálogo, que é um registro derivado da triagem e não a fonte. Isso serve para achar, não para conferir. Há mais dois avisos. Nos itens da 2ª Vice-Presidência, o excerto pode ser a ementa do acórdão recorrido, transcrita na decisão de admissibilidade (voz alheia). E a "data de julgamento" do catálogo é metadado do banco: nos registros abertos em `dados/candidatos-tjba.jsonl`, `data_julgamento` = `data_publicacao`. Proposta: uma frase no § 7 de cada ficha (itens A-14, B-11 e C-06 deste relatório; no JSON, os três itens com `local` = "§ 7, Só ementa").

## 2. TES-07 · Sujeição passiva: quem é o contribuinte

### A-01 · Ruído da API · **MÉDIO** · contagem errada
- **Ficha** (§ 7): "239 itens brutos, 6 no pacote, dois deles ruído; não serve de denominador."
- **Fonte**: pacote, `teses[n=7].tjba_api.itens`, 6 itens: 0169983-43.2004, 0140628-22.2003, 8052083-67.2022, 8032337-36.2021, 0795758-25.2015 e 8003270-57.2023. A própria ficha (§ 3) classifica 0169983 e 8003270 como "Favoráveis fora do catálogo (API)", 8052083, 8032337 e 0795758 como contrárias, e só 0140628 como ruído ("0140628-22.2003 (só prescrição)"). Os outros três itens de ruído do § 3 (0385814, 0001188 e 0005995) vêm da amostra do acervo, não da API.
- **Texto certo**: "um deles ruído (0140628-22.2003)". A conclusão não muda.

### A-02 · Súmula 399 atribuída a três contrárias · leve · atribuição
- **Ficha** (§ 2): "Tema 122 e Súmula 399 do STJ: invocados nas contrárias (8016415-67.2024; 8006413-09.2022; 8032337-36.2021)."
- **Fonte**: 8016415 «TEMA REPETITIVO N° 122. LEI MUNICIPAL 1.039/2009»; 8032337 «TEMA 122 DO STJ»; 8006413 «SÚMULA N.º399 E TEMA N.º122 DO STJ». A 399 aparece só em 8006413.

### A-03 · "com título registrado" no item 2 · leve · generalização
- **Ficha** (§ 3, item 2): "Deixou de ser dono antes do fato gerador, com título registrado (venda, arrematação, desmembramento)."
- **Fonte**: só 0795600 («contrato particular devidamente registrado em cartório») e 0102383 («escritura pública registrada») falam em registro. Os outros três não falam: 8001312 («NÃO DETÉM MAIS A POSSE»), 8001892 («INSCRIÇÃO JÁ HAVIA SIDO CANCELADA EM RAZÃO DO DESMEMBRAMENTO») e 8002358 («ACORDO JUDICIAL QUE SE REVELA COMO DOCUMENTO HÁBIL»). O título geral diz mais do que três dos cinco excertos sustentam.

### A-04 · 0314008 dentro de "Proprietário que perdeu a posse" · leve · classificação
- **Ficha** (§ 3, item 4): "Proprietário que perdeu a posse (invasão, ocupação, bem público, imóvel demolido)."
- **Fonte**: 0314008 «BEM DE DOMÍNIO PÚBLICO. INOCORRÊNCIA DA POSSE PELO EMBARGANTE. IMÓVEL DEMOLIDO». Se o bem é de domínio público, o embargante não era proprietário. O caso é de ausência de posse e de propriedade, não de perda da posse pelo dono.

### A-05 · Construtora até a entrega · leve · `[A CONFERIR]` resolvido: **diverge**
- **Ficha** (§ 3, item 5): "O excerto não mostra se a regra veio de lei municipal ou do contrato `[A CONFERIR]`."
- **Fonte**: inteiro teor no acervo, `<ACERVO>/JURISPRUDÊNCIAS-TJBA/2025/acordaos-2025-07.jsonl`, processo 8065774-83.2024.8.05.0000 (busca por número, só leitura): «III – Segundo a jurisprudência do Superior Tribunal de Justiça, as despesas de IPTU são de responsabilidade da construtora até a entrega do imóvel ao adquirente, de modo que afigura-se correto impor ao Município, in casu, que autorize a transferência do bem controvertido para a titularidade do exequente, independentemente da quitação dos débitos tributários pretéritos, que devem permanecer vinculados ao CNPJ da parte executada.» Cabeçalho: «DIREITO DO CONSUMIDOR, TRIBUTÁRIO E PROCESSUAL CIVIL. CUMPRIMENTO DE SENTENÇA. RELAÇÃO DE CONSUMO SUBJACENTE».
- **Leitura**: a regra não vem de lei municipal nem do contrato. Vem da jurisprudência do STJ, que o acórdão não identifica, num cumprimento de sentença de consumo (atraso na entrega da obra). O Município aparece como agravante, obrigado a transferir o cadastro. Como precedente de sujeição passiva em execução fiscal, o caso é periférico.

### A-06 · Homonímia em 8003270 · leve · paráfrase ambígua
- **Ficha**: "Exceção acolhida por homonímia (o CNPJ executado era outro)."
- **Fonte**: «acolheu exceção de pré-executividade oposta por Vila Rica Empreendimentos Imobiliários Ltda. (CNPJ [CNPJ omitido]), reconheceu sua ilegitimidade passiva decorrente de homonímia, indeferiu a substituição do polo passivo para incluir Vila Rica Imobiliária Ltda. (CNPJ [CNPJ omitido])».
- **Leitura**: a executada não era a devedora, e o Município não pôde trocar o polo para outra pessoa jurídica. Do jeito que está, "o CNPJ executado era outro" pode ser lido ao contrário.

### A-07 · AgInt no REsp 1.950.739 × favorável 0795600 · leve · alcance (amarelo, **MIJ**)
- **Ficha** (§ 4): "Os favoráveis do item 2 tratam de escritura ou contrato translativo registrado, não de promessa; a distinção tem de ser feita na peça."
- **Fonte**: Cognitio `STJ:integras:151559969` (teor). Ementa: «ORIENTAÇÃO QUE SE APLICA ÀS HIPÓTESES EM QUE O CONTRATO DE COMPRA E VENDA FOI DEVIDAMENTE REGISTRADO EM CARTÓRIO». Relatório: «ainda que o compromisso seja registrado em cartório». O voto cita o REsp 1.849.545/SP: «a existência de contrato de compromisso de compra e venda de imóvel, com transferência imediata da posse, ainda que acompanhada de registro no cartório imobiliário, não afasta a responsabilidade tributária do alienante». O favorável 0795600 (inteiro teor em acervo local, `acordaos-2025-08.jsonl`) diz: «CONTRATO PARTICULAR DE COMPRA E VENDA REGISTRADO EM CARTÓRIO ANTES DOS FATOS GERADORES – ART. 34 DO CTN» e «PROPRIEDADE E POSSE JÁ TRANSFERIDAS».
- **Leitura**: a leitura da ficha (compromisso registrado) tem apoio no relatório. Mas a letra da ementa do STJ ("contrato de compra e venda registrado") se choca com a letra do 0795600 ("contrato particular de compra e venda registrado"). Na peça, é preciso mostrar que o título registrado era translativo, não compromisso, e citar o relatório e o voto, não só a ementa. A conclusão fica para o MIJ.

### A-08 · Argumento de Walton: "possuidor com ânimo de dono" atribuído ao art. 34 · leve · paráfrase de lei
- **Ficha** (§ 6): "o art. 34 do CTN define o contribuinte do IPTU como proprietário, titular do domínio útil ou possuidor com ânimo de dono;"
- **Fonte**: o art. 34, como o STJ o transcreve, diz «o proprietário do imóvel, o titular do seu domínio útil ou o seu possuidor a qualquer título» (REsp 1.111.202, ementa, item 1). A exigência de ânimo de dono vem da jurisprudência: «Especificamente em relação ao possuidor, conforme a interativa jurisprudência deste Superior Tribunal de Justiça, a posse deverá ser qualificada pelo animus domini» (REsp 1.982.001, Tema 1.158, ementa, item III). O § 2 da própria ficha diz certo ("possuidor a qualquer título").

### A-09 · Temas 385 e 437 do STF · leve · `[A CONFERIR]` resolvido: **confere**, com aviso de alcance (MIJ)
- **Fonte**: Cognitio `STF:repercussao_geral:tema-385` (RE 594.015): «A imunidade recíproca, prevista no art. 150, VI, a, da Constituição não se estende a empresa privada arrendatária de imóvel público, quando seja ela exploradora de atividade econômica com fins lucrativos. Nessa hipótese é constitucional a cobrança do IPTU pelo Município.» `STF:repercussao_geral:tema-437` (RE 601.720): «Incide o IPTU, considerado imóvel de pessoa jurídica de direito público cedido a pessoa jurídica de direito privado, devedora do tributo.»
- **Leitura**: "imunidade recíproca e concessionária" é uma paráfrase aceitável. Os dois temas, porém, vão **contra** o item 3 ("posse sem ânimo de dono": arrendatário) quando o imóvel é público: lá, a arrendatária ou cessionária privada é a devedora. Os favoráveis do item 3 tratam de imóvel de entidade filantrópica (privado), o que os distingue, mas a ficha deveria dizer isso. Os temas reforçam o "Quando não usar: concessionária".

### A-10 · REsp 940.942/RJ e Tema 166 · leve · `[A CONFERIR]` resolvido em parte
- **Tema 166: confere.** Cognitio `STJ:paradigmas:Tema-166`, leading case REsp 1.045.472, rel. Min. Luiz Fux, 2009. Tese: «A Fazenda Pública pode substituir a certidão de dívida ativa (CDA) até a prolação da sentença de embargos, quando se tratar de correção de erro material ou formal, vedada a modificação do sujeito passivo da execução.» É o mesmo texto da Súmula 392 (o sha256 é igual nos dois registros).
- **REsp 940.942/RJ: não localizado.** O Basanos dá "fora do índice", com 1 citante no acervo. Existe um HC 940.942, processo diverso: não confundir. O portal do STJ (scon) devolveu 403. Fora do índice não prova inexistência.

### A-11 · Tema 1.184 do STF · leve · `[A CONFERIR]` resolvido: **confere**
- **Fonte**: Cognitio `STF:repercussao_geral:tema-1184` (RE 1.355.208): «1. É legítima a extinção de execução fiscal de baixo valor pela ausência de interesse de agir tendo em vista o princípio constitucional da eficiência administrativa, respeitada a competência constitucional de cada ente federado. [...]» A ficha está certa: o tema não trata de sujeição passiva.

### A-12 · Dispositivos da LEF em 8008076 · leve · `[A CONFERIR]` resolvido: **confere**
- **Fonte**: inteiro teor em acervo local, `acordaos-2025-04.jsonl`, processo 8008076-49.2020.8.05.0004: «4. Contudo, o art. 2º, §5º, I, da mesma lei, estabelece que o Termo de Inscrição da Dívida Ativa deverá conter "o nome do devedor, dos co-responsáveis e, sempre que conhecido, o domicílio ou residência de um e de outros". 5. No mesmo sentido, o art. 202, I, do CTN [...]» e «Dispositivos relevantes citados: Lei nº 6.830/80, arts. 2º, §5º, I, e 6º; CTN, art. 202, I». O texto da LEF bate com o Cognitio (`lei-6830-1980-lef-art-2`).

### A-13 · Proprietário esbulhado no STJ · leve · `[A CONFERIR]`: **não localizado**
- A busca temática no Cognitio (06/11/2026) foi exploratória e não achou correspondência confiável. Fica como está, com o registro de que se buscou.

### A-14 · Transversal (§ 7) · leve · ressalva (ver § 1)

**Limite declarado, sem ação**: o fundamento da contrária 8052083-67.2022 está cortado no pacote. É uma publicação de 10/2026, fora dos arquivos de acervo local, e a ficha declara isso.

**Walton (TES-07)**: PLAUSIBLE é coerente. A CQ1 vem respondida com recorte e a CQ2 está aberta, com o ônus em quem questiona. A-08 é só de redação.

## 3. TES-23 · Desapropriação ou imissão na posse

### B-01 · 0317285: "o resto caiu por prescrição" · leve · omissão que distorce
- **Ficha** (§ 3): "Favorável **em parte**: a ilegitimidade só valeu para um exercício (...); o resto caiu por prescrição."
- **Fonte** (API, 0317285-56.2016): «PRELIMINAR ACOLHIDA COM RELAÇÃO AO EXERCÍCIO DE 2000. [...] RECONHECIMENTO DA PRESCRIÇÃO DIRETA EM RELAÇÃO A TODO CRÉDITO TRIBUTÁRIO OBJETO DA AÇÃO. MANUTENÇÃO DA SENTENÇA EM SUA INTEIREZA.»
- **Leitura**: a prescrição cobriu **todo** o crédito, inclusive 2000.

### B-02 · CQ1: "Onde a prova cobria só um exercício" · leve · inferência
- **Ficha** (§ 6, CQ1): "Onde a prova cobria só um exercício, a regra valeu só para ele (0317285-56.2016)."
- **Fonte**: a ementa diz só «configurada está a ilegitimidade passiva do Embargante em relação ao exercício do IPTU do ano 2000». Ela não diz por quê, nem que a prova se limitava a esse exercício.

### B-03 · Objeção do registro "rejeitada em 8000043" · leve · atribuição
- **Ficha** (§ 3): "A objeção do Município (só o registro transfere) aparece no DJEN e é rejeitada em 8000043-09.2025 («ainda que sem registro formal da propriedade»)." Também na CQ2: "O TJBA a afastou (8000043-09.2025 [...]; DJEN 8037526-12.2021)".
- **Fonte**: a objeção do Município está no DJEN (1º grau, 8037526: «sustenta que somente há transferência de titularidade mediante o registro no cartório competente»). O excerto de 8000043 afirma a regra contrária, mas não mostra que o Município a tenha levantado ali. E o DJEN é decisão de 1º grau, que a própria ficha deixa "fora da conta".

### B-04 · 0022673: "O executado não alegou imissão" · leve · ausência inferida de texto cortado
- **Fonte** (API): «AUSÊNCIA DE PEDIDO ADMINISTRATIVO DE COMPENSAÇÃO DE DÉBITOS FISCAIS COM CRÉDITOS ORIUNDOS DE DESAPROPRIAÇÃO AMIGÁVEL DE IMÓVEL.» e «Termo de Acordo de fl. 19, na data de 17/04/2009». O trecho não trata da imissão nem a exclui. O correto é "o trecho não mostra", não "não alegou".

### B-05 · DJEN 8037526 "exceção [...] acolhida" · leve · dispositivo fora do trecho
- **Fonte**: o texto do pacote termina na transcrição de um aresto («Comportamento contraditório da Muni»). A fundamentação acolhe («não sendo possível pretender a tributação em tela»), mas o dispositivo não está no trecho.

### B-06 · AREsp 3.117.209: resultado do caso · leve · alcance (MIJ)
- **Fonte**: Cognitio `STJ:espelhos:959011` (espelho; ementa cortada no acervo): «AQUISIÇÃO ORIGINÁRIA E FRUIÇÃO DA PROPRIEDADE. RESPONSABILIDADE TRIBUTÁRIA PROPORCIONAL. PRECEDENTES. AGRAVO CONHECIDO PARA CONHECER EM PARTE DO RECURSO ESPECIAL E, NESSA EXTENSÃO, DAR-LHE PROVIMENTO.» O Diákrisis classifica o caso como "Decisão PROCESSUAL — não enfrenta o mérito", com barreira **parcial**.
- **Leitura**: a citação do item 3 está literal. O espelho, porém, não diz quem recorreu nem a quem o provimento favoreceu. "Proporcional" pode ter sido a favor do Município, no exercício da imissão. Também é interpretação da ficha que a "aquisição originária" seja "o que separa a desapropriação do regime de registro do Tema 122" (MIJ).

### B-07 · Formulação: "por acordo" · leve · generalização
- **Ficha** (§ 1): "Se o imóvel foi desapropriado (por decreto e ação, por acordo ou por apossamento indireto)".
- **Fonte**: nenhum favorável do pacote é desapropriação amigável. A única amigável é a contrária 0022673 («DESAPROPRIAÇÃO AMIGÁVEL»), que trata de compensação. "Por acordo" não tem caso de apoio no pacote.

### B-08 · Item 2, § 2 · `[A CONFERIR]` resolvido: **confere**
- Uma busca por código em todo o bloco `teses[n=23]` do pacote não acha "art. 34" nem "3.365". O único dispositivo do CTN é «INCIDÊNCIA DO ART. 32 DO CTN» (0239834, análogo civil). O DL 3.365/1941, art. 34, está no REsp 2.201.074 (`STJ:espelhos:957895`): «tal ônus recai sobre o expropriado somente até ao momento da imissão na posse pela entidade expropriante», como a ficha diz.

### B-09 · "Nenhum tema repetitivo ou súmula" · `[A CONFERIR]` resolvido: **confere** (no acervo)
- A busca no Cognitio em 06/11/2026 ("IPTU desapropriação imissão na posse expropriado responsabilidade tributária", STJ) trouxe os dois espelhos da ficha, o cadastro do Tema 1.158 (alienação fiduciária) e o REsp 2.142.066 (Segunda Turma, 2024, levantamento de indenização). Nenhum tema ou súmula específico. A ausência no acervo não é ausência no ordenamento.

### B-10 · REsp 1.291.828 · `[A CONFERIR]`: **não localizado**
- O Basanos dá "fora do índice", com 0 citantes; só o espelho do AREsp 3.117.209 o menciona. O portal do STJ devolveu 403.

### B-11 · Transversal (§ 7) · leve · ressalva (ver § 1)

**Conferido e sustentado** (além do cruzamento do § 1): REsp 2.201.074 (Primeira Turma, 2026, rel. Min. Sérgio Kukina; espelho cortado); AREsp 3.117.209 (Segunda Turma, 2026, rel. Min. Teodoro Silva Santos), item 3 literal; 0795148 com «artigo 156, I, da Constituição Federal», «art. 373, II, do CPC/2015» e os decretos 11.004, 11.006 e 14.199/2012; 0022673 com o art. 22 da Lei Municipal 7.186/2006 e o Decreto 19.251; DJEN 8037526 com o Decreto Municipal 24.849/2014; as 9 decisões do catálogo nas câmaras e no período (11/02/2020 a 12/11/2025); 417/498/32 e 385 = 417 − 32.

**Walton (TES-23)**: PLAUSIBLE é coerente. CQ1 e CQ2 estão respondidas, e a CQ3 está aberta, com o ônus em quem questiona. A resposta da CQ2 ganharia precisão com B-03 e B-06.

## 4. TES-25 · Promitente comprador sem posse

### C-01 · AgInt no REsp 1.950.739 "neutro para o comprador sem posse" · leve · alcance (amarelo, **MIJ**; o ponto mais relevante do lote)
- **Ficha** (§ 4): "Contra o vendedor; neutro para o comprador sem posse."
- **Fonte**: Cognitio `STJ:integras:151559969`. O voto, sob "Ainda sobre o tema", cita um julgado (a identificação está cortada no acervo) com a ementa «DIREITO REAL. CONTRATO DE COMPRA E VENDA REGISTRADO EM CARTÓRIO. APLICABILIDADE.» e o item «II - O art. 34 do Código Tributário Nacional, ao apontar como contribuinte do IPTU o possuidor a qualquer título, engloba também a relação de direito real advinda do contrato de promessa de compra e venda irretratável».
- **Leitura**: o texto não é neutro para a tese. Se a "posse a qualquer título" abrange o **direito real** do compromissário (promessa irretratável), o comprador pode ser contribuinte sem posse física. É exatamente o contrário do gancho da formulação ("o Tema 122 do STJ só o alcança como 'possuidor a qualquer título'"). O texto é de julgado citado dentro do voto (lugar a conferir), não a ementa do AgInt. Vai ao MIJ antes de qualquer uso. Na Walton, é um undercut não tratado (CQ1).

### C-02 · Análogos civis: "o IPTU anterior à imissão na posse é da construtora" · leve · generalização
- **Fonte**: 0007391 («COBRANÇA DE TAXAS DE IPTU ANTES DA IMISSÃO DA PROMITENTE COMPRADORA NA POSSE») e 0505388 («restituição de taxas condominiais e IPTU cobrados antes da imissão na posse») sustentam. Mas 0500829 («ATRASO NA ENTREGA DO EMPREENDIMENTO. CULPA EXCLUSIVA DAS RÉS») e 0562941 («AÇÃO DE RESCISÃO CONTRATUAL [...] RESCISÃO DO CONTRATO [...] TAXA CONDOMINIAL, IPTU E ITIV. RESTITUIÇÃO DOS VALORES ADIMPLIDOS») ligam a restituição ao atraso e à rescisão, não à imissão.

### C-03 · Regra do registro: "o artigo do CC não aparece no trecho" · leve · resolvido de passagem
- **Fonte**: o trecho de 0795758 («A propriedade de bens imóveis transfere-se entre vivos mediante o registro do título translativo») reproduz o CC, art. 1.245, caput (Cognitio `lei-10406-2002-cc-art-1245`, texto compilado do Planalto, status DRAFT): «Art. 1.245. Transfere-se entre vivos a propriedade mediante o registro do título translativo no Registro de Imóveis.» Na mesma família, 8016429 cita o artigo pelo número (TES-07).

### C-04 · STJ sobre o comprador sem posse · `[A CONFERIR]`: **não localizado** em tributário; achado lateral
- A busca no Cognitio (06/11/2026) não trouxe acórdão tributário específico. Achado lateral, análogo civil da mesma família da Súmula 183 do TJPE: o **Tema 886 do STJ** (REsp 1.345.331/RS, Segunda Seção, 08/04/2015; `STJ:paradigmas-teor:201201992764-1396734`): «a) O que define a responsabilidade pelo pagamento das obrigações condominiais não é o registro do compromisso de compra e venda, mas a relação jurídica material com o imóvel, representada pela imissão na posse pelo promissário comprador e pela ciência inequívoca do condomínio acerca da transação.» **Ressalva:** há uma proposta de revisão do tema (REsp 2.100.395, Segunda Seção, 2025, `STJ:espelhos:000911776`), na linha da «legitimidade passiva concorrente entre promitente vendedor (proprietário) e promitente comprador». Entra como sugestão, não como correção.

### C-05 · Walton: "Sem exceções abertas" · leve · ressalva
- PLAUSIBLE é defensável com o que a ficha mostra, e a própria ficha chama a CQ3 de "fina". Com o C-01 (o direito real da promessa irretratável dentro de "a qualquer título"), a CQ1 tem um contra-argumento não tratado. "Sem exceções abertas" é otimista, e WEAK estaria a um passo.

### C-06 · Transversal (§ 7) · leve · ressalva (ver § 1)

**Limite declarado, sem ação**: a lei municipal que prevê o processo administrativo de renúncia da posse (0504009) não foi lida, e a ficha declara isso nos §§ 2 e 7.

**Conferido e sustentado**: Tema 122 (PANGEA `stj-rr-122`, "Transitado em julgado", tese literal; teor `STJ:paradigmas-teor:200900091426-892440`: Primeira Seção, 10/06/2009, DJe 18/06/2009); Súmula 399; Súmula 393 («A exceção de pré-executividade é admissível na execução fiscal relativamente às matérias conhecíveis de ofício que não demandem dilação probatória.») e Súmula 392 em 8012566 («SÚMULA 393 DO STJ» e «SÚMULA 392 DO STJ»); Tema 1.158, citação literal (item III); Súmula 183 do TJPE (PANGEA, literal); as três contrárias e a "Favorável de outra tese" 8029000; os 4 do catálogo (Terceira 3, Segunda 1; 11/02/2020 a 04/09/2024); 805/939/36 e 769 = 805 − 36.

## 5. Tabela dos `[A CONFERIR]`

| Ficha | Linha | Item | Resultado | Referência certa / texto da fonte |
|---|---|---|---|---|
| TES-07 | 28 | Dispositivos da LEF em 8008076 | **confere** | LEF, arts. 2º, § 5º, I, e 6º; CTN, art. 202, I (inteiro teor, acervo local) |
| TES-07 | 62 | Construtora: lei municipal ou contrato? | **diverge** | nem um nem outro: «Segundo a jurisprudência do Superior Tribunal de Justiça [...]» (inteiro teor, acervo local) |
| TES-07 | 78 | Fundamento de 8052083 | limite declarado | publicação de 10/2026, fora de acervo local; a ficha declara |
| TES-07 | 98 | STJ sobre o esbulhado | não localizado | busca exploratória no Cognitio |
| TES-07 | 99 | REsp 940.942/RJ | não localizado | fora do índice (Basanos); STJ 403 |
| TES-07 | 99 | Tema 166 do STJ | **confere** | REsp 1.045.472, rel. Luiz Fux, 2009; tese = Súmula 392 |
| TES-07 | 100 | Tema 1.184 do STF | **confere** | RE 1.355.208; execução fiscal de baixo valor |
| TES-07 | 101 | Tema 385 do STF | **confere** | RE 594.015; arrendatária privada de imóvel público paga IPTU |
| TES-07 | 101 | Tema 437 do STF | **confere** | RE 601.720; cessionária privada de imóvel público é devedora |
| TES-23 | 24 | CTN 34 e DL 3.365 nos excertos do TJBA | **confere** | ausentes do pacote (busca por código) |
| TES-23 | 67 | Tema ou súmula específicos | **confere** (no acervo) | nenhum; ausência no acervo ≠ ausência no ordenamento |
| TES-23 | 70 | REsp 1.291.828 | não localizado | fora do índice; STJ 403 |
| TES-25 | 24 | Lei municipal da renúncia da posse | limite declarado | não alcançável; a ficha declara |
| TES-25 | 67 | STJ sobre o comprador sem posse | não localizado (tributário) | análogo civil: Tema 886 (REsp 1.345.331/RS), em revisão |

## 6. Situação dos precedentes superiores e nível de evidência

| Precedente | Fonte lida | Nível | Situação |
|---|---|---|---|
| Tema 122 STJ (REsp 1.111.202/SP) | `STJ:paradigmas-teor:200900091426-892440`; PANGEA `stj-rr-122` | inteiro teor (p. 1 a 2) + tese | Primeira Seção, 10/06/2009, DJe 18/06/2009; "Transitado em julgado" (PANGEA, 28/08/2024) |
| Tema 1.158 STJ (REsp 1.982.001) | `STJ:integras:301232701` | teor (ementa e relatório) | Primeira Seção; publicação 19/03/2025; tese literal. O cadastro do tema traz como leading case o REsp 1.949.182 (outro recurso afetado; não é erro) |
| AgInt no REsp 1.950.739 | `STJ:integras:151559969` | teor | Segunda Turma; sessão virtual de 19 a 25/04/2022; publicação 04/05/2022; rel. Min. Og Fernandes |
| Súmulas 392, 393 e 399 STJ | `STJ:sumulas:*` | enunciado | textos conferidos |
| Tema 166 STJ | `STJ:paradigmas:Tema-166` | cadastro (tese) | REsp 1.045.472, Luiz Fux, 2009 |
| AREsp 3.117.209 | `STJ:espelhos:959011` | espelho, ementa cortada no acervo | barreira parcial (Súmula 211); resultado desconhecido |
| REsp 2.201.074 | `STJ:espelhos:957895` | espelho, ementa cortada | barreira parcial (Súmula 284/STF) |
| Temas 385, 437 e 1.184 STF | `STF:repercussao_geral:tema-*` | cadastro (tese) | textos conferidos |
| Súmula 183 TJPE | PANGEA `tjpe-sum-183` | enunciado | "Vigente" (PANGEA, 10/07/2025) |
| Tema 886 STJ (lateral) | `STJ:paradigmas-teor:201201992764-1396734` | teor (p. 1) | Segunda Seção, 08/04/2015; proposta de revisão em 2025 |

Basanos (`basanos_verificar_citacoes`, 15 citações): 12 "existe"; REsp 940.942 e REsp 1.291.828 deram "fora do índice". O "tribunal diverge" do REsp 1.045.472 é um artefato do meu texto de teste, não da ficha.

## 7. O que não foi verificado

- O inteiro teor dos acórdãos do TJBA, salvo três que abri no acervo acervo local só por busca de número: 0795600 (art. 34 do CTN, confirmado), 8008076 e 8065774. Os demais foram conferidos só pelo excerto e pela ementa do pacote, como as fichas declaram.
- O portal do STJ (scon) devolveu 403: REsp 940.942/RJ e REsp 1.291.828 não foram alcançados.
- A vigência atual dos precedentes: o Cognitio avisa que o acervo não prova vigência. O PANGEA dá a situação na data da captura.
- Nenhuma lei municipal foi lida (Camaçari, Lei 1.039/2009; o CTRM de Salvador; os decretos expropriatórios).
- Os textos legais (CC, art. 1.245; LEF, art. 2º) vêm do compilado do Planalto no Cognitio (status DRAFT), e não abri o Planalto diretamente.
- As páginas de Walton, Reed e Macagno (2008) e os rótulos `ARG.SCH.WRM08.*` não foram conferidos. Avaliei só a coerência entre PLAUSIBLE e o que a ficha mostra.
- O MIJ não foi feito. Ficam para ele: A-07, A-09, B-06 e C-01.
- Não editei as fichas. Os JSONs das fichas foram lidos, e os campos `precedentes`, `contrarias_ids` e `excertos` batem com os `.md`. Na TES-07, `excertos` tem 35 entradas (0169983 aparece duas vezes, com dois trechos).
