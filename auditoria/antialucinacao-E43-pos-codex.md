---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
lote: pos-codex (trocas da correção dos itens 1, 3 e 9 do Codex)
alvo: as 196 trocas de auditoria/correcoes-pos-codex-e43.jsonl (32 fichas .md/.json e analises/fichas/00-INDICE.md)
originais: estado/E4-3/antes-pos-codex/
destino-do-alvo: interno (pesquisa; nada a renderizar, nada a enviar)
metodo: brief-antialucinacao-fichas-v1 (formato, gravidade). Conferência das trocas, e só delas, contra o texto das decisões (derivados/ementas-candidatos.jsonl), os pacotes estado/E4-3/pacote-*.json, estado/E4-3/recorte-acervo.json e a própria ficha. Não usei o pipeline `conferidor`: o destino é interno e o formato pedido é trecho, fonte e gravidade.
---

# Antialucinação: trocas pós-Codex da E4-3

## 1. Veredito

**Nada grave.** O item 1 (órgão) está certo em todas as trocas. O item 3 (`n_acervo` e `n_acervo_fav`) bate em todas as fichas e em todas as linhas do índice. Nenhuma troca mexeu em excerto literal. O problema está no item 9: em algumas trocas, uma frase vaga virou contagem, mas a contagem afirma mais do que os excertos sustentam. Foram 2 médios e 8 leves nas trocas, e mais 2 leves residuais fora delas (resíduos do item 9 que a nota do índice dá por resolvidos). As propostas estão no `.json` (12 itens).

| Ficha | Pior gravidade | Itens | Veredito |
|---|---|---|---|
| TES-16 | **médio** | P-01 | A formulação atribui "presumido (in re ipsa)" aos 9 favoráveis; só 1 excerto diz isso. |
| TES-30 | **médio** | P-02 | "Nos casos do material, a restrição total dependeu de prova técnica" contradiz o que a própria ficha mostra de 0555629 e 0030481. |
| TES-08 | leve | P-03, P-04 | O argumento de Walton passou a dizer "nos 11", mas a CQ1 da ficha diz 8 de 11. O "11 de 11" do risco tem por denominador um recorte só de favoráveis. Status `PLAUSIBLE` coerente. |
| TES-13 | leve | P-05, P-06 | "Nos 18 do catálogo, [...] depois de despacho de emenda": o excerto mostra a emenda em 8 dos 18. |
| TES-10 | leve | P-07, P-08 | "7 decisões [...] afastam por distinção": a distinção está expressa em 3. A formulação do JSON manteve a generalização. |
| TES-39 | leve | P-09 | "Negou nas 3 decisões": são 3 processos; houve também a apelação de 8002112, revertida. |
| TES-20 | leve | P-10, P-12 | "Nos excertos que indicam o remédio": o de 0333357 não indica. Resta um "resultado típico" (residual). |
| TES-23 | leve | P-11 | Resta um "a via mais usada" (residual, fora das trocas). |
| TES-04, 07, 09, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24 a 29, 31 a 34, 36, 37 e 00-INDICE | nenhum | — | As trocas conferem. |

## 2. Cobertura e regra

Conferi **as 196 trocas, sem amostragem.** Não foi preciso amostrar.

- **Aplicação** (código). Repus as 196 trocas, em ordem, sobre `estado/E4-3/antes-pos-codex/`: o resultado reproduz as 65 versões atuais. A única diferença é uma linha em branco antes da nota acrescentada no fim de cada arquivo. Não há troca fora do registro. Cada `de` existia uma única vez quando foi trocado. Os 32 JSON abrem sem erro.
- **Item 1** (código e leitura). Para cada número de processo das 44 trocas do item 1 e das notas "1+…", procurei todos os registros em `derivados/ementas-candidatos.jsonl` e li três coisas: o cabeçalho "Órgão Julgador", o "ACORDAM … da X Câmara" e o dispositivo. Também conferi se o id do catálogo no pacote é o da linha citada na `fonte`.
- **Item 3** (código). Para as 32 fichas, cruzei o JSON (`n_acervo` e `n_acervo_fav`), a frase "Acervo …" do § 3 do MD, `pacote.acervo` (`n_processos` e `n_processos_fav_indicio`), `recorte-acervo.json[n].n` (decisões), `n_acervo_detalhe` e as duas colunas novas do índice. No índice, conferi também que as outras colunas (Nº, ficha, formulação, fav. no catálogo, Walton, precedentes) não mudaram.
- **Item 9** (leitura). Li cada uma das 51 trocas do item 9 e as "3+9" e "1+3+9" contra a seção da ficha ou do pacote que a `fonte` aponta. Recontei as contagens a partir dos itens listados.
- **Excerto literal** (código). Nenhuma troca tem «…» no `de` nem no `para`, e nenhum excerto do JSON mudou. As citações entre aspas simples nas `fonte` das trocas do item 1 são literais nas ementas, inclusive as que têm "[...]".
- **Walton** (leitura). Li todas as trocas que mexem em argumento, CQ ou status: #23, #38, #39, #47, #48 e as notas #162, #167 e #175.

