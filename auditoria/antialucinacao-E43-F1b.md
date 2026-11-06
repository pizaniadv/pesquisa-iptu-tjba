---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
lote: F1b (execução e processo)
alvo: analises/fichas/TES-16, TES-18, TES-24, TES-34, TES-36, TES-37 (.md e .json, draft de 06/11/2026)
pacote: estado/E4-3/pacote-F1b_execucao_processo.json
destino-do-alvo: interno (pesquisa; nada a renderizar nem enviar)
metodo: conferência manual de cada afirmação contra a fonte própria (pacote, JSON da ficha, ementas do laboratório, Cognitio, PANGEA); não o pipeline `conferidor` (destino interno, formato do precedente TES-001)
saida-por-codigo: auditoria/antialucinacao-E43-F1b.json (43 itens; cada `de` conferido por código como substring única da ficha)
---

# Antialucinação: lote F1b da E4-3

## 1. Veredito por ficha

| Ficha | Pior gravidade | [A CONFERIR] resolvidos | Veredito |
|---|---|---|---|
| TES-16 dano moral por protesto | **médio** (3) | 5 de 5 | Nada inventado. Mas a ficha toma o rótulo "2ª Vice-Presidência" do banco como se fosse o órgão, e daí tira um risco ("admissibilidade ≠ adesão") que o texto desmente: os cinco são acórdãos de mérito de Câmara. Também diz "o único valor conhecido é R$ 2.000", e a ementa mostra R$ 6.000 e R$ 35.000. A tese sai **mais forte** do que a ficha diz. |
| TES-18 extinção por pagamento | leve | 5 de 5 | Contagens e excertos batem. Ajustes: paráfrase do art. 26 da LEF, rótulo 2ª VP, ementa "idêntica" que é quase idêntica, Tema 365 conferido pela ementa (a tese cadastrada é outra). |
| TES-24 competência ou foro | leve | 2 de 3 | Sem erro. A lei de organização judiciária do TJBA não foi localizada (limite). Ressalva no Walton. |
| TES-34 menor onerosidade | leve | 5 de 5 | Sem erro de fato. O caso 8064523 (Quinta Câmara, 2026), que estava "truncado", é **favorável** à URBIS. Dois dos seis favoráveis são de pessoa natural, e a ficha não registra isso. |
| TES-36 decisão surpresa | leve | 3 de 3 | Sem erro. O único favorável (0511072) foi apelação do **executado**: o [A CONFERIR] se resolve a favor do contribuinte. |
| TES-37 gratuidade do executado | leve | 2 de 2 | Sem erro grave. "Falta de patrimônio" no § 1 não está na ementa de 8029728. O REsp 1.487.772/SE é de Turma, não repetitivo. |

**Nada grave no lote.** Não há citação inexistente, aspas falsas nem número que mude a conclusão. Os 602 excertos já tinham sido conferidos por código. Aqui conferi a paráfrase, o órgão, a data, as contagens e os precedentes superiores.

## 2. Afirmações problemáticas

### TES-16

**A-01: Órgão dos cinco favoráveis "da 2ª Vice-Presidência".** **MÉDIO**, erro de fato (atribuição errada de órgão), vermelho pelo contrato por ser contradição objetiva.
- Ficha, § 3: "2ª Vice-Presidência (5: provavelmente decisões de admissibilidade de recurso que transcrevem o acórdão favorável, ver Limites)". A mesma ficha rotula cada item como "(2ª Vice-Presidência, data)".
- Fonte: `derivados/ementas-candidatos.jsonl`, conferida na linha crua do acervo (`<ACERVO>/JURISPRUDÊNCIAS-TJBA/2020/acordaos-2020-09.jsonl:16052`: `orgaoJulgador` "2ª VICE-PRESIDÊNCIA" e, na ementa, "Órgão Julgador: Segunda Câmara Cível"). Na face de cada texto:
  - 0529503-06.2014: "ACORDAM os Desembargadores integrantes da Segunda Câmara Cível, à unanimidade, Conhecer e NEGAR PROVIMENTO ao Recurso de Apelação do Réu";
  - 8001087-62.2020: Terceira Câmara Cível, "CONHECER E NEGAR PROVIMENTO À APELAÇÃO";
  - 0505335-84.2017: Terceira Câmara Cível, "conhecer e negar provimento ao recurso";
  - 0500482-32.2017: Primeira Câmara Cível, "NEGAR PROVIMENTO AO RECURSO";
  - 8015030-26.2020: Segunda Câmara Cível, "NEGAR PROVIMENTO AO RECURSO".
