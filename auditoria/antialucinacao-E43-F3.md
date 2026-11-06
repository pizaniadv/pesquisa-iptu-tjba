---
tipo: auditoria-antialucinacao
data: 2026-11-06
produzido-por: papel-antialucinacao (Opus 5.5), conferência independente
versao-core: 1.0
status: vigente
alvo: analises/fichas/TES-08, TES-09, TES-14, TES-20, TES-21, TES-22, TES-33 (.md e .json), lote F3 (família F3_quantificacao)
destino-do-alvo: interno (pesquisa; nada a renderizar nem enviar)
regra: estado/brief-antialucinacao-fichas-v1.md
metodo: conferência manual de cada afirmação contra a fonte própria (pacote estado/E4-3/pacote-F3_quantificacao.json; Cognitio para precedentes e leis), no formato do precedente auditoria/antialucinacao-TES-001-v1.md
saida-por-codigo: auditoria/antialucinacao-E43-F3.json (30 entradas; cada `de` conferido por código como trecho único e exato da ficha)
---

# Antialucinação — lote F3 (quantificação): TES-08, 09, 14, 20, 21, 22 e 33

## 1. Veredito

**Nada grave nas sete fichas.** Não há citação inventada nem aspas falsas. Nenhum número muda uma conclusão.

O que foi conferido e bate:
- Todos os precedentes qualificados citados existem (Temas 211, 226, 523, 155 e 1084 do STF; Súmula 668 do STF; SV 10; Súmulas 160 e 393 do STJ; Temas 375 e 1113 do STJ), e toda tese ou enunciado transcrito entre aspas é literal.
- Todos os números de processo do TJBA estão no pacote, e todas as datas batem com ele. Isso foi conferido por código, linha a linha.
- As contagens dos JSON (`n_catalogo_fav`, `n_acervo` = processos, `contrarias_ids`, `excertos`) batem com o pacote e com o MD.

Há **um ponto médio**, que convém aplicar antes de usar a TES-08. A ficha diz que não achou precedente qualificado sobre a irretroatividade da reclassificação cadastral. Ele existe e está no Cognitio: **STJ, Tema 387 (REsp 1.130.545)**. É ele que decide justamente a exceção que a ficha deixa aberta (revisão por fato não conhecido, CTN, art. 149, VIII). Fora isso, há 29 itens leves: contagens e rótulos imprecisos, duas paráfrases que ampliam o excerto e `[A CONFERIR]` resolvidos com a referência certa (11 ao todo, contando o médio).

| Ficha | Pior gravidade | `[A CONFERIR]` resolvidos | Veredito |
|---|---|---|---|
| TES-08 | médio | 3 de 4 | aprovada com correções (aplicar A-08.1) |
| TES-09 | leve | 2 de 4 | aprovada com ressalvas |
| TES-14 | leve | 1 de 2 | aprovada com ressalvas |
| TES-20 | leve | 2 de 2 | aprovada com ressalvas |
| TES-21 | leve | 0 de 0 | aprovada com ressalvas |
| TES-22 | leve | 2 de 3 | aprovada com ressalvas |
| TES-33 | leve | 1 de 1 | aprovada com ressalvas |

"Resolvido" quer dizer que a referência foi localizada e conferida: a norma ou o precedente existe e diz o que se afirma. Quando o `[A CONFERIR]` pergunta se o acórdão do TJBA cita aquele artigo, a resposta continua dependendo do inteiro teor. Isso fica como limite declarado, que as fichas já fazem.

## 2. Afirmações problemáticas

### TES-08 — Alíquota e seletividade

**A-08.1 · MÉDIO · `[A CONFERIR]` resolvido (diverge do "não achado") · alcance → MIJ**
- **Ficha (§ 4):** "Para a irretroatividade da reclassificação não há precedente qualificado no pacote nem foi achado no Cognitio nesta leitura: [A CONFERIR]."
- **Fonte:** Cognitio `STJ:paradigmas:Tema-387`, REsp 1.130.545, rel. Min. Luiz Fux, 2010. Questão: "alteração de dados cadastrais do imóvel não constitui erro de fato apto a ensejar a revisão do lançamento de IPTU, à luz do disposto nos artigos 146 e 149, do CTN". Tese: "A retificação de dados cadastrais do imóvel, após a constituição do crédito tributário, autoriza a revisão do lançamento pela autoridade administrativa (desde que não extinto o direito potestativo da Fazenda Pública pelo decurso do prazo decadencial), quando decorrer da apreciação de fato não conhecido por ocasião do lançamento anterior, ex vi do disposto no artigo 149, inciso VIII, do CTN." Basanos: `existe_no_indice`.
- **Por que importa:** a contra-analogia do § 6 diz: "O pacote não traz decisão que enfrente isso". Também a CQ3 fica em branco. Mas existe precedente vinculante sobre exatamente essa exceção: o Município pode rever para trás se a reclassificação corrigir **fato não conhecido**; não pode, se for **mudança de critério jurídico** (CTN, art. 146). O Walton continua coerente (`PLAUSIBLE`, porque o ônus da CQ3 é de quem questiona). Mas o "risco baixo" do § 8 precisa dessa ressalva. Em qual dos dois lados cai o apart-hotel é juízo de alcance, e fica para o MIJ.
- **Médio, não grave:** a ficha não afirma nada falso sobre o pacote; omite um precedente que estava ao alcance. A correção da contra-analogia vai no JSON, como item leve.

