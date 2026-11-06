---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
lote: E4-3 / F6
alvo: analises/fichas/TES-17, TES-26, TES-28, TES-32 (.md e .json, draft de 06/11/2026)
pacote: estado/E4-3/pacote-F6_merito_diverso.json
destino-do-alvo: interno (pesquisa; nada a renderizar nem enviar)
metodo: conferência manual contra a fonte própria (brief estado/brief-antialucinacao-fichas-v1.md; formato do precedente auditoria/antialucinacao-TES-001-v1.md)
saida-por-codigo: auditoria/antialucinacao-E43-F6.json (36 itens; o código conferiu que cada "de" é trecho único e exato da ficha)
---

# Antialucinação: fichas E4-3, lote F6

## 1. Veredito

**Nenhum achado grave nas quatro fichas.** Não há citação inventada nem aspa falsa. As oito súmulas citadas batem letra por letra com o Cognitio: STJ 162, 188, 213, 460 e 461; STF 70, 323 e 547. As teses dos Temas 142, 229, 258 e 387 do STJ também batem, e o mesmo vale para o AREsp 2.345.529 e o teor do REsp 947.206.

Na parte mecânica, um script cruzou com o pacote os 51 excertos dos JSON e todos os números de processo das fichas. Resultado: 0 excerto não literal e 0 número fora do pacote. A única exceção é o 8190679 da TES-26, que a própria ficha diz vir do DJEN da TES-28, onde ele está literal. As contagens dos JSON também batem com o pacote: 14/291, 4/179, 2/766 e 1/9, e as 5 contrárias da TES-17 conferem. Câmara e data de cada linha batem com o pacote. Onde li a ementa inteira no acervo acervo local (pelos ponteiros de `dados/candidatos-tjba.jsonl`), as paráfrases ficaram fiéis, com as ressalvas abaixo.

O **médio** está na TES-26. A ficha diz que o material não mostra lei municipal que autorize a compensação, e o Walton (CQ2) se apoia nisso. Mas o voto de 0563911-23.2014, um dos 4 casos do catálogo, cita a lei de Salvador: o art. 22 do CTRMS (Lei 7.186/2006). A ementa do mesmo acórdão cita ainda os Decretos 24.102/2013 e 24.215/2013. A objeção da CQ2 continua de pé, e o STJ a confirma (AREsp 2.608.527). Só que, para Salvador, a premissa "não há lei" está errada.

| Ficha | Pior gravidade | `[A CONFERIR]` resolvidos | Veredito |
|---|---|---|---|
| TES-17 | leve | 3 de 4 | segue; 11 ajustes leves (via do lote 0235, CQ2 com art. 97 § 2º mal atribuído, AgInt 2.062.845 conferido) |
| TES-26 | **médio** | 3 de 3 | segue com correção da premissa "não há lei municipal" (§ 2, § 6 CQ2, contra-analogia, § 7) |
| TES-28 | leve | 1 de 2 | segue; 6 ressalvas (CQ2 já respondida no próprio 0500725) |
| TES-32 | leve | 1 de 3 | segue; 9 ressalvas (amostra é 8, não 7; 8065174 tem resultado; Tema 31 conferido) |

## 2. Afirmações problemáticas

### TES-26

**A-26-01 · MÉDIO · erro de fato sobre o material (a premissa do CQ2 está errada para Salvador)**
- **Ficha:**
  - § 2: "A lei municipal que autorize a compensação de IPTU não foi identificada nem lida."
  - § 6, CQ2: "**Não respondida.** [...] O material não mostra lei municipal que autorize a compensação de IPTU, nem enfrenta a objeção de que um pedido sem base legal não suspenderia nada."
  - Contra-analogia: "lá a base era a cláusula contratual, não a lei."
  - § 7: "A lei municipal autorizadora (Salvador e outros) é o ponto central e não foi lida."
- **Fonte** (0563911-23.2014.8.05.0001, Primeira Câmara, 17/02/2020; acervo acervo local, DEC-TJBA-5b2d3f862525):
  - ementa: «a legislação que rege a compensação tributária pleiteada é aquela vigente ao tempo do requerimento administrativo de compensação. IMPOSSIBILIDADE DE APLICAÇÃO DOS CRITÉRIOS E CONDIÇÕES PREVISTOS NOS DECRETOS MUNICIPAIS N. 24.102/2013 E 24.215/2013»;
  - voto: «Nos termos do artigo 170, caput, do CTN, para que seja admitida, a compensação exige lei [...] No âmbito municipal, a compensação está regulada no artigo 22 do Código Tributário e de Rendas do Município do Salvador Lei n.º 7.186/06: "Fica o Chefe do Poder Executivo autorizado a realizar cessão de créditos tributários [...] bem como a compensação de créditos tributários do Município, com créditos líquidos e certos, vencidos ou vincendos do sujeito passivo contra a Fazenda Pública do Município [...]"».
