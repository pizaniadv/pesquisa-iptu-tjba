---
tipo: protocolo-anexo
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: vigente
---

# Harmonização T3, v1 (anexo ao protocolo v2 e ao dicionário v1.1)

Os leitores T3 leram às cegas e, em alguns padrões que o dicionário não fixava, aplicaram critérios diferentes entre si. Esta regra uniformiza esses padrões **por código** (`scripts/harmonizar_t3.py`). A regra foi fixada depois da leitura e antes de qualquer contagem. Cada mudança guarda o valor anterior no próprio registro, no campo `harmonizacao`, e vai para `auditoria/harmonizacao-t3.jsonl`.

| Regra | Padrão | Antes (variável entre leitores) | Depois |
|---|---|---|---|
| H1 | Questão com `materia_examinada = admissibilidade`: recurso do Município ou do contribuinte inadmitido, negativa de seguimento (art. 1.030 do CPC), Súmulas 7, 83 e 279, conformidade com tema | `favoravel_integral` (16), `favoravel_parcial` (2), `desfavoravel` (8), `indeterminavel` (2), `sem_exame` (37) | `resultado = sem_exame` e `natureza_beneficio = null`. Inadmissão não é adesão (CLAUDE.md, regra 5). O resultado que importa está no acórdão recorrido, que é etapa de trajetória. |
| H2 | Texto que é só relatório, sem decisão (pedido de pauta, art. 931 do CPC; "Passo a decidir" sem continuação) | `classificado` (o brief mandava) ou `excluido` (EXC-03) | `estado = pendente` (protocolo §5). Sai das contagens e entra na fila de inteiro teor (PDPJ). |
| H3 | Exclusões criadas pelos leitores e candidatas apontadas por eles | Códigos fora do brief (EXC-05, EXC-01, EXC-03) | Revisadas pelo orquestrador, uma a uma (lista no script). A controvérsia só sobre TRSD é EXC-05. |

## Regras de contagem (sem mudar registro)
- **Unidade = processo.** Os atos do mesmo processo (número sem o sufixo `/5000x`) contam uma vez, pelo ato principal. A ordem de preferência é:
  1. mérito;
  2. processual;
  3. cautelar;
  4. admissibilidade.
- Dentro do mesmo grau de preferência, o acórdão vem antes dos embargos de declaração.
- **Tutela:** conta-se pela `provisoriedade` (provisória × definitiva), e não pelo eixo IPTU-04 ou IPTU-13 que o leitor escolheu.
- **Ônus da destinação:** é a determinação do leitor, extraída da linha final de cada um (`estado/t3/respostas-leitores.jsonl`, `scripts/coletar_respostas_t3.py`).
- **Alínea:** é a da leitura T3 (subtema e pergunta). A alínea por regex da fatia (`fatiar_t3.py`) era só indício de ordem de leitura. O que for alínea *a* (imunidade recíproca) vai para a TES-002.