**A-08.2 · LEVE · generalização (CQ1).** A ficha diz "os 11 processos do Subgrupo A têm esse fato" (reclassificação para trás sobre exercício pago). Pela fonte, em 8 dos 11 o excerto ou o resumo do catálogo mostram a retroação ou o tributo recolhido. Em 8001652-34.2019 ("TIPO CADASTRAL CLASSIFICADO COMO NÃO RESIDENCIAL..."; resumo: "retificação do lançamento") e em 8024467-25.2019 e 8023580-41.2019 ("MUDANÇA ILÍCITA..."), não há menção a tributo já pago.

**A-08.3 · LEVE · ressalva de órgão.** A ficha diz "0506436-75.2015 — 2ª Vice-Presidência". O texto diz isso, mas o pacote rotula o processo como "ÓRGÃO ESPECIAL". A ficha está certa pelo texto; basta registrar o rótulo divergente, como ela já faz em outros casos ("rotulado").

### TES-09 — Base de cálculo e valor venal

**A-09.1 · LEVE · número.** A ficha diz "os 7 vistos são inventários e ITIV". O pacote traz **6** itens do DJEN: 4 inventários (8211201, 8001364, 8002541, 8001221) e 2 ITIV de Lauro de Freitas (8013724, 8019231).

**A-09.2 · LEVE · origem.** A ficha diz "8 processos: 4 do catálogo, 4 da amostra do acervo". Só 3 vêm da amostra da tese 9 (0511252, 0507288, 8007407). O 0575556-11.2015 está na amostra da **tese 22**, e a própria ficha o diz no item ("seção da TES-22").

**A-09.3 · LEVE · sem fonte.** A ficha diz "perícia complexa pode afastar o rito" (Juizado). Nenhum item do pacote trata disso. Ou se marca como não conferido, ou se tira.

**Nota (sem entrada no JSON).** O Tema 387 do STJ (A-08.1) também toca a TES-09: o erro de padrão construtivo e o erro de fator de localização são dados cadastrais. A tese favorável da TES-09 é o contribuinte provando o erro, não o Fisco revendo. A relação entre os dois fica para o MIJ.

### TES-14 — Majoração por decreto

**A-14.1 · LEVE · composição.** A ficha diz "3 de Salvador sobre aumento desproporcional ou acima da trava legal". A soma (10 + 2 + 1 + 3 = 16) só fecha com o **8013132-09.2019** entre os três. Esse caso é de **delegação ao Executivo** ("TRANSFERÊNCIA AO PODER EXECUTIVO PARA FIXAÇÃO DA BASE DE CÁLCULO DO IPTU"), e não de aumento ou trava. Os outros dois são 0568211-86.2018 e 0552379-13.2018.

**A-14.2 · LEVE · generalização.** A ficha diz "o município é nomeado nos excertos". Só 3 dos 10 excertos nomeiam Vitória da Conquista (0500256, 0010621, 0003051). Nos demais, a ligação é pelo número da comarca (0274).

**A-14.3 · LEVE.** A ficha diz que os 6 itens do portal tratam de "prescrição, imunidade e ITR, salvo um". Falta um assunto: 8006269-12.2025 é extinção por falta de CPF do executado.

**A-14.4 · LEVE · ressalva de fonte.** O § 2 cita o art. 229 do RITJBA, o incidente 0005785-38.2007 e o CTN, art. 97, II c/c § 1º. Tudo isso está no pacote, mas na **seção da TES-21** (0003051-51.2006, 0003615-30.2006, 0006835-36.2006), não na da TES-14. E o número do incidente aparece com dois sufixos: ".805.0274" em 0003051 e ".805.0774" em 0003615. Convém conferir antes de citar.