- Texto certo: Primeira Câmara (2), Segunda (4), Terceira (2), Sexta Turma Recursal (1). São todos acórdãos de órgão fracionário, não decisões de admissibilidade (8003186 é agravo contra tutela). O rótulo "2ª VP" é metadado do banco. É a mesma armadilha já registrada para o TJBA: o metadado do banco não é a face do acórdão.
- Gravidade média, não grave: a conclusão da tese continua de pé (fica até mais forte). O erro recai no § 7 e no § 8 (A-02, A-03).

**A-02: § 7, "Admissibilidade ≠ adesão: conferir os acórdãos de origem [A CONFERIR]".** **MÉDIO**, [A CONFERIR] resolvido.- Os textos do laboratório já são os acórdãos de origem (A-01). Não há decisão de admissibilidade entre os nove favoráveis. Pelo contraste, as três decisões da 2ª VP na TES-34 (8013496, 8000428, 8002424) são, de fato, decisões de admissibilidade de REsp ("Trata-se de recurso especial interposto..."), e aquela ficha as tratou corretamente.

**A-03: § 8, "Risco: valor modesto (o único conhecido é R$ 2.000). [...] a maior parte dos favoráveis é da 2ª Vice-Presidência."** **MÉDIO**, erro de fato na conclusão de risco.
- Fonte (ementas do laboratório):
  - 0529503: "reconhecendo o direito à indenização por dano moral em favor da Autora/Apelada no valor de R$ 35.000,00(trinta e cinco mil reais)";
  - 0505335: "não se verifica desproporcionalidade ou excessividade no valor de R$ 6.000,00 (seis mil reais)";
  - 8008537: "DANOS MORAIS CONFIGURADOS E BEM SOPESADOS NO VALOR DE R$2.000,00".
- Por que médio, e não grave: o número muda a avaliação de risco ("valor modesto"), mas não a conclusão sobre a tese. O § 7 (1º item) repete o mesmo erro (leve, mesmo fato).

**A-04: Fundamento normativo [A CONFERIR] (CF, art. 37, § 6º; CTN, art. 151).** Leve, resolvido.
- 8001087: "A responsabilidade civil do apelante é objetiva, nos termos do artigo 37, § 6º, da Constituição Federal." 0529503: "RESPONSABILIDADE OBJETIVA. CONSTITUIÇÃO FEDERAL."
- O art. 151, II, do CTN ("o depósito do seu montante integral") é o fundamento material de 8125564 e 8003186, mas o artigo não é citado nas ementas.

**A-05: DJEN.** Leve. "2ª Vara do Sistema dos Juizados da Fazenda Pública": a fonte diz "2ª VARA DO SISTEMA DOS JUIZADOS **ESPECIAIS** DA FAZENDA PÚBLICA".

### TES-18

**B-01: LEF, art. 26.** Leve, paráfrase de lei.
- Ficha: "LEF, art. 26: extinção sem ônus quando o débito é pago antes da citação".
- Lei: "Se, antes da decisão de primeira instância, a inscrição de Divida Ativa for, a qualquer título, cancelada, a execução fiscal será extinta, sem qualquer ônus para as partes."
- Quem leva o artigo ao pagamento anterior à citação é o acórdão 0502110 (Quinta Câmara: "Por força do art. 26 da Lei n.º 6.830/88 [...] por ter sido pago o débito fiscal antes da citação"). A ficha atribui à lei o que é aplicação do tribunal. O cabeçalho "como aparece no pacote" atenua.

