---
tipo: dicionario-de-dados
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: vigente
versao: v1.1
schema: schemas/decisao.schema.json (v1.1)
historico: "v1.1 (05/11/2026): achados do Codex na revisão do piloto — prescrição sem contradição; nao_examinada; convenção de leitura; campos independentes obrigatórios"
---

# Dicionário de dados v1 — registro de decisão

Uma linha por valor. Quem classifica usa só estas definições. Na dúvida entre dois valores, escolha o mais fraco e diga por quê em `qualidade.pendencias`.

## Regras que valem para todos os campos
- **Ausência não é zero.** Campo sem dado = `{"valor": null, "motivo": ...}` com `nao_informado` (o documento não traz), `nao_localizado` (procurei e não achei), `nao_aplicavel`, `ilegivel`, `nao_verificado` (não procurei).
- **Excerto é cópia literal** do arquivo `evidencias/extracoes/<id>.txt` (mesma grafia, sem corrigir, sem reticências no meio). O localizador e o `conferido_no_original` são preenchidos pelo `scripts/validar.py`; excerto que não for achado literalmente reprova o registro.
- **Voz**: quem diz o trecho. Alegação de parte reproduzida no relatório é `parte`, não fundamento.

## questoes[] — uma por pergunta jurídica
Cada pedido ou capítulo decidido vira uma questão. Honorários são questão própria (eixo IPTU-15). Taxa de lixo, COSIP, ITBI no mesmo processo são questões próprias com `tributo` correspondente (eixo IPTU-17).

| Campo | Valor | Definição |
|---|---|---|
| `tributo` | IPTU / TAXA_LIXO / COSIP / ITBI / ISS / OUTRO | o tributo da questão, não do processo |
| `materia_examinada` | nao_examinada | a questão não foi examinada por nenhum ângulo (registro excluído; tema só afetado) |
| | merito | o órgão resolveu a questão tributária ou de direito material |
| | admissibilidade | não conheceu, negou seguimento por óbice formal, intempestividade, preparo, dialeticidade |
| | processual | questão de processo (nulidade de citação, cabimento de exceção, legitimidade como condição, extinção sem mérito) |
| | cautelar | tutela provisória, liminar, efeito suspensivo |
| | sucumbencial | só honorários/custas |
| `resultado` | favoravel_integral | o contribuinte obteve tudo o que pedia naquela questão |
| | favoravel_parcial | obteve parte (dizer qual parte em `objeto_do_resultado`) |
| | desfavoravel | perdeu a questão |
| | sem_exame | a questão foi posta mas o órgão não a examinou (prejudicada, não conhecida, remetida) |
| | indeterminavel | o texto disponível não permite saber |
| `natureza_beneficio` | material | inexistência/redução do tributo, imunidade, isenção, nulidade do lançamento por vício material |
| | processual | extinção da execução sem declarar extinto o crédito, nulidade da CDA por vício formal, ilegitimidade; prescrição só quando o texto não declara extinto o crédito (ver nota) |
| | provisorio | tutela, liminar, suspensão de exigibilidade |
| | probatorio | direito a prova, perícia, inversão do ônus |
| | sucumbencial | honorários ou custas a favor do contribuinte |
| | null | quando o resultado não é favorável |
| `provisoriedade` | definitiva_na_instancia / provisoria / nao_aplicavel | tutela e liminar são `provisoria` |
| `efeito_sobre_ato_anterior` | mantem / reforma / reforma_parcial / anula / integra / nao_aplicavel / indeterminado | o que o ato fez com o ato recorrido (sentença ou decisão) |

**Nota — prescrição:** é extinção do crédito tributário (CTN art. 156, V). Registre `natureza_beneficio = processual` quando a decisão só extingue a execução, e `material` quando declara extinto o crédito. Copie o trecho que diz qual das duas.

**Negativas do protocolo (§ 7):** "provido/desprovido" sozinho não classifica — cruze com quem recorreu. Recurso do Município desprovido em que a sentença era favorável = `favoravel_*` + `mantem`. Recurso do contribuinte não conhecido = `sem_exame` + `materia_examinada = admissibilidade`. Extinção processual não é inexistência da obrigação. Vitória só sobre taxa não é vitória sobre IPTU. Liberação de penhora ou honorários não é cancelamento do IPTU.

## Outros campos
| Campo | Definição |
|---|---|
| `identificacao.grau` | 1G sentença/decisão de vara; 2G câmara/seção/relator do TJ; TR turma recursal; STJ; STF; ADM conselho administrativo |
| `identificacao.especie_ato` | acordao · decisao_monocratica · sentenca · decisao_interlocutoria · tutela · integrativa (embargos de declaração) · sumula · tese_qualificada · decisao_administrativa |
| `partes.contribuinte_polo` | posição do contribuinte NESTE ato |
| `contexto.exercicios` | exercícios fiscais do IPTU discutido, como texto ("2012", "2015-2018"); vazio se não informado, com pendência |
| `precedentes_usados.uso` | aplicacao_determinante (a decisão decide por ele) · distincao · referencia_incidental · transcricao_de_alegacao · discordancia |
| `qualidade.completude` | inteiro_teor (relatório+voto+dispositivo) · ementa_e_dispositivo · so_ementa · trecho_publicado · metadados |
| `qualidade.leitura` | nao_lida · lida_parcialmente (não leu todo o texto disponível) · disponivel_lido_integralmente (leu todo o texto disponível, que NÃO é o inteiro teor) · inteiro_teor_lido (só quando `completude` = inteiro_teor) |
| `estado` | candidato → pendente/elegivel → classificado (leitor) → verificado (validar.py + antialucinação). O leitor nunca marca `verificado`. |
| `via_descoberta` | neutra_sistematica para tudo que veio da varredura Q-NEUTRA-01 |
