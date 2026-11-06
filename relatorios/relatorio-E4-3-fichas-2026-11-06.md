---
tipo: relatorio-de-pesquisa
data: 2026-11-06
produzido-por: claude-code
versao-core: 1.0
status: draft
---

# Relatório E4-3: fichas das 33 teses escolhidas (IPTU, TJBA)

**Ordem do titular (06/11/2026, 00:25):** tirar as teses 1, 2, 3, 5, 6 e 35. Trabalhar com DJEN, acervo, API de jurisprudência do TJBA, STJ, STF e portais.

**Feito:**
- **Fichas:** 32 fichas (`analises/fichas/`) e a TES-001 v3 (`analises/teses/`). Índice em `analises/fichas/00-INDICE.md`.
- **Leitores:** 8 leitores Opus, um por família (F1a, F1b, F2, F3, F4, F5, F6, F7), cerca de 2,8 milhões de tokens.
- **Excertos:**
  - fichas: 602 de 602 conferidos por código (`auditoria/conferencia-fichas-e43.jsonl`);
  - TES-001 v3: 26 de 26.
- **Walton/Élenchos:** 23 PLAUSIBLE e 9 WEAK_UNANSWERED_CQ. Cada WEAK nomeia a pergunta crítica que o material não responde.

## Fontes por tese
- **Acervo:** base de ementas dos 10.213 candidatos (`derivados/ementas-candidatos.jsonl`), com recorte por palavra em `estado/E4-3/recorte-acervo.json`. É de onde saem as contrárias.
- **API do TJBA:** busca com `IPTU AND "chave"` (`evidencias/dirigida/tjba-api-e43-2026-11-06.json`). Não é neutra e subconta.
- **DJEN por termo e PANGEA:** `evidencias/dirigida/F*-2026-11-06.json`.
- **Cognitio:** usado pelos leitores para o STJ e o STF (`buscar_juris_struct` + `obter_documento`). O que não foi conferido está marcado `[A CONFERIR]` em cada ficha.
- **Portal do STF:** ARE 800.395 AgR e ARE 1.037.290 AgR (`evidencias/dirigida/stf-portal-2026-11-05.json`).
- **Deduplicação:** por processo (número sem sufixo) e por texto, dentro de cada fonte e entre fontes, como o titular pediu.

## Inteiro teor
- **PJe 2º grau** (titular logado, captcha resolvido por ele): 8 processos da linha minoritária da TES-001 (`evidencias/pje2g/`).
- **PDPJ pelo servidor de coleta,** depois que o Codex do CNJ voltou (~00:36): os 22 alvos (`evidencias/pdpj/`). Foram removidos 28 arquivos que eram mensagem de erro gravada como texto, e houve uma retentativa.
- **DJEN por número:** 13 dos 19 processos tinham publicação (`evidencias/djen/`).

## Destaques (detalhe nas fichas)
- **TES-001 v3:** no templo, o ônus é do Município (com respaldo do STF). Na entidade (alínea c), a destinação se presume, mas os requisitos do art. 14 do CTN se provam por documento; as 5 derrotas foram em exceção de pré-executividade sem prova pré-constituída.
- **TES-39 (imunidade recíproca):**
  - EMBASA e CODEBA: imunes;
  - COELBA: divergência entre câmaras e no tempo, com sobrestamento pelo Tema 1.297. A aderência desse tema foi questionada, porque ele trata de transporte ferroviário.
- **Teses PLAUSIBLE com respaldo qualificado:**
  - ilegitimidade passiva (Súmula 392 do STJ);
  - sujeição passiva (Temas 122 e 1.158 do STJ);
  - progressividade (Temas 155 e 226 do STF);
  - majoração por decreto (Súmula 160 do STJ);
  - zona rural (Tema 174 do STJ);
  - revisão de ofício (Tema 387 do STJ);
  - sanção política (Súmulas 70, 323 e 547 do STF).
- **Teses frágeis no TJBA:**
  - competência (sem decisão favorável no material);
  - decisão surpresa (serve sobretudo ao Município);
  - trava do aumento de Salvador (1 a 1);
  - planta genérica (10 a 10).

## Pendências
1. **Antialucinação, Codex e revisão humana:** não feitas em nenhuma ficha nem na TES-001 v3. Nada sai do laboratório antes delas.
2. **Os 11 registros pendentes da harmonização:** já têm inteiro teor no PDPJ; falta relê-los pelo Opus e reclassificar.
3. **Itens `[A CONFERIR]`:** listados em cada ficha. Na TES-001 e na TES-39, constam da própria v3.
4. **1º grau:** a moldura do DataJud ficou em coleta no servidor de coleta.
5. **Fichamento no banco de teses do Vault:** feito em versão resumida, com as âncoras marcadas.