### TES-20 — Progressividade

**A-20.1 · LEVE · deduplicação indevida + órgão.** A ficha diz que 0506326-08.2017 e 0510074-19.2015 foram "contadas como uma só por cautela". As ementas são idênticas, mas as **partes diferem**: Hotel Bahia do Sol Ltda × Município, num caso; Jorge Oliveira Sampaio × Município, no outro. São dois processos com ementa-padrão, não o mesmo julgado. O brief manda contar processos, e então as contrárias são **10**, não 9. Além disso, o 0506326 está rotulado "2ª Vice-Presidência" no pacote, mas o texto diz "Primeira Câmara Cível".

**Nota (verde, sem correção).** O "Risco de distinção" do § 4 está **confirmado no teor**. A tese longa do RE 602.347 fala de "fato gerador ocorrido em período anterior ao advento da EC 29/2000"; o recurso foi "conhecido e provido", "vencido o Ministro Marco Aurélio" (Cognitio `STF:paradigmas-teor:226-10676798`, p. 1-3). A observação de que o TJBA estende o Tema 226 a leis posteriores à EC 29 é correta.

### TES-21 — Planta genérica de valores

**A-21.1 · LEVE.** A ficha diz "Quase metade do catálogo é tutela em agravo". São 5 de 10, ou seja, metade.

**A-21.2 · LEVE · omissão no risco.** A ficha diz "Terceira, Quarta e Quinta Câmaras concederam" a tutela. A Primeira Câmara também suspendeu a exigibilidade em 2020 (8015659-34.2019), embora o município não seja identificado no excerto. A divergência da Primeira Câmara é de mérito (2024-2025), não de tutela.

### TES-22 — Área tributável

**A-22.1 · LEVE · generalização.** A ficha diz "7 de erro de metragem provado por laudo". Em 5 deles o excerto ou o resumo cita laudo ou perícia. Em 8033822-59.2019 e 8036110-77.2019, só aparece a "CORREÇÃO NA METRAGEM".

**A-22.2 · LEVE.** O título "Na justiça comum" abrange o 8090444-22.2023, que é da **Sexta Turma Recursal**.

**A-22.3 · LEVE.** A ficha diz "o catálogo é de 2020-2021". O 8138690-20.2021 é de 11/04/2024, e o § 3 da própria ficha dá o período certo.

**A-22.4 · LEVE · ressalva.** A lacuna "precedente qualificado sobre erro de metragem" está certa no sentido favorável ao contribuinte. No sentido inverso, existe o Tema 387 do STJ (A-08.1): o Fisco pode rever o lançamento por retificação cadastral de fato não conhecido. Serve para a contra-analogia (alcance: MIJ).

### TES-33 — Erro de cálculo do limite máximo (trava)

**A-33.1 · LEVE · paráfrase com inferência.** A ficha diz "a Quarta Câmara afastou as travas para o exercício discutido". A ementa de 0508495-31.2018 diz "INAPLICABILIDADE DA LEGISLAÇÃO MUNICIPAL QUANTO ÀS "TRAVAS" NOS VALORES DE COBRANÇA". A expressão "do exercício discutido" aparece em outra frase: "NORMAS VERGASTADAS NÃO ESTABELECEM A TABELA DE ALÍQUOTAS PARA O CÁLCULO DO IPTU DO EXERCÍCIO DISCUTIDO NA AÇÃO MANDAMENTAL". A ligação entre as duas frases é inferência. Que o motivo não está no trecho, a ficha já declara.

## 3. Conferido e sustentado (verde)