- **STJ sobre a objeção** (Cognitio `STJ:integras:281727625`, AREsp 2.608.527, Primeira Turma, publicado em 14/11/2024): «por ausência de legislação específica autorizativa, o pedido de compensação de tributo com precatório não suspende a exigibilidade do crédito tributário».
- **Leitura:** a ficha lê só o excerto do pacote, que corta a ementa. O material do próprio catálogo identifica a lei de Salvador e mostra que o caso da transação também se apoiou na lei, e não só na cláusula. A objeção da CQ2 (sem lei, o pedido não suspende) é real e o STJ a confirma. Por isso a CQ2 fica **parcialmente respondida** para Salvador: há lei, falta ler o texto e o regulamento. Para os outros municípios, segue sem resposta. O status `WEAK_UNANSWERED_CQ` continua defensável fora de Salvador. Para Salvador, o orquestrador pode rodar de novo o Élenchos com a CQ2 respondida em parte. Os quatro textos corretos estão no JSON.
- **Por que médio e não grave:** a conclusão prática ("argumento acessório, risco alto") não muda. O que muda é o diagnóstico do ponto fraco.

**A-26-02 · LEVE · § 8, "Quando não usar: Pedido protocolado depois do ajuizamento."** No 8031438-92.2020, ementa item 4, o exercício de 2013 tinha pedido feito depois do ajuizamento e o resultado foi «o seu sobrestamento», com liminar em mandado de segurança suspendendo a exigibilidade. Não houve extinção, mas o pedido também não foi inútil.

**A-26-03 · LEVE · vigência do art. 151, III.** A ficha parafraseia "reclamação ou recurso administrativo". O compilado do Planalto no Cognitio traz hoje a redação dada pela LC 236/2026: «as impugnações, os recursos e a manifestação de inconformidade, nos termos das leis reguladoras do processo tributário administrativo». Os acórdãos de 2020 e 2021 aplicaram a redação anterior. Se o pedido de compensação cabe na redação nova é questão para o MIJ. A base é de status DRAFT: confira no Planalto.

**A-26-04 · LEVE.** "decisão de 25/09/2026" (8190679) é a data de disponibilização no DJEN.

### TES-17

**A-17-01 · LEVE · via do lote 0235 (`[A CONFERIR]` resolvido).** As quatro ementas no acervo dizem: «sentença proferida em sede de execução fiscal [...] que, diante da cobrança de valor de pequena monta, reconheceu extinção do crédito tributário, por isenção legal, e, por conseguinte, indeferiu a petição inicial e extinguiu o feito sem apreciação meritória». A extinção foi **de ofício**, sem embargos nem exceção. A Terceira Câmara a manteve na apelação do Município. Isso põe em tensão o lote com a contrária 8001022-81.2021 (Quarta Câmara, mesmo Município): «Não cabe ao Judiciário, de ofício, decretar a extinção de Execução Fiscal sob o fundamento de que o valor cobrado é insignificante». A ficha distingue os dois casos só pelo valor. Há também a diferença entre isenção e insignificância, e o Juízo de origem extinguiu de ofício nos dois. Qual leitura prevalece fica para o MIJ.

**A-17-02 · LEVE · atribuição errada de dispositivo (§ 6, CQ2).** "a presunção de legitimidade do lançamento (CTN, art. 97, § 2º)". O § 2º do art. 97 diz: «Não constitui majoração de tributo [...] a atualização do valor monetário da respectiva base de cálculo». Nas ementas, a presunção de legitimidade é um fundamento à parte. O § 2 da própria ficha está certo; o erro está só na tabela.

**A-17-03 · LEVE · 8040730 (Teixeira de Freitas).** A ementa (item 5) diz: «documentos que comprovam a condição de aposentada da genitora da agravada e o valor de seu benefício previdenciário». A aposentada é a mãe da agravada.

**A-17-04 · LEVE · "Faltou prova (sem laudo)" (8009857).** A ementa diz só «AUTORA QUE NÃO LOGROU ÊXITO EM COMPROVAR QUE O VALOR ATRIBUÍDO AO SEU IMÓVEL ESTÁ SUPERESTIMADO». Que não havia laudo é inferência.

