---
tipo: protocolo-de-pesquisa
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: superado
versao: v1
congelado_em: 2026-11-05 (antes da coleta extensiva; hora registrada antes por engano como 19:00)
superado_por: protocolo-v2.md
---

# Protocolo v1 — PESQUISA-IPTU

Congelado antes da coleta extensiva. Mudança posterior gera v2 com justificativa em `auditoria/correcoes.jsonl`; nunca se altera em silêncio para melhorar resultado aparente.

## 1. Perguntas
As oito do prompt-mestre (§ 1): questões com solução favorável; fatos, normas, exercícios e provas determinantes; benefício e extensão; natureza (provisória, mérito, processual, encargos); trajetória; relação com TJBA/STJ/STF; condições de transposição; distribuições descritivas com denominador.

## 2. Unidade de análise
- **Registro canônico = decisão** (ato judicial). Questões decididas ficam dentro dela, cada uma com ID próprio (`<id-decisao>#Qn`).
- **chave_questao_comparavel** = `CNJ-raiz | eixo | exercício(s) | pedido` — só vinculada quando a equivalência tem fundamento.
- Indicador declara a unidade (documento, decisão, processo, litígio, questão, tese).

## 3. Trilhas
| Trilha | Fontes | Entra no denominador? |
|---|---|---|
| **N — neutra sistemática** | Varredura integral `rg` dos JSONL de acervo local (TJBA, STJ, STF) e FTS do PANGEA; moldura DataJud (assunto 5952) com sorteio | Sim, no recorte de cada fonte |
| **D — dirigida** | Cognitio `buscar_juris_struct` com termos de resultado; DJEN por frase; portais; citações | Não (salvo se também achada em N; preservam-se as duas procedências) |
| **I — interna** | corpus_busca, Clients-Files, 60-Library/teses | Não; pista |

## 4. Vocabulário neutro (consulta Q-NEUTRA-01)
Famílias, sem termo de resultado: `F1` sigla (`\biptus?\b`, `i.p.t.u`); `F2` "predial e territorial urban"; `F3` "propriedade predial"; `F4` "imposto predial"; `F5` "imposto territorial urbano". Insensível a caixa; sobre a linha JSON inteira (ementa + conteúdo + metadados). Recibo por arquivo em `auditoria/buscas.jsonl`.

Termos dirigidos (só trilha D): inexigibilidade, nulidade do lançamento/CDA, prescrição, imunidade, isenção, repetição de indébito, exceção de pré-executividade acolhida, segurança concedida, sentença mantida.

## 5. Funil e critérios
1. **Bruto**: linha que casa Q-NEUTRA-01.
2. **Candidato**: deduplicado por `sha256_linha` e por identidade judicial (`numeroProcesso` + `tipoDecisao` + `dataJulgamento` + `orgao`); republicação ≠ novo julgamento.
3. **Pertinência (triagem T1, determinística)**: separa *objeto* (IPTU é questão tributária decidida) de *menção* (EXC-07: IPTU como dado de fato). Regras em `scripts/triar.py`, com motivo por registro.
4. **Elegível** (T2, Sonnet sobre ementa + dispositivo): pertinência confirmada, eixo(s), direção indiciária por questão. Indício, não classificação.
5. **Classificado** (T3, Opus sobre inteiro teor): questões, resultado por questão, natureza do benefício, provisoriedade, efeito sobre o ato anterior, fundamento determinante com excerto e localizador.
6. **Verificado**: excertos conferidos no original (offset no texto com hash); decisão central passa pela antialucinação.

Pendente (não some da base): sem inteiro teor suficiente, OCR ruim, dispositivo não classificável — fica com motivo e com o documento que falta.

## 6. 1º grau (moldura DataJud)
- **Moldura A**: TJBA, assunto 5952, todas as classes menos Execução Fiscal (classe 1116). **Moldura B**: Execução Fiscal (660 mil; só contagem até a v2).
- Sorteio estratificado por classe (procedimento comum, juizado da Fazenda, MS, embargos à EF, outros) e ano de ajuizamento (2021+), semente fixa registrada; para cada sorteado, DJEN por `numeroProcesso` → sentença publicada; PDPJ quando o DJEN não trouxer o teor.
- Proporção do 1º grau vale só para a amostra da moldura, com o ruído de cadastro de assunto declarado.

## 7. Resultado e capítulos
Por questão: favorável integral · favorável parcial · desfavorável · sem exame · indeterminável. Campos independentes: matéria examinada; resultado processual; natureza do benefício; provisoriedade; alcance; efeito sobre o ato anterior; situação recursal. "Provido/desprovido" sozinho não classifica; admissibilidade ≠ mérito; tutela ≠ definitivo; extinção processual ≠ inexistência da obrigação; vitória sobre taxa ≠ vitória sobre IPTU.

## 8. Jurimetria
Descritiva. F/(F+P+D) e (F+P)/(F+P+D) sobre unidades classificáveis que examinaram a questão; sem exame e indeterminável informados à parte; denominador zero = não calculável. Regra de seleção longitudinal: última decisão conhecida por `chave_questao_comparavel` × instância, preservada a trajetória. Instâncias diferentes não somam como êxitos independentes. Sem ranking de julgador, sem inferência causal.

## 9. Walton e Élenchos
Cada dossiê de tese traz a tabela argumento · esquema (`ARG.SCH.WRM08.*`) · perguntas críticas com ônus · resposta (com localizador) · contra-analogia. Avaliação por `elenchos_evaluate_scheme`; o motor confere forma, não Direito. Os argumentos do Município também passam pelos esquemas. As afirmações jurimétricas do relatório passam pelos esquemas de exemplo/sinal/correlação.

## 10. Revisão
Revisão por agente = automatizada; humana só quando o titular ler. Codex revisa com a árvore parada. Erro relevante → mecanismo identificado, revisão ampliada dos suscetíveis, regeneração dos dependentes, trilha preservada.