| Afirmação | Fonte e verificação |
|---|---|
| Todos os 152 números de processo citados nas sete fichas (24 + 33 + 23 + 25 + 24 + 14 + 9 excertos) | presentes no pacote; data de cada bullet = `julgamento`/`publicacao`/`data` do pacote (script, zero divergências) |
| Contagens de catálogo, acervo (decisões, processos, indício), portal e DJEN | pacote, teses 8, 9, 14, 20, 21, 22 e 33; JSON `n_catalogo_fav` e `n_acervo` = processos, idênticos |
| Câmaras e período de cada ficha | contagem por `orgao` e min/max de `julgamento` no catálogo; todas batem (Sexta TR 12/16 na TES-08; 9/10 na TES-22 etc.) |
| Recorte "perícia"/"área do imóvel" (TES-22) e "limite máximo"/"trava"/"teto" (TES-33) | `estado/E4-3/teses.json`, campo `regex` das teses 22 e 33 |
| TES-08 e TES-20: Tema 523, tese literal; "não se confunde com o estabelecimento de alíquotas progressivas" | Cognitio `STF:paradigmas-teor:523-752973153`, p. 1-2 (Barroso, 2020, vencido Marco Aurélio) |
| TES-08 e TES-20: Tema 226, tese curta e tese longa (aspas) | PANGEA `stf-rg-226`; Cognitio `STF:paradigmas-teor:226-10676798`, p. 1-3 |
| TES-09, 14, 21 e 33: Tema 211, tese literal; TES-14: ementa do RE 648.245 entre aspas | PANGEA `stf-rg-211`; Cognitio `STF:paradigmas-teor:211-5323879`, p. 1, item 6, literal |
| Súmula 160 do STJ (TES-14, 21) | Cognitio `STJ:sumulas:160`, literal; PANGEA `stj-sum-160` "Vigente" (evidencias/pangea-iptu.jsonl) |
| Súmula 393 do STJ (TES-09, 22) | Cognitio `STJ:sumulas:393`, literal |
| Tema 155 (AI 712.743) e Súmula 668 (TES-20) | Cognitio `STF:repercussao_geral:tema-155` e `STF:sumulas:668`, textos idênticos; teor do RE 602.347: "AI-QO-RG 712.743, de relatoria da Ministra Ellen Gracie" |
| Tema 1084 (ARE 1.245.097), tese literal (TES-21) | Cognitio `STF:repercussao_geral:tema-1084`; PANGEA `stf-rg-1084` |
| SV 10 (TES-21, 8035808-60.2021) | Basanos `existe_no_indice`; ementa de 8035808 no pacote: "SÚMULA VINCULANTE Nº 10. AUTOS ENCAMINHADOS AO TRIBUNAL PLENO." |
| TES-08: art. 73 da Lei 7.186/2006; Leis 4.279/90 e 5.325; IN 12/2013; arts. 156, § 1º, I, e 182, § 4º, II | pacote: 0007301 (art. 73), 0129121 (Leis 4.279/90 e 5.325), 0522213 (IN 12/2013), 0532317 ("156, § 1º, I e 182, § 4º, II") |
| TES-09: CTRMS, art. 65 (0560744); CTN, art. 173, II (0577832); art. 67, I e CPC, art. 480 (resumos do catálogo) | pacote, ementas e campo `tese` do catálogo |
| TES-20: CTN, art. 170 e Lei 7.186/2006, art. 22 "numa decisão monocrática da busca do portal" | pacote, tese 8, `tjba_api` 0330025-85.2012 (DECISAO_MONOCRATICA) |
| TES-21: Lei 1.293/2013, arts. 83 e 84; Lei 1.359/2014; IN SEFAZ 33/2015; CTN, art. 151, V (resumo de 8031079) | pacote: 8010680, 8035808, 0507524, catálogo |
| Reapontamentos "rotulado 2ª Vice-Presidência / Órgão Especial" (TES-20 0507452; TES-21 8001720 e 0500927; TES-22 8004702) | cabeçalho do texto no pacote indica Segunda, Terceira e Primeira Câmaras: as ressalvas da ficha estão certas |
| Walton: TES-08, 09, 14, 20 e 22 `PLAUSIBLE`; TES-21 e 33 `WEAK_UNANSWERED_CQ` | coerentes com as tabelas de CQ: nas `PLAUSIBLE`, as CQ abertas têm ônus do questionador; nas `WEAK`, a CQ pendente (TES-21, CQ3, Primeira Câmara contrária; TES-33, CQ2, 0508495) está mesmo sem resposta no material |

## 4. Itens `[A CONFERIR]`