**A-17-05 · LEVE · § 2 omite o art. 83, IX, da Lei 7.186/2006.** É a base da faixa de isenção por valor venal usada em dois favoráveis: 8002398, «IMÓVEL CUJO VALOR NÃO ULTRAPASSE R$ 93.540,96 (-). INTELECÇÃO DO ART. 83, IX»; e 8001327, valor venal inferior a R$ 80.000,00. A sub-regra 1 da ficha mistura isso com a Lei 107/2009 de São Francisco do Conde.

**A-17-06 · LEVE · 0198690 como contrária.** É ação de consumo contra a vendedora («comprou imóvel junto a Ré através do programa Casa Verde e Amarela»), e o Município não é parte. O caso análogo 0089584 (ITIV, também contra a MRV) a ficha põe "fora da conta". O critério deveria ser o mesmo nos dois. A contagem do catálogo não muda.

**A-17-07 · LEVE.**
- 8014812: "05/02/2025" é a data do DJEN. A decisão também se apoia no depósito integral (art. 151, II; Súmula 112).
- § 7: dos 251 processos sem indício, 8 foram lidos na amostra.

### TES-28

**A-28-01 · LEVE · CQ2 "Não alegada no material" (`[A CONFERIR]` resolvido).** A objeção civil foi alegada e rejeitada no próprio catálogo. Em 0500725-41.2018 (Quarta Câmara, ementa no acervo), a sentença tinha negado a restituição, e o acórdão a reformou, «afastando-se, por conseguinte, a regra prevista no Código Civil (artigo 882)», porque «a prescrição não extingue apenas a ação para a cobrança do tributo, mas o próprio crédito e a relação material». O status `PLAUSIBLE` fica mais forte, porque a CQ2 passa a ter resposta.

**A-28-02 · LEVE · Tema 229, "Limite no teor".** A frase está na ementa, item 5, mas é transcrição do REsp 593.356/RJ, adotada pela Seção. O item 9 completa: a transferência do direito de repetir «deve ser específica». É a base do "cessão específica" do § 5, que fica sustentado.

**A-28-03 · LEVE · § 2, padrão construtivo.** Em 8032508 o vício é «ALTERAÇÃO DA DESTINAÇÃO DA ÁREA OCUPADA [...] (LEI N°. 8.473/2013 E N°. 7.186/2006)». Padrão construtivo (B5 × B4) é só o 8190679.

**A-28-04 · LEVE.** As datas de 8190679 (25/09/2026) e 0010500 (23/09/2026) são de disponibilização no DJEN.

### TES-32

**A-32-01 · LEVE · número da amostra.** A ficha diz "a amostra (7)", mas o pacote traz 8 itens em `amostra_outras` (o 8028759 vem com id `DEC-TJBAAPI`). São 4 favoráveis claros, 1 favorável com resultado (A-32-02) e 3 ruídos. Os 8 restantes foram todos lidos.

**A-32-02 · LEVE · 8065174 tem resultado.** O acórdão da mesma data está no acervo (DEC-TJBA-15139248e0cd): «conhecer e negar provimento ao apelo, mantendo a sentença». O apelo do Município pedia só a redução dos honorários. É favorável, mas o mérito (sanção política) ficou na sentença, sem revisão pela Câmara.

**A-32-03 · LEVE · "A maior parte é remessa necessária".** São 3 de 6 processos com mérito: 8029958, 8009256 e 8031036. Os outros são apelação em mandado de segurança (0510899), agravo contra liminar (8028759) e apelação em ação ordinária (8065174).

**A-32-04 · LEVE · § 2.** O 8009256 invoca só a Súmula 323 («SÚMULA 323 DO SUPREMO TRIBUNAL FEDERAL»). As três súmulas estão em 0510899, em 8031036 e na sentença transcrita em 8065174.

**A-32-05 · LEVE · tese do Tema 31 cortada.** A citação para em "–", e a tese segue: «tal qual ocorre com a exigência, pela Administração Tributária, de fiança, garantia real ou fidejussória como condição para impressão de notas fiscais de contribuintes com débitos tributários». O núcleo geral está certo; o corte só esconde o caso concreto.

**A-32-06 · LEVE · contra-caso adicional (amarelo, MIJ).** Ao buscar a ADI 173, o Cognitio devolveu a ADI 4854 (PANGEA, regime especial de fiscalização para devedor contumaz de ICMS): «A submissão de contribuintes inadimplentes a regime fiscal diferenciado, sem inviabilizar o exercício da atividade econômica, não configura sanção política ou meio oblíquo de cobrança». Ela reforça o ponto de fuga do § 6. O alcance fica para o MIJ.