**B-02: Rótulo "2ª Vice-Presidência".** Leve. Mesma armadilha de A-01: 0502110 é da Quinta Câmara e 0502524 da Segunda, ambos acórdãos de mérito. Aqui não sustenta nenhuma conclusão.

**B-03: "A ementa é idêntica à de 0757529-64.2013".** Leve. O núcleo é idêntico, mas o cabeçalho difere ("DIREITO TRIBUTÁRIO E PROCESSUAL CIVIL. RECURSO DE APELAÇÃO." × "APELAÇÃO CÍVEL."). A contagem separada está correta.

**B-04: 0562331-21.2015, classificação duvidosa [A CONFERIR].** Resolvido.
- Fonte: "APELANTE: MUNICIPIO DE SALVADOR" e "CONHECER E NEGAR PROVIMENTO AO RECURSO"; "A alegação posterior de insuficiência do depósito configura comportamento contraditório (venire contra factum proprium)".
- A direção é favorável ao contribuinte, e o rótulo "desfavoravel" do catálogo está errado. Mas a questão é outra (anulatória com desistência; conversão em renda, CTN, art. 156, VI), e a ficha acerta ao deixar o caso fora da contagem.

**B-05: Tema 365.** Leve, conferido com ressalva.
- A paráfrase da ficha ("a suspensão posterior ao ajuizamento só obsta o curso da execução, não a extingue") é fiel à **ementa**, item 8: "a suspensão da exigibilidade do crédito tributário, perfectibilizada após a propositura da ação, ostenta o condão somente de obstar o curso do feito executivo e não de extingui-lo".
- A **tese cadastrada** do Tema 365 é outra: "A produção do efeito suspensivo da exigibilidade do crédito tributário, advindo do parcelamento, condiciona-se à homologação expressa ou tácita do pedido formulado pelo contribuinte junto ao Fisco." Citar como "tese do Tema 365" o trecho da ementa seria recorte. A ficha deve dizer que o trecho é da ementa do REsp 957.509.

**B-06: Fonte do Tema 1012.** Leve. A ficha indica "PANGEA `stj-rr-1012`", mas esse registro está no pacote da tese 34, não no da 18. O conteúdo confere.

### TES-24

**C-01: Walton, CQ1 "não respondida".** Leve, ressalva.
- O argumento posto (causa sobre valor venal → tributária → vara fiscal) tem a CQ1 respondida por 0555415 ("MATÉRIA COM EVIDENTE REPERCUSSÃO NA ESFERA TRIBUTÁRIA").
- O que falta é proveito para o contribuinte. O `WEAK_UNANSWERED_CQ` mede utilidade, não correção da classificação. A conclusão do § 8 (rebaixar a tese) continua certa.

### TES-34

**D-01: 8064523-93.2025 "resultado truncado" [A CONFERIR].** Resolvido: favorável.
- Fonte (`evidencias/dirigida/tjba-api-e43-2026-11-06.json`): "Recurso conhecido e provido para reformar a decisão e admitir a penhora sobre o imóvel indicado, afastando a constrição sobre ativos financeiros." Tese: "É cabível a mitigação da ordem legal de penhora em favor de bem imóvel quando demonstrada a grave crise financeira de estatal em liquidação extrajudicial [...]".
- Consequência: em 2026 a Quinta Câmara admitiu a substituição à URBIS, e a Terceira e a Quarta a negaram. O § 8 deve dizer isso (leve).

**D-02: "Na API, as Quarta e Quinta Câmaras, em 2026".** Leve. Na API estão também a Segunda (8009423) e a Terceira (8042647).