## 3. Item 1 (órgão): confere em todas

Todos os 23 registros que o banco rotula "2ª Vice-Presidência" e que as trocas atribuem a uma Câmara trazem no texto o cabeçalho e o "ACORDAM" dessa Câmara. A decisão também confere quando a troca a descreve.

| Ficha | Processo | Linha (ementas) | Texto | Troca |
|---|---|---|---|---|
| TES-04 | 0067028-21.2010 | 9667 | Terceira Câmara, NEGAR PROVIMENTO | confere |
| TES-04 | 0126041-58.2004 | 3979 | Quarta Câmara | confere |
| TES-04 | 0167595-07.2003 | 4879 | 2ª Vice-Presidência, «nego seguimento ao recurso especial com fundamento no Tema 166» | confere (é de fato admissibilidade) |
| TES-07 | 0501103-22.2016 / 8005329-04.2021 / 0306925-91.2018 / 0504150-45.2016 | 9841 / 9970 / 4296 / 4139 | Quinta / Terceira / Quinta / Primeira, todos com «ACORDAM» | confere |
| TES-07 | 0306925-91.2018 (2ª VP) | 5179 | «inadmito o recurso especial»; sem data no corpo | confere (#195) |
| TES-09 | 0769929-71.2017 | 6722 | Quinta Câmara, negar provimento | confere |
| TES-11 | 0502098-35.2016 / 0500177-07.2017 / 8087684-08.2020 | 5453 / 4751 / 6006 | Segunda / Quinta / Segunda | confere |
| TES-11 | 8087684-08.2020 (2ª VP) | 7182 | sobrestamento; «Salvador(BA), 18 de junho de 2024» (o metadado diz 19/06) | confere |
| TES-13 | 8005591-65.2023 | 8412 | Quarta Câmara | confere |
| TES-14 | 0516790-62.2015 | 5581 | Quarta Câmara, DAR PROVIMENTO | confere |
| TES-15 | 8003250-77.2020 / 0531268-12.2014 | 9592 / 4554 | Terceira, NEGAR PROVIMENTO / Segunda | confere |
| TES-20 e TES-21 | 0507452-30.2016 | 4316 | Segunda Câmara, DAR PROVIMENTO | confere |
| TES-21 | 0302531-29.2015 / 8001590-06.2021 / 8038630-90.2019 / 0304400-61.2014 | 3300 / 7065 / 6007 / 8868 | Segunda / Quarta / Quarta / Quarta («por maioria»), todos NEGAR PROVIMENTO | confere |
| TES-21 | 8001720-30.2020 / 8022215-18.2020 | 7006 / 2145 | Terceira / Quarta (agravo de instrumento) | confere |
| TES-23 | 0016654-52.2008 | 8112 | Terceira Câmara, DAR PROVIMENTO | confere |
| TES-23 | 0016654-52.2008 (2ª VP) | 9044 | «não admito o presente Recurso Especial», «28 de Julho de 2025» | confere |
| TES-25 | 0562941-23.2014 | 1975 | Quinta Câmara | confere |

**Contagens por órgão refeitas por código** (órgão do texto; sem cabeçalho, o do metadado):

| Ficha | Resultado |
|---|---|
| TES-04 | Primeira 5, Segunda 3, Terceira 7, Quarta 5, Quinta 4, 2ª VP 1: "Primeira a Quinta e, em 1 dos 25, a 2ª VP"; mérito 24 de 25. **Confere.** |
| TES-07 | Sexta TR 6, Segunda 6, Quarta 5, Quinta 3, Primeira 2, Terceira 2 (= 24). **Confere.** |
| TES-09 | Sexta TR 8, Primeira, Quarta e Quinta 4 cada, Terceira 2, Segunda 1 (= 23). **Confere.** |
| TES-11 | só Primeira a Quinta (21). **Confere.** |
| TES-13 | só as cinco Câmaras (18). **Confere.** |
| TES-15 | Primeira, Terceira, Quarta e 6ª TR (8). **Confere.** |
| TES-21 | Primeira a Quinta e 6ª TR (10). Entre as contrárias, a 2ª VP passa de 4 para 3 (0505600 L8181, 0507524 L7819, 8000169 L396, todas inadmissões reais). **Confere.** |
| TES-23 | Terceira 4, Segunda 2, Quinta 1, Primeira 1, 6ª TR 1. **Confere.** |
| TES-14 | contrárias de admissibilidade 3 → 2 (0542847 L7629 e 0507145 L8198, inadmissões reais); total de 7 sem mudança. **Confere.** |

**A afirmação da nota #194 também foi conferida.** A nota diz que, nas demais fichas, as menções à 2ª VP "são decisões reais de admissibilidade ou já traziam a ressalva". Conferi linha a linha:

- TES-08 0506436: L8173, texto «2ª Vice Presidência», «nego seguimento».
- TES-11 0323034: L7970, inadmito. TES-11 8030962: L8746, não admito.
- TES-20 0567192: L7470. TES-20 0507145: L8198.
- TES-33 8024363: L8976, sobrestamento.
- TES-34 8013496, 8000428 e 8002424: L4164, L780 e L753, inadmissões.
- TES-39 8019519: L4020.
- TES-28 0010500: DJEN; o texto do pacote F6 abre com «2ª Vice Presidência».
- Ressalva já presente: TES-16, 18, 19, 22, 27, 29 e 31.

## 4. Item 3 (`n_acervo`): confere em todas

Nas 32 fichas, `n_acervo` é o total de processos do recorte e `n_acervo_fav` é o subconjunto com indício. Os dois são iguais ao `pacote.acervo.n_processos` / `n_processos_fav_indicio`, à frase do § 3 do MD e às duas colunas do índice. O `n` de `recorte-acervo.json` é igual ao de decisões do MD.

- As seis que mudavam de semântica (TES-16, 18, 24, 34, 36 e 37) agora mostram 1.079/172, 499/57, 194/23, 56/9, 70/25 e 445/45. `n_acervo_detalhe` também bate.
- TES-39 não tem pacote. Seus números são 98 e 47, e batem com a tabela do § 3.6: 38+25+21+8+4+1+1 = 98 processos; 23+7+11+3+3+0+0 = 47 com indício.
- O status de Walton no índice é igual ao do JSON em todas as linhas. As colunas que não deviam mudar não mudaram.

## 5. Item 9 (frases sem denominador): os achados

### P-01 · TES-16, formulação · **MÉDIO** · generalização
- **Ficha** (§ 1): "que acórdãos do TJBA no catálogo tratam como presumido (in re ipsa; 9 favoráveis e nenhuma contrária na mesma questão, recorte por palavra)".
- **Fonte**: os excertos dos 9 favoráveis no JSON da ficha. Só 0505335-84.2017 diz «DANO MORAL IN RE IPSA». Os outros 8 reconhecem o dano ou o ilícito sem qualificá-lo: «é passível de configurar a responsabilidade […] pelo dano moral», «é situação apta a gerar dano moral», «ILÍCITO», «caracteriza abuso de direito», «PROTESTO INDEVIDO», «bis in idem».
- **Leitura**: a frase antiga ("o TJBA tem tratado") não tinha número. A nova põe "9 favoráveis" ao lado de "presumido". Assim, a contagem passa a sustentar uma qualificação que só 1 excerto dá. A conclusão (dano moral devido) fica; o "presumido" não tem lastro de 9. **Texto certo** no `.json`.

### P-02 · TES-30, § 5 · **MÉDIO** · generalização contrária ao próprio material
- **Ficha**: "Nos casos do material, a restrição total dependeu de prova técnica".
- **Fonte**: o próprio § 3 da ficha. Em 0555629 a prova veio de consultas à Prefeitura («passou - em diversas oportunidades de consulta junto à própria Prefeitura Municipal de Salvador - por Análise de Orientação Prévia»). Em 0030481 a restrição é legal e está nomeada na ementa («ÁREA NÃO EDIFICÁVEL. APA LAGOAS E DUNAS DO ABAETÉ»). 8028737 é tutela sobre restrição «APARENTE». Laudo pericial só aparece no AREsp 1.723.597. A `fonte` da troca cita também 0526259, que é a contrária de restrição **parcial**.
- **Leitura**: a troca trocou "quase sempre" por "nos casos do material", mas a frase nova não é verdadeira para os casos do material. A conclusão ("exceção arriscada") fica de pé pelo AgInt no AREsp 2.594.742.

### P-03 · TES-08, argumento determinante · leve · contagem que a CQ1 desmente
- **Ficha** (§ 6): "A Sexta Turma Recursal decidiu, nos 11 processos do Subgrupo A (2020–2021), que a reclassificação unilateral não retroage para cobrar diferença de alíquota de tributo já recolhido".
- **Fonte**: a CQ1 da mesma ficha: «em 8 dos 11 processos do Subgrupo A o excerto ou o resumo do catálogo mostram esse fato; nos outros 3 (8001652-34.2019, 8024467-25.2019 e 8023580-41.2019) aparecem só a classificação errada ou a mudança ilícita». O excerto de 8001652 diz «TIPO CADASTRAL CLASSIFICADO COMO NÃO RESIDENCIAL, QUANDO NA VERDADE SE TRATA DE IMÓVEL RESIDENCIAL».
- **Walton**: o status `PLAUSIBLE` continua coerente, porque a CQ1 está respondida com a condição. Mas o texto do argumento é agora diferente do que o motor avaliou, e o motor não foi rodado de novo. A nota #162 declara isso ("status mantido").

### P-04 · TES-08, risco · leve · denominador de recorte só de favoráveis
- **Ficha** (§ 8): "(11 de 11 no Subgrupo A do catálogo, todos de 2020–2021; nada mais recente no material)".
- **Fonte**: § 3. O catálogo não tem contrário. O Subgrupo A tem 4 itens "(parcial)". Das contrárias: «Nenhuma enfrenta a reclassificação retroativa».
- **Leitura**: "11 de 11" parece uma taxa, mas o denominador é um recorte feito só de favoráveis. É o defeito que o item 9 do Codex aponta ("recorte não aleatório").

### P-05 e P-06 · TES-13, § 3 e § 5 · leve · generalização
- **Ficha**: "Nos 18 do catálogo, a extinção veio depois de despacho de emenda e decurso do prazo;" e "Nos acórdãos do catálogo, a extinção vem de sentença proferida depois de despacho de emenda não cumprido".
- **Fonte**: o pacote F1a, `teses[n=13].catalogo.favoraveis`.
  - O excerto fala de emenda, regularização ou intimação em 8 dos 18: 8113000, 0814634, 8084636, 8134774, 8138390, 8005591, 8034128 e 8150340.
  - Em mais 5, isso aparece só no campo `tese` do catálogo, que é registro derivado: 8052314, 8072571, 8084949, 8001698 e 8085144.
  - Nos outros 5, nem um nem outro: 8001880, 8001863, 8001878, 8001520 e 8136162.
- **Leitura**: a frase antiga era uma regra condicional ("prevalece quando houve"). A troca a transformou num fato sobre os 18. A CQ1 já dizia "18 [...] com despacho de emenda descumprido", mas essa afirmação é anterior e está fora destas trocas; o status não muda.

### P-07 e P-08 · TES-10, formulação (MD e JSON) · leve
- **MD**: "afastam por distinção (7 decisões na linha b do § 3, 1 delas do catálogo; sem denominador)". No texto do pacote, a distinção está expressa em 3 das 7: 8000948, 0502387 e 0503918. 8041504 (rescisória) não cita a Súmula 558 nem o Tema 876. A contagem 7 é da linha, não da distinção.
- **JSON**: a formulação continua com "o TJBA de 2025-2026 aplica [...] e afasta, por distinção". É a mesma generalização. A nota #164 diz que "a formulação do JSON não tinha a frase", o que é verdade na letra, mas não no sentido.

### P-09 · TES-39, § 3.1 · leve · ressalva
- "Negou nas 3 decisões de 2021 a 08/2024": a sequência da tabela é por processo. No mesmo intervalo houve também a apelação desfavorável de 8002112-79.2022 (02/04/2024), revertida nos embargos de 30/10/2024 (§ 3.5).
- **Conferem as demais contagens novas da TES-39**:
  - EMBASA 23/38, CODEBA 11/21, CONDER 3/4 e 37/63 (camada E).
  - COELBA 11 × 17 (§ 3.1: 1+0+4+2+4 e 7+1+4+1+4).
  - "4 seguintes, de 10/2024 a 07/2025".
  - Vias da COELBA 20/7/1/1 = 29 (§ 3.5).
  - Sobrestamentos de RE em 2025: 3 processos com nota na tabela.

### P-10 · TES-20, § 3 · leve · ressalva
- "Nos excertos que indicam o remédio (0333357-84.2017 e 8017145-83.2021)": o excerto de 0333357 só declara a inconstitucionalidade. A alíquota mínima está na anotação da ficha, "(parcial; a execução prossegue pela alíquota mínima)".

### P-11 e P-12 · residuais fora das trocas · leve · ressalva
- A nota #194 do índice diz que "as frases de taxa ou tendência sem denominador viraram contagem ou saíram". Ficaram duas:
  - TES-23 § 5: "É a via mais usada (0810931-21.2017; 0795148-52.2018; DJEN 8037526-12.2021)".
  - TES-20 § 5: "O resultado típico é o prosseguimento pela alíquota mínima".

### Trocas do item 9 que conferem (amostra do que foi recontado)

- **TES-04 #5**: as 4 contrárias de 2025-2026 (8071811 DJEN 12/11/2025; 8072682 DJEN 09/06/2025; 8032337 e 0795758 API 30/09/2026).
- **TES-08 #45/#46**: Subgrupo A, 11 processos, todos da 6ª TR, de 27/04/2020 (8001652) a 28/07/2021 (8134513); apart-hotel nomeado em 8006407 e 8024467.
- **TES-14 #53**: 5 de 6.
- **TES-16 #55/#56**: 8 da amostra e 6 da API, todos lides privadas de compra de imóvel.
- **TES-17 #57**: 8 processos de Salvador, 5 da 6ª TR.
- **TES-18 #58**: 12 contrárias, 9 de 2020 e 3 de 2026 da API; 13 favoráveis, 11 de 2023 a 2026; 0785219 de 2020 e 0812413 de 2021.
- **TES-21 #60**: 5 de 10.
- **TES-22 #61**: 9 de 10.
- **TES-23 #62**: 0810931 com declarações da Prefeitura; 8001107 com decreto municipal.
- **TES-24 #63/#64**: 7 TR e 1 Seções Cíveis Reunidas na amostra; 6 TR na API; 13 de 14.
- **TES-28 #67**: 8 lides privadas; 705 = 766 − 61.
- **TES-29 #69 a #71**: 13 processos; 12 da comarca de Lauro de Freitas (0150) e 1 consignação em Salvador.
- **TES-30 #72**: 7 de 8.
- **TES-31 #77**: 2 + 3 favoráveis de 2023 a 2026, 0 contrárias.
- **TES-32 #78**: 3 remessas, 1 apelação e 1 agravo em mandado de segurança, mais 8065174 em ação ordinária.
- **TES-33 #79**: 1 + 7.
- **TES-36 #80 a #82**: 10 contrárias e 1 parcial; 9 a favor do Município; 0507337 com o contribuinte vencido.

## 6. Walton

- Nenhum status mudou: JSON, MD e índice estão iguais aos originais.
- TES-21: entrar a Segunda Câmara no argumento determinante (#38) é coerente com o texto (0302531, comarca 0039, Segunda Câmara). A nota #39 justifica bem o `WEAK_UNANSWERED_CQ` mantido pela CQ3.
- TES-13: a CQ1 reescrita (#23) mantém a resposta.
- TES-08: ver P-03.
- Ressalva comum: nas três fichas o texto do argumento ou da CQ mudou depois da rodada do motor. "Status devolvido pelo motor" se refere à versão anterior. As notas de revisão declaram isso; não é erro, é proveniência.

## 7. Proveniência (sem defeito)

- A troca #7 registra um `para` que a troca #195 alterou depois ("de 10/01/2023" → "(data do banco: 10/01/2023; o texto não traz data)"). Reposto em ordem, o registro reproduz o arquivo.
- As notas finais (#160 a #194) resumem corretamente as trocas de cada ficha. A única imprecisão é a da #164 (P-08).

## 8. O que não foi verificado

- O inteiro teor dos acórdãos do TJBA: só o texto de `ementas-candidatos.jsonl` e dos pacotes.
- Afirmações anteriores às trocas, como a CQ1 da TES-13 e a classificação de "lides privadas" já no § 3 da TES-28. Só as olhei na medida em que uma troca se apoia nelas.
- Os itens 2 e 4 a 10 do Codex.