## 3. Conferido e sustentado (verde)

| Afirmação | Fonte e verificação |
|---|---|
| TES-26/28 § 4: Súmulas 213, 460, 461, 162 e 188 do STJ (aspas) | Cognitio `STJ:sumulas:*`, literal; a 188 confere com «(SÚMULA 188, PRIMEIRA SEÇÃO, julgado em 11/06/1997...)» |
| TES-32 § 4: Súmulas 70, 323 e 547 do STF (aspas) | Cognitio `STF:sumulas:70/323/547`, literal |
| TES-26: Tema 258 = "É incabível o mandado de segurança para convalidar a compensação tributária realizada pelo contribuinte." | `STJ:precedentes:Tema-258`, campo tese, literal (mesmo texto da Súmula 460) |
| TES-28: Tema 229, REsp 947.206/RJ, Primeira Seção, 13/10/2010, IPTU, TCLLP e TIP, aspas da tese e do art. 168, I | `STJ:paradigmas-teor:200700991022-1011837`: «Brasília (DF), 13 de outubro de 2010(Data do Julgamento)»; ementa «IPTU, TCLLP E TIP»; tese no `STJ:precedentes:Tema-229` |
| TES-28: Tema 142, REsp 1.110.578/SP, Primeira Seção, 12/05/2010, taxa municipal, aspas | `buscar_juris` (identificador exato): «TAXA DE ILUMINAÇÃO PÚBLICA», Município de Barretos, 12/05/2010; tese literal |
| TES-28: Tema 387, aspas do art. 149, VIII | `STJ:precedentes:Tema-387`, tese literal |
| TES-17 § 4: AREsp 2.345.529, Segunda Turma, publicado em 25/09/2024, Súmula 7, as duas aspas | `STJ:integras:272539042`: «SEGUNDA TURMA [...] sessão virtual de 17/09/2024 a 23/09/2024»; publicação 2024-09-25; as duas aspas literais (a primeira é transcrição do AgInt no REsp 2.062.845/SP) |
| TES-28 § 2: art. 165 «independentemente de prévio protesto» | Cognitio `lei-5172-1966-ctn-art-165` |
| TES-17: lote 0235 julgado em 06/02/2024, Terceira Câmara, Lei 107/2009 até R$ 50,00 "sem qualquer desconto" | quatro ementas do acervo, idênticas no ponto |
| TES-17: 0315192 em embargos à execução, art. 2º da Lei 7.719/2009; 0327783 em embargos à execução, decreto isenta após 2013 e remite antes | ementas no acervo (DEC-TJBA-cba360e9029c, -9394dea6428c) |
| TES-17: 8070993 (APP reconhecida pelo próprio Município; arts. 32 e 34 do CTN), 8016004 e 8016224 (zona de proteção, «ISENÇÃO DEVIDA») | ementas no acervo |
| TES-17: 0503134, mandado de segurança, Camaçari, prova pré-constituída insuficiente | pacote, amostra (ementa) |
| TES-26: 8031438 em exceção de pré-executividade; 2012 extinto, 2013 sobrestado | ementa no acervo |
| TES-26: 0814389, Município arca com a sucumbência por causalidade | ementa no acervo («ÔNUS DO ENTE PÚBLICO [...] HONORÁRIOS MAJORADOS. ART. 85, § 11») |
| TES-26: 0567700, resultado parcial (anulou a sentença terminativa) | ementa no acervo («SENTENÇA ANULADA. RETORNO DOS AUTOS À ORIGEM»); cita também o REsp 1.365.095/SP (Tema 118 do STJ) |
| TES-28: 8002219 (Quinta Câmara, ED com efeitos modificativos, imóvel para moradia de ministros, 2018 a 2021), 8000435 (Camaçari, Leis 1.293/2013 e 1.359/2014, pedidos improcedentes), 0010500 (Ilhéus, guia de imóvel alheio) | textos do DJEN no pacote |
| TES-32: 8029958 (art. 323, par. ún., da Lei 7.186/2006 afastado), 8031036 (arrematação, Tema 1113), 8028759 (Morro do Chapéu, credor fiduciário legitimado) | amostra do pacote; ementa de 8031036 no acervo (inclui o art. 130, par. ún., do CTN) |
| TES-32: ADI 3952 (registro especial, devedor contumaz, apuração do montante e devido processo) | ementa do registro PANGEA no pacote |
| TES-17/26/28/32: Walton coerente com a ficha | TES-17 `PLAUSIBLE` (CQ3 em aberto, ônus do questionador); TES-26 `WEAK_UNANSWERED_CQ` (CQ2; ver A-26-01); TES-28 `PLAUSIBLE` (fica mais forte com A-28-01); TES-32 `PLAUSIBLE` (as três CQ com resposta no material) |