**D-03: § 7, "a generalização para a pessoa natural comum é fraca".** Leve, ressalva.
- Dois dos seis favoráveis do catálogo são de pessoa natural: 8018463 (agravante pessoa física; "VALOR VENAL SUPERIOR AO VALOR DA DÍVIDA") e 8021542 (agravante pessoa física; "DOENÇA GRAVE QUE ACOMETE A SUA ESPOSA").
- A frase sobre a API está certa. A frase geral omite os dois casos.

**D-04: 0305467-39.2018 sob "faltou prova (Tema 578)".** Leve.
- É apelação em embargos da URBIS, e a ementa diz "TEMA 578 STJ. INAPLICABILIDADE". O fundamento foi a ineficácia do meio. A ficha, de todo modo, já prevê "ou o imóvel foi tido como meio ineficaz".

### TES-36

**E-01: 0511072-36.2018 "não se sabe quem apelou" [A CONFERIR].** Resolvido.
- Fonte: "APELANTE: ANTONIO CARLOS DE JESUS AMORIM [...] APELADO: FEIRA DE SANTANA PREFEITURA"; "SENTENÇA ANULADA. APELO PROVIDO."
- Foi o executado que apelou e obteve a anulação. A ficha deve corrigir o § 3 e o § 7. Isso dá à CQ1 do uso ofensivo um caso real, mas o status `WEAK_UNANSWERED_CQ` continua coerente, porque a CQ3 segue aberta.

**E-02: "AgInt no REsp 1.755.008".** Leve. O nome exato é "AgInt nos EDcl no Recurso Especial nº 1.755.008 - PR" (Quarta Turma, Rel. Raul Araújo, publicado em 01/02/2021). Ver a tabela da seção 3.

### TES-37

**F-01: § 1, "Comprovada a hipossuficiência e a falta de patrimônio".** Leve, generalização.
- Fonte (8029728): "considerando que a parte Apelante é hipossuficiente [...] ainda que, não lhe desonere de garantir o juízo, o simples fato do amparo da assistência judiciária gratuita da justiça"; o caso tinha "Termo de Confissão e Assunção de Dívida" adimplido; invoca "REsp 1.487.772-SE".
- "Falta de patrimônio" não está no texto. A exigência de "prova inequívoca" vem do Tema 260 e do TJSC IAC 28, não deste acórdão.

## 3. Tabela dos [A CONFERIR]

