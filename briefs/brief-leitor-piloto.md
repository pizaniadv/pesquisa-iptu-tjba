---
tipo: brief-executor
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: superado
---

# Brief — leitor do piloto (SUPERADO: usar estado/brief-leitor-t3-v1.1.md) (classificação por questão)

**Papel:** ler cada decisão que lhe foi atribuída e produzir UM registro canônico JSON por decisão. Você é leitor jurídico (Direito Tributário, IPTU). Não pesquise nada fora do texto: nada de Cognitio, portal, internet, outros arquivos do acervo. A trajetória (o que veio depois) é outra etapa; aqui você só registra o que o próprio texto diz.

## Leia antes (nesta ordem)
1. `metodologia\dicionario-de-dados.md` — as definições de cada valor. Obrigatório.
2. `schemas\decisao.schema.json` — a forma do registro.
3. `config\taxonomia.yaml` — eixos IPTU-01..17, conceitos e motivos de exclusão EXC-01..07.
4. `metodologia\protocolo-v1.md` §§ 5 a 7.

## Para cada decisão `<id>`
- Entrada: `evidencias\extracoes\<id>.txt` (texto) e `evidencias\extracoes\<id>.meta.json` (metadados do tribunal: número, órgão, relator, classe, datas, ponteiro, sha256_texto).
- Leia o texto INTEIRO (use offset/limit se for longo; registre em `qualidade.leitura` o que leu de fato).
- Saída: `dados\decisoes\<id>.json`, válido no schema, com:
  - `id` = o `<id>` recebido; `versao_schema` = "v1"; `estado` = "classificado" (nunca "verificado"); `via_descoberta` = ["neutra_sistematica"].
  - `fonte`: `canal` (F_TJBA, F_STJ ou F_PANGEA conforme o ponteiro), `ponteiro` e `sha256` (= `sha256_linha` ou `_sha256` do meta; se não houver, o `sha256_texto`), `sha256_texto` do meta.
  - `datas.coleta` = "2026-11-05". Datas do meta em ISO (só a data). Datas ausentes = objeto nulo motivado.
  - `questoes`: uma por pergunta jurídica decidida (honorários e taxas são questões próprias). IDs `<id>#Q1`, `<id>#Q2`… Para cada uma: tributo, eixo, pergunta, materia_examinada, resultado (do ponto de vista do CONTRIBUINTE), objeto_do_resultado, natureza_beneficio, provisoriedade, efeito_sobre_ato_anterior, fundamento_determinante (1 a 3 excertos), argumentos_rejeitados (se houver), normas, precedentes_usados (com `uso`).
  - `dispositivo`: o(s) trecho(s) do dispositivo/certidão de julgamento.
  - `contexto`: município, exercícios, fatos relevantes (excertos), provas mencionadas. `partes`: polo do contribuinte, ente, recorrente.
  - `qualidade`: completude, leitura, `verificacao` = "nao_verificada", `revisor` = [{"quem": "leitor-opus-piloto", "tipo": "automatizada", "data": "2026-11-05"}], pendências.
- **Excertos:** só cópia LITERAL do `.txt` (copie e cole; mesma grafia, inclusive erros e caixa; nada de reticências no meio). Não escreva `localizador` nem `conferido_no_original` — o validador preenche.
- **Se a decisão não for sobre IPTU como questão tributária** (ex.: IPTU só como encargo de locação, comprovante, partilha), registre `estado` = "excluido", `exclusao` = {"motivo": "EXC-0x", "nota": "..."} e uma questão com o tributo/eixo mais próximo e `resultado` = "sem_exame", explicando na pergunta. Não force classificação.
- **Precedente qualificado (súmula, tema):** `especie_ato` = "sumula" ou "tese_qualificada"; a questão é a questão do tema; `resultado` do ponto de vista do contribuinte se a tese foi fixada; se o tema está só afetado/pendente, `resultado` = "sem_exame" e diga isso. Grau = STF/STJ.

## Conferência obrigatória
Depois de gravar, rode: `python -I scripts\validar.py dados\decisoes\<id>.json`
- REPROVADO por excerto não achado → corrija copiando o trecho exato do `.txt` e rode de novo. REPROVADO por schema → corrija o campo. Repita até OK.
- Não altere nenhum outro arquivo do projeto, nem os scripts, nem o schema.

## Resposta final (curta)
Uma linha por decisão: `<id> | OK/REPROVADO | nº de questões | resultado de cada questão (Q1=..., Q2=...) | dúvida que o titular precisa ver (se houver)`. Nada mais.
