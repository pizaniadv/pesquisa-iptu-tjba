---
tipo: relatorio-de-pesquisa
data: 2026-11-06
produzido-por: claude-code
versao-core: 1.0
status: draft
---

# Relatório: revisão das fichas da E4-3 e TES-001 v4 (06/11/2026, manhã)

**Ordem do titular (06/11/2026, 10:20):** "faça do jeito que vc recomendar". Ficaram fora, por ordem dele: o volume de consultas no PDPJ e a correção da ferramenta pdpj-api/`consultar.py` (sessão paralela).

## Resultado
- **Antialucinação** das 32 fichas e da TES-001 v4, em 7 lotes por família, mais um lote para as trocas pós-Codex (`auditoria/antialucinacao-E43-*.md`):
  - nenhum achado grave;
  - 249 propostas: 25 médias e 224 leves;
  - todas aplicadas (`auditoria/aplicacao-antialucinacao.jsonl`, 250 recibos);
  - a maior parte dos médios deixa a tese **mais forte** do que a ficha dizia.
- **Codex**, só leitura e com a árvore parada:
  - rodada 1: 2 graves, 7 médios e 1 leve (`estado/codex-revisao-e43.md`);
  - rodada 2: todos resolvidos e nenhum grave novo (`estado/codex-revisao-e43-r2.md`).
- **Revisão humana:** pendente.
- **Excertos:** 602/602 literais e, agora, **atribuídos ao processo citado**. O controle negativo, com número trocado, rejeitou 50 de 50.

## O que mudou nos dados
1. **8 ajustes da conferência de inteiro teor** aplicados aos registros, mais uma data corrigida pela antialucinação (`auditoria/ajustes-conferencia-it.jsonl`).
2. **Releitura dos 11 pendentes H2** com inteiro teor (PDPJ e DJEN), em duas rodadas (`auditoria/releitura-h2.jsonl`):
   - 8 reclassificados;
   - 3 duplicatas (EXC-04).
   Algumas peças decisórias foram baixadas pontualmente pelo PDPJ.
3. **Preliminar de dialeticidade rejeitada** deixou de ser `sem_exame`:
   - fd5f Q1: favorável, processual;
   - eec4 Q2: desfavorável.
   Ver `auditoria/correcoes.jsonl`.
4. **TES-001 v4:**
   - 147 processos, 110 de alínea *b*/*c*;
   - ônus no Município: 52 favoráveis em 57;
   - entra 0503944-29.2016 (templo);
   - 8003270-07.2025 passa a ônus misto;
   - as 5 derrotas da linha minoritária continuam.
5. **Rótulo "2ª Vice-Presidência" do banco F::** cerca de 540 dos 1.318 julgados assim rotulados são acórdãos de Câmara no texto. Foi corrigido em 11 fichas (`auditoria/correcoes-pos-codex-e43.jsonl`), e o núcleo de mérito subiu em algumas (TES-07: de 20 para 24). Vira limite permanente: órgão pelo texto.
6. **`n_acervo` uniformizado** (total do recorte × `n_acervo_fav`). Frases de taxa ou tendência sem denominador foram reescritas em 23 fichas.

## Para o MIJ antes de uso em peça (lista nos relatórios de cada lote)
- **TES-25:** o AgInt no REsp 1.950.739 admite o promitente comprador irretratável como contribuinte mesmo sem posse; vai contra a tese.
- **TES-001:** o AgInt no REsp 1.968.035/RJ põe no Fisco também o ônus do art. 14 do CTN, o que tensiona a "A4 restrita".
- **TES-39:**
  - Tema 1.140/STF (pilar das estatais);
  - Tema 1.398 (alcance);
  - a recomendação de pedir sobrestamento, porque a 2ª VP mandou os agravos da COELBA ao STF e ao STJ em 05/2026.
- **TES-08:** Tema 387/STJ diante da reclassificação retroativa.

## Pendências
- **Revisão humana:** começar por `analises/fichas/00-INDICE.md`.
- **Atos sem registro achados na releitura:**
  - embargos sobre embargos acolhidos em 8000200-86.2020;
  - embargos .4.EDCiv rejeitados em 0303373-71.2014;
  - embargos de 12/2025 em 0300365-78.2019.
  São pistas de trajetória, de trilha dirigida, e não entram no denominador.
- **Irmãos do mesmo julgamento** (acórdão e voto como registros separados: e3b4/eec4; 9e9d/a757): a contagem por processo já neutraliza, mas cabe EXC-04 entre si.
- **DataJud (moldura do 1º grau):** parada em 37.344 de 43.219 (`dados/moldura-datajud-a-parcial-2026-11-06.jsonl`).
