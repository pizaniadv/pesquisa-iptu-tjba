---
tipo: relatorio-de-rodada
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: draft
rodada: 1 (E1 reconhecimento + E2 varredura neutra + E3 piloto)
protocolo: v2
---

# Rodada 1 — PESQUISA-IPTU (05/11/2026)

## 1. O que foi pesquisado (trilha neutra Q-NEUTRA-01, sem termo de resultado)
| Fonte | Intervalo efetivamente percorrido | Registros percorridos | Acertos | Candidatos únicos |
|---|---|---|---|---|
| <ACERVO>/JURISPRUDÊNCIAS-TJBA (2º grau + TR) | 2020-01-01 a 2025-12-31 (72 arquivos mensais) | 2.101.322 | 11.893 | 9.981 |
| API TJBA (delta) | 2026-01-01 a 2026-11-05, por dia (309 dias) | 135.102 | 264 | 232 |
| <ACERVO>/STJ (espelhos locais) | o acervo local inteiro | 135.625 | 308 | 308 |
| <ACERVO>/STF (acórdãos indexados, RG, súmulas) | o acervo local inteiro | 29.423 | 60 | 60 |
| <ACERVO>/PANGEA (BNP/CNJ) | espelho de 21/07/2026 | 13.776 | 51 | — |
| <ACERVO>/CMT-Salvador (administrativo) | o acervo local inteiro | 1.635 | 1.074 | 981 |
| DataJud — moldura do 1º grau (assunto 5952, sem Execução Fiscal) | ajuizamentos de qualquer data | 43.219 esperados | em coleta no servidor de coleta | — |

**Leitura de cobertura:**
- **A API do TJBA não é completa:** 03/2025 trouxe 8.407 registros na API × 31.044 em acervo local, e 10/09/2026 só 80. O delta de 2026 é **parcial**: densidade de 0,20% de acertos, contra 0,57% em acervo local.
- **Fora de alcance nesta rodada:**
  - decisões de 2026 que a API não devolve;
  - o 1º grau (moldura ainda em coleta);
  - o STJ e o STF fora dos acervos locais.
- **Zero resultado** numa consulta não prova inexistência.

## 2. O que foi encontrado, lido e verificado
- **Piloto E3:** 24 registros (20 do TJBA, 1 do STJ, 3 precedentes qualificados), sorteados com semente fixa em 14 estratos por indício.
- **Leitura:** 4 leitores Opus, às cegas, sem estrato nem indício.
- **Verificação:** 24/24 aprovados no `validar.py` (excertos literais localizados por código no texto com hash; schema v1.1).
- **Unidades distintas:**
  - 24 decisões e 40 questões;
  - 5 registros excluídos por EXC-07 (IPTU só como dado de fato);
  - só 4 dos 24 têm inteiro teor no acervo (3 deles excluídos; o outro é DEC-TJBA-97bcca2ed476); os demais trazem só ementa e dispositivo, ou menos.
- **Duplicação entre fontes:** testada num caso. O mesmo acórdão está em acervo local e no Cognitio; vale como procedência alternativa.
- **Revisão:**
  - antialucinação do dossiê TES-001: nada grave, 2 achados médios corrigidos;
  - Codex: 1 achado grave (deduplicação) e 7 médios ou leves, todos corrigidos com recibo em `auditoria/correcoes.jsonl`;
  - **nenhuma revisão humana registrada.**

## 3. Tese com suporte de piloto
**TES-001 — imunidade de IPTU e ônus da prova da destinação** (`analises/teses/TES-001-imunidade-onus-da-destinacao.md`).
- **Templo (alínea *b*):** um acórdão do TJBA põe no Município o ônus de provar a tredestinação.
- **Alínea *c*:** uma decisão põe o ônus no contribuinte (art. 14 do CTN) e barra a exceção. Outra, em embargos, reconhece a imunidade sem dizer de quem era o ônus.
- **Walton:** A2 (SV 52 como regra) dá PLAUSIBLE, com exceções abertas. A1, A3 e A4 dão WEAK, cada uma com a pergunta crítica que falta. A generalização de tendência (J1) foi barrada.
- **Estado:** hipótese em teste, não repertório consolidado.

**Candidata a TES-002:** imunidade recíproca de estatais baianas (CODEBA, EMBASA), com distinção dos Temas 385 e 437 e o Tema 1398 só afetado.

## 4. Achados de método que mudam a expansão
1. **Precisão da T1:** a T1 determinística não basta para dizer se a decisão trata de IPTU (4 de 20 A1 eram menção). A E4 precisa da T2 (Sonnet) antes de classificar.
2. **Completude do acervo:** o acervo do TJBA tem, na maior parte, ementa e dispositivo. Teses centrais precisam do inteiro teor pela PDPJ ou pelo portal.
3. **Metadados do portal:** o órgão "2ª Vice-Presidência" e o tipo do ato divergem do texto em 4 de 20 casos. O texto prevalece.
4. **Deduplicação:** só funde o mesmo ato, com classe e texto iguais; corrigido no protocolo v2.

## 5. Jurimetria nesta rodada
Só **funil de cobertura** (`jurimetria/funil.json`) e **composição do piloto** (`jurimetria/piloto-composicao.json`, com as listas de IDs). O piloto é amostra intencional: **nenhuma taxa de êxito é calculável**, por desenho.

## 6. Próximo lote executável (E4, lote 1)
1. **T2 (Sonnet):** pertinência e eixo dos 9.981 + 232 candidatos do TJBA, em lotes de ~300 ementas, com recibo por registro.
2. **Fila IPTU-04 (imunidade):** classificação Opus por questão dos elegíveis; inteiro teor das centrais pela PDPJ; trajetória dos 3 casos do TES-001.
3. **Moldura DataJud (quando terminar):** sorteio estratificado do 1º grau, depois DJEN por número de processo.
4. **Portal STF (Chrome):** situação da SV 52, rótulo do Tema 693 e o precedente sobre ônus citado pelo TJBA (pista: RE 611.510).