| Ficha | Item | Resultado | Referência certa / texto da fonte | Nível |
|---|---|---|---|---|
| 16 | CF 37 § 6º; CTN 151 | **confere** | 8001087 cita o art. 37, § 6º, literalmente; o CTN 151, II, é o fundamento material de 8125564 e 8003186 | ementa TJBA |
| 16 | ADI 5135 | **confere** | "O protesto das Certidões de Dívida Ativa constitui mecanismo constitucional e legítimo [...] não constituir sanção política." O Basanos dá `fora_do_indice` (o índice não é o universo) | tese e ementa (espelho BNP) |
| 16 | Controvérsia 30/STJ | **confere** | "Possibilidade ou não de protesto de CDA pela Fazenda Pública"; "Controvérsia vinculada ao tema do STJ" | metadados |
| 16 | TJES IRDR 10; TJRJ IAC 8 | **confere** (tema) | IRDR 10 "Não admitido", sem tese; IAC 8 com mérito publicado, mas a tese **não localizada** | metadados |
| 16 | 2ª VP: acórdãos de origem | **confere / diverge da ficha** | Os textos já são os acórdãos de Câmara (A-01, A-02) | ementa TJBA + linha crua <ACERVO>/ |
| 18 | 0562331, direção | **diverge do catálogo** | Favorável ao contribuinte (Município desprovido); outra questão | ementa TJBA |
| 18 | Tema 365 | **confere** (ementa) | REsp 957.509/RS, Primeira Seção, DJe 25/08/2010; a tese cadastrada é a da homologação (B-05) | teor |
| 18 | Tema 400 | **confere** | Leading case REsp 1.143.320; tese do bis in idem com o encargo do DL 1.025/69 | tese |
| 18 | Tema 1012 | **confere** | Leading case REsp 1.756.406 | tese |
| 18 | Ct 532; TJPR IRDR 31 | **confere** | Honorários na extinção por prescrição intercorrente | enunciado |
| 24 | Lei de organização judiciária / resolução TJBA | **nao_localizado** | Fora do Cognitio; limite declarado pela ficha | — |
| 24 | CPC 46 § 5º | **confere** | "A execução fiscal será proposta no foro de domicílio do réu, no de sua residência ou no do lugar onde for encontrado." O Planalto remete às ADI 5737 e 5492, não conferidas | lei (compilado DRAFT) |
| 24 | Tema 373 | **confere** | Leading case REsp 1.146.194; não se aplica ao IPTU | tese |
| 34 | TJRJ IAC 8, questão 5 | **confere** (questão) | Tese firmada **não localizada** | metadados |
| 34 | 8064523, resultado | **confere: favorável** | "Recurso conhecido e provido [...] admitir a penhora sobre o imóvel indicado" | ementa TJBA (coleta dirigida) |
| 34 | Tema 769 | **confere** | Leading case REsp 1.835.864 | tese |
| 34 | Tema 1012 | **confere** | Trecho entre aspas literal | tese |
| 34 | Súmula 406/STJ | **confere** | "A Fazenda Pública pode recusar a substituição do bem penhorado por precatório." | verbete |
| 36 | 0511072, quem apelou | **confere: o executado** | E-01 | ementa TJBA + ponteiro <ACERVO>/ |
| 36 | Súm. 452/STJ; Súm. 17/TJBA; Tema 1.184/STF | **confere** | Textos no JSON. Há tensão entre o Tema 1.184 (item 1, "respeitada a competência constitucional de cada ente federado") e as súmulas; o TJBA a resolve pela existência de lei municipal (8001275, 8011684). Alcance: MIJ | verbete e tese |
| 36 | IAC no REsp 1.604.412/SC | **confere** (por citação) | Rel. Bellizze, j. 27/06/2018, DJe 22/08/2018, citado no AgInt nos EDcl no REsp 1.755.008/PR; o IAC não é documento próprio do acervo | segunda mão |
| 37 | TJSC IAC 28 | **confere** | Literal até "deve ser dispensada"; continua "(parcial ou totalmente, conforme o caso), na execução fiscal, a garantia do juízo para a oposição de embargos do devedor."; transitado em julgado | tese |
| 37 | Repetitivo que dispense a garantia | **confere a ausência** | O precedente invocado é o REsp 1.487.772/SE (Primeira Turma, Gurgel de Faria, j. 28/05/2019), de Turma, não repetitivo | citação (AgInt no AREsp 2.042.546) |

## 4. Conferido e sustentado (verde)

