---
tipo: relatorio-de-pesquisa
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: draft
---

# Relatório E4-1: eixo imunidade (IPTU-04), TES-001

**Estado:** triagem T2 e leitura T3 concluídas e harmonizadas; tabela da TES-001 gerada. O dossiê v3 (Walton/Élenchos → antialucinação → Codex) **ainda não foi feito**. Revisão humana: nenhuma até aqui.

## 1. Funil (trilha neutra Q-NEUTRA-01, indício IPTU-04)
| Etapa | N | Onde |
|---|---|---|
| Candidatos com indício IPTU-04 (TJBA acervo local 446 + API 2026 11) | 457 | `dados/candidatos-*.jsonl` |
| Já classificados no piloto | 5 | `dados/decisoes/` |
| Lote E4-IPTU04 | 452 | `estado/lote-E4-IPTU04.json` |
| T2 (Sonnet; calibrada no piloto): pertinentes / dúvidas / excluídos | 402 / 27 / 23 | `auditoria/triagem-T2-E4-IPTU04.jsonl`, `auditoria/revisao-T2-E4-IPTU04.jsonl` |
| Para a T3, distintos por texto (36 grupos de gêmeos) | 391 | `estado/t3/E4-IPTU04-fatias.json` |
| Fatia alíneas b/c por indício (lida agora) / alínea a (TES-002, não lida) / indefinida | 233 / 134 / 24 | idem |
| T3 Opus: registros validados (5 do teste + 228 da onda) | 233 | `dados/decisoes/`, `estado/t3/respostas-leitores.jsonl` |
| Após harmonização: pendentes (texto só com relatório) / excluídos na T3 | 11 / 9 | `auditoria/harmonizacao-t3.jsonl` |
| Com questão de IPTU-04: atos / **processos** | 199 / **146** | `analises/teses/TES-001-tabela-v1.json` |
| Processos de alínea b ou c (sem a) / com exame (mérito, processual, cautelar) / só mérito | 109 / **100** / 82 | idem |

## 2. Achados de método
- **O indício IPTU-04 da T1 é sobre-inclusivo.** Pega imunidade de outros tributos: 20 das 23 exclusões da T2 são de ITBI na integralização de capital ou de ISS da CODEBA e da EMBASA.
- **A alínea por regex era só ordem de leitura.** A leitura T3 achou 37 processos de alínea *a* dentro da fatia "b/c" (a linha COELBA, Temas 385, 437 e 1.297). Eles vão para a TES-002.
- **Harmonização por regra** (`metodologia/harmonizacao-t3-v1.md`). Os leitores cegos divergiram em três pontos:
  - recurso inadmitido (28 questões passaram a `sem_exame`);
  - texto só com relatório (11 registros passaram a `pendente`);
  - exclusões fora do brief (revistas uma a uma).
- **Unidade = processo.** Embargos de declaração, agravo interno e admissibilidade do mesmo processo contam uma vez.

## 3. TES-001: ônus da destinação, alíneas b e c (100 processos com exame; 82 só de mérito)
Ônus = determinação do leitor Opus; das 55 linhas "Município", só 4 o leitor marcou como implícito ou transcrito. Via processual = indício por código no texto, conferido numa amostra de 6. Alínea = leitura T3; 7 casos mistos foram revistos à mão e eram b ou c.

| Alínea | Ônus no Município | Ônus no contribuinte | Misto | Não tratado | Outro |
|---|---|---|---|---|---|
| **b** (templo), 39 | 28 (25 favoráveis, 2 desfavoráveis, 1 sem exame) | **1** (favorável; Turma Recursal; "ônus não discutido") | 0 | 10 (7 favoráveis) | 0 |
| **c** (entidade), 59 | 27 (26 favoráveis) | **8** (3 favoráveis, 5 desfavoráveis) | 2 | 21 (16 favoráveis) | 1 |
| b+c, 2 | 0 | 0 | 0 | 2 (favoráveis) | 0 |

- **Templo (alínea b):** quando o tribunal fala do ônus, ele é do Município, pela presunção de destinação. A única exceção é inferida, numa decisão de Turma Recursal em que o ônus não foi discutido.
- **Entidade (alínea c):** a maioria segue a mesma presunção. Há uma **linha minoritária** que põe no contribuinte a prova dos requisitos do art. 14 do CTN.
  - Esses casos estão espalhados: 2ª Câmara, 4 casos (2020 a 2024); 3ª, 2 (2021 e 2025); 1ª, 1 (2025); 5ª, 1 (2025).
  - **As 5 derrotas dessa linha são todas em exceção de pré-executividade**, com prova pré-constituída insuficiente e Súmula 393 do STJ.
  - As 3 vitórias são de entidade que provou os requisitos por documento.
  - Lista em `TES-001-tabela-v1.csv`.
- **A hipótese "exceção → ônus do contribuinte" não vale como regra.** Nas exceções de alínea b ou c, o ônus ficou com o Município em 24 processos, com o contribuinte em 7 e não foi tratado em 14. O que se vê é mais estreito: na alínea c, se o ônus cai no contribuinte e a via é a exceção, ele perde.
- **Associação ônus × resultado:** com ônus no Município, o contribuinte ganha em 51 de 55 casos; com ônus no contribuinte, em 4 de 9. Isso **não é causal**, porque o tribunal enuncia o ônus para justificar o resultado.
- **Embargos de declaração rejeitados** (classificados como "processual") não contam como derrota no mérito da imunidade. A contagem só de mérito (82) fica ao lado, para isso.
- **Não é taxa de êxito do TJBA.** O universo é o indício IPTU-04 da trilha neutra, com estas limitações:
  - acervo local vai até 12/2025;
  - a API de 2026 subconta;
  - a maioria dos textos tem só ementa e dispositivo;
  - o 1º grau está pendente.

## 4. Pontos para o dossiê v3 (achados dos leitores)
- **Tema 437 aplicado a casos de alínea c:** a 2ª Vice-Presidência aplicou o Tema 437 (alínea a) a casos de alínea c que a câmara havia distinguido (389e59d02135, 46bd27ed00bb, 39ea588186c6). São os casos do Abrigo do Salvador.
- **Grupo MMS Participações / Abrigo do Salvador:** a arrendatária é a contribuinte e o fundamento é a SV 52. Conta como uma linha de casos, não como precedentes independentes.
- **Derrota de templo com imóvel ocioso há 10 anos** (2720a57a2069). Limite da presunção.
- **Imunidade × taxas:** a imunidade não alcança a TRSD, a COSIP nem a TCL (vários casos). Há uma decisão (bbd590893927) que extinguiu a TRSD pela imunidade, sem fundamento próprio.
- **Inteiro teor:** 11 pendentes (só relatório), mais os acórdãos recorridos dos atos de admissibilidade. Vão para a fila da PDPJ.

## 5. Custos
- **T2 Sonnet:** 10 lotes, cerca de 220 mil tokens por lote.
- **T3 Opus:** 36 leitores, de 140 a 220 mil tokens cada (cerca de 6 M no total), em cerca de 1 h com 5 em paralelo.