## 4. Itens `[A CONFERIR]`

| Ficha | Item | Resultado | Referência |
|---|---|---|---|
| TES-17 | CTN, arts. 176 e 179 | **confere** | Cognitio `lei-5172-1966-ctn-art-176/179` (DRAFT); 0327783, item 4, aplica a regra do art. 179 via CTM de Salvador |
| TES-17 | AgInt no REsp 2.062.845/SP | **confere** | `STJ:integras:223610641`: Primeira Turma, Regina Helena Costa, publicado em 21/12/2023; proveu o REsp do Município (APP, por si só, não afasta o IPTU) |
| TES-17 | classe do lote 0235 | **diverge** da hipótese do § 5 (embargos ou exceção) | apelação do Município contra extinção **de ofício** na execução fiscal (A-17-01) |
| TES-17 | precedente qualificado sobre isenção por lei municipal | não buscado; limite declarado | direito local; a ficha declara |
| TES-26 | CTN, arts. 170, 170-A e 156, II | **confere** | Cognitio `lei-5172-1966-ctn-art-170/170-A/156` (DRAFT) |
| TES-26 | STJ: o pedido de compensação suspende a exigibilidade | **confere, com limite** | REsp 1.157.847/PE (repetitivo, 24/03/2010); REsp 2.083.104 (Primeira Turma, 11/06/2025); limite no AREsp 2.608.527 (sem lei autorizativa não suspende). Alcance para o IPTU: MIJ |
| TES-26 | CQ2, "CTN, art. 170" | **confere** | idem |
| TES-28 | precedente do STJ sobre repetição de crédito prescrito | **nao_localizado** | duas buscas no Cognitio em 06/11/2026, resultados exploratórios sem correspondência |
| TES-28 | CQ2, objeção por analogia civil | **confere que foi enfrentada** | 0500725: art. 882 do CC afastado; art. 156, V, do CTN (A-28-01) |
| TES-32 | acórdão do Tema 31 de RG | **confere** | RE 565.048/RS, Plenário, 29/05/2014, Marco Aurélio, unânime; `STF:paradigmas-teor:31-6911989` |
| TES-32 | inteiro teor da ADI 173 | **nao_localizado** (teor); ementa confere | Basanos: fora do índice; `STF:pangea:stf-adi-173` (ementa, item 3) |
| TES-32 | inteiro teor da ADI 3952 | **nao_localizado** (teor); ementa confere | Basanos: fora do índice; ementa PANGEA no pacote |

Os JSON das fichas TES-17 (AgInt 2.062.845), TES-26 ("STJ: pedido de compensação...") e TES-32 (Tema 31) marcam esses precedentes como `"conferido": false`. Depois da aplicação, o orquestrador pode trocar para `true` com a fonte acima. Esses campos não estão no JSON de saída, porque o `de` é sempre trecho do `.md`.

## 5. O que não foi verificado

- Inteiro teor do TJBA: só li o que está no acervo acervo local (ementa e, quando havia, o voto) e no pacote. Os votos dos acórdãos do DJEN de 2026 vêm truncados (cerca de 2.500 caracteres).
- Leis municipais (Lei 107/2009 e CTM de São Francisco do Conde; Lei 7.186/2006, arts. 22, 83 e 323; Leis 7.719/2009, 308/2003, 8.473/2013 e as de Camaçari): nenhuma foi lida na fonte. O art. 22 do CTRMS foi lido só como transcrito no voto de 0563911.
- CTN pelo Cognitio (compilado do Planalto, status DRAFT); não abri o Planalto. A redação do art. 151, III, dada pela LC 236/2026, precisa de conferência na fonte (A-26-03).
- Inteiro teor das ADI 173, 3952 e 4854: não está no Cognitio.
- Páginas de Walton, Reed e Macagno (2008) e rótulos `ARG.SCH.WRM08.*`: fora do escopo, não conferidos.
- Situação atual (cancelamento, revisão) das súmulas e temas no portal do STF e do STJ: não consultada. O acervo avisa que não prova vigência.
- MIJ não feito. Ficam para ele: o alcance do REsp 1.157.847 e do REsp 2.083.104 para o IPTU municipal (TES-26); a tensão entre o lote 0235 e o 8001022 (TES-17); a ADI 4854 como contra-caso (TES-32).