| Afirmação | Verificação |
|---|---|
| Contagens das seis fichas (catálogo, acervo, contrárias, fora da contagem) | O MD bate com o JSON e com o pacote: TES-16 9/0, 1.207/1.079/172; TES-18 14 (13 + 1 parcial)/9, contrárias 8 + 1 + 3 = 12; TES-24 0/0, 210/194/23; TES-34 6/0, contrárias 2 + 3 = 5; TES-36 1/1, contrárias 1 + 6 + 3 = 10; TES-37 3/0, contrárias 1 + 1 |
| Número, órgão e data de todos os julgados TJBA citados | Batem com o pacote item a item. A única divergência é o rótulo 2ª VP (A-01, B-02), que é do próprio pacote |
| Paráfrases das regras nas seis fichas | Fiéis aos excertos e, quando lidas, às ementas. Exemplos: 0529503 homônimo com três execuções e penhora; 8125564 lançamentos anulados com depósito integral; 0037689 "EXISTÊNCIA DE PROVA DOCUMENTAL INDICANDO A PERMANÊNCIA DO DÉBITO EM ABERTO"; 8105607 "Contraditório substancial observado"; 0803273 aposentado com R$ 1.100 (um salário mínimo); 8018463 valor venal superior |
| Tema 777 (REsp 1.686.659), Tema 421 (REsp 1.185.036), Tema 143 (REsp 1.111.002), Tema 578 (REsp 1.337.790), Tema 260 (REsp 1.127.815) | Basanos `existe_no_indice` com o leading case declarado; o texto das teses bate com o PANGEA |
| Tema 260: data e órgão; aspas do item 11 | Teor: "Brasília (DF), 24 de novembro de 2010 (Data do Julgamento)", Primeira Seção; "conquanto a insuficiência patrimonial do devedor seja justificativa plausível [...] deve ser a mesma comprovada inequivocamente" |
| AREsp 2.810.673 (Terceira Turma, publicado em 10/04/2025; duplicata; dano in re ipsa) | `STJ:integras:306683039`: "acordam os Ministros da TERCEIRA TURMA"; "DUPLICATAS. PROTESTO INDEVIDO. PESSOA JURÍDICA. DANO IN RE IPSA"; persuasivo e com identidade parcial, como a ficha diz |
| Súmulas 58, 481, 406 e 452/STJ | Textos idênticos aos do Cognitio |
| CTN 158, I, em 0804591 e 0790870 | Ementa: "PAGAMENTO DE UM CRÉDITO DE FORMA PARCIAL NÃO IMPORTA EM PRESUNÇÃO DE PAGAMENTO DAS PRESTAÇÕES EM QUE SE DECOMPONHA. INTELIGÊNCIA DO ART. 158, INCISO I, DO CTN" |
| TES-36: "A ementa é igual à do anterior" (0762145 × 0825054) | Ementas do laboratório (DEC-TJBA-b0a725877fc7) e do pacote: idênticas palavra por palavra |
| Walton: TES-16, 18, 34, 37 `PLAUSIBLE`; TES-24 e 36 `WEAK_UNANSWERED_CQ` | Coerentes com o que cada ficha mostra (ressalva C-01). O motor não confere fato, como as fichas declaram |
| ADI 7695, ADI 7697 e ADC 84 "impertinentes" (TES-36) | Pacote: emendas PIX e orçamentárias; PIS/COFINS sobre receitas financeiras ("princípios da segurança jurídica e da não surpresa" na alíquota) |

## 5. O que não foi verificado

- O inteiro teor dos acórdãos do TJBA. A conferência foi pela ementa do laboratório (`derivados/ementas-candidatos.jsonl`), mais uma linha crua do <ACERVO>/ para o metadado da 2ª VP. As datas do TJBA são as do banco, que para o TJBA costuma ser a data de publicação, e não foram confrontadas com a sessão.
- A tese firmada no TJRJ IAC 8. A lei de organização judiciária e as resoluções do TJBA sobre varas fiscais. As leis municipais (parcelamento, custas, teto de execução).
- O efeito das ADI 5737 e 5492 sobre o CPC, art. 46, § 5º (o Cognitio só traz indexação telegráfica). A situação atual do art. 15, I, da Lei 5.010/66, citado pelo Tema 373: o diploma não está no acervo de leis, e a hipótese de revogação não foi conferida.
- A situação no portal do STF e do STJ de cada tema e súmula, em 06/11/2026. Usei cadastro e tese do Cognitio e o espelho BNP (PANGEA). A ADI 5135 está fora dos índices próprios do Basanos.
- O REsp 1.487.772/SE e o IAC no REsp 1.604.412/SC foram conferidos só por citação em outro acórdão. Não estão no acervo como documento próprio.
- As páginas de Walton, Reed e Macagno (2008) e os rótulos `ARG.SCH.WRM08.*` do Élenchos.
- O MIJ não foi feito. Ficam para ele: o alcance do Tema 1.184 diante das Súmulas 452/STJ e 17/TJBA (TES-36), o do Tema 578 para a pessoa natural (TES-34) e o do Tema 260 para a ausência total de garantia (TES-37).