| Ficha | Item | Resultado | Referência certa / limite |
|---|---|---|---|
| TES-08 | art. da CF na vedação ao confisco (0519683) | **confere (norma)** | CF, art. 150, IV, "utilizar tributo com efeito de confisco"; se o acórdão o cita: teor TJBA (limite) |
| TES-08 | art. do CTN da irretroatividade da reclassificação (§ 2 e § 7) | **nao_localizado** (limite declarado) | candidato CTN, art. 146 (redação LC 236/2026), mas o artigo usado pela Sexta TR depende do teor |
| TES-08 | art. do CPC da readequação do ônus (0311778) | **confere (norma)** | CPC, art. 373, § 1º; citação no acórdão: teor (limite) |
| TES-08 | precedente qualificado da irretroatividade | **diverge** (existe) | STJ, Tema 387, REsp 1.130.545 (A-08.1) |
| TES-09 | CTN, art. 146 no teor de 0758800 | **nao_localizado** (limite declarado) | depende do inteiro teor do TJBA |
| TES-09 | artigo do ônus do autor nas contrárias (8020927) | **confere (norma)** | CPC, art. 373, I; citação: teor (limite) |
| TES-09 | CTRMS, art. 67, I (8054259) | **nao_localizado** | lei municipal não alcançada; a ficha declara |
| TES-09 | STJ, Tema 1113 | **confere** | Cognitio `STJ:paradigmas:Tema-1113`, REsp 1.937.821, Gurgel de Faria, 2022; tese (a) literal |
| TES-14 | art. do CTN da suspensão por tutela e depósito | **confere (norma)** | CTN, art. 151, II e V (V na redação da LC 236/2026: "liminar ou de tutela provisória"); inciso usado: teor (limite) |
| TES-14 | Lei 9.279/2017 (alteração da trava) | **nao_localizado** | lei municipal; só o resumo do catálogo de 0552379 a menciona; a ficha declara |
| TES-20 | artigos da legalidade e da anterioridade (0507390 etc.) | **confere (norma)** | CF, art. 150, I e III, *c*; o § 1º do art. 150 tira da noventena só a base de cálculo do IPTU, não a alíquota |
| TES-20 | STF, ADI 2732 | **confere** (nível: ementa do espelho) | PANGEA `stf-adi-2732` = Cognitio `STF:pangea:stf-adi-2732`: "Ação julgada improcedente", unânime, Plenário, 07/10/2015. O espelho erra a data da EC 29 ("2003"; o certo é 13/09/2000) e o artigo ("185, § 4º"; o certo é 182, § 4º, II). Basanos: `fora_do_indice` (não está no índice próprio) |
| TES-22 | art. do CTN da nulidade por erro de fato | **nao_localizado** (limite declarado) | candidatos 142 e 149, VIII; depende do teor |
| TES-22 | CPC, art. 373 (8006244) | **confere (norma)** | CPC, art. 373, caput e § 1º; parágrafo usado: teor (limite) |
| TES-22 | STJ, Tema 375 | **confere** | Cognitio `STJ:paradigmas:Tema-375`, REsp 1.133.027, 2010; tese literal no JSON; alcance para erro de área: MIJ |
| TES-33 | CF, art. 150, I e CTN, art. 97 | **confere (norma)** | textos conferidos; CTN, art. 97, § 2º (atualização monetária não é majoração) é o pano de fundo da trava pelo IPCA-E |
| TES-21 | (nenhum `[A CONFERIR]`) | — | — |

Os demais limites ("texto da lei municipal não lido", "inteiro teor não lido", incidente do Pleno não lido) estão declarados nas sete fichas, nas seções 2 e 7.

## 5. O que não foi verificado

- O inteiro teor dos acórdãos do TJBA: não está no laboratório (`evidencias/extracoes` só tem 1 dos 154 ids de catálogo e amostra do pacote). Conferi a paráfrase só contra o excerto, a ementa (até 1.500 caracteres) e o resumo do catálogo. A literalidade dos excertos não foi refeita aqui: ela já está em `auditoria/conferencia-fichas-e43.jsonl` (602/602).
- As páginas de Walton, Reed e Macagno (2008) citadas nas fichas (p. 310, 315, 319, 331, 343 e 344) e as saídas do Élenchos.
- O teor de Tema 155, Tema 1084, Tema 375, Tema 387 e Tema 1113: li o cadastro (questão e tese), não o acórdão. Tema 211, 226 e 523 foram lidos no teor (p. 1 a 3).
- A situação atual de cada precedente no portal do STF ou do STJ (cancelamento, modulação). O acervo avisa que "não prova vigência atual".
- As leis municipais (Salvador, Vitória da Conquista, Camaçari, Porto Seguro) e os incidentes e ADIs do Pleno do TJBA (0005785-38.2007; 0343261-07.2012; 0002526-37.2014 e conexas).
- Os textos de lei vieram do compilado do Planalto no Cognitio (status "draft"). Não abri o Planalto diretamente. CTN, arts. 146 e 151, aparecem com redação da LC 236/2026; vale conferir a data de vigência dessa redação para fatos geradores antigos.
- O MIJ não foi feito. Ficam para ele: o alcance do Tema 387 na TES-08 (apart-hotel: fato não conhecido ou mudança de critério?), na TES-09 e na TES-22; o do Tema 375 na TES-22; o do Tema 226 para leis posteriores à EC 29 na TES-20.
