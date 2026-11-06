---
tipo: readme-projeto
data: 2026-11-06
produzido-por: claude-code
versao-core: 1.0
status: em-revisao
---

# PESQUISA-IPTU — repertório de teses de IPTU no TJBA (2020-2026)

Pesquisa jurisprudencial sobre o IPTU no Tribunal de Justiça da Bahia (2º grau e Turmas Recursais), com STJ e STF como camada qualificada. Ela traz um catálogo de teses, fichas por tese, um dossiê aprofundado (TES-001, ônus da prova na imunidade de templo e de entidade) e o método, que pode ser repetido para outros tributos.

> **Estado: em revisão.** As fichas passaram por conferência literal dos excertos por código (602 de 602, atribuídos ao processo citado), por antialucinação contra a fonte primária e por duas rodadas de revisão independente (`revisao/`). **A leitura humana do titular está pendente.** Fichas são camada de descoberta, não parecer: o uso em peça exige reabrir a fonte primária de cada âncora.

## O que há aqui
| Pasta | Conteúdo |
|---|---|
| `metodologia/` | Protocolo, dicionário de dados, regra de harmonização e **método replicável** para outros tributos (`METODO-REPLICAVEL.md`) |
| `scripts/` | Pipeline: varredura neutra, triagem, pacotes, conferência, harmonização, tabelas |
| `schemas/`, `config/` | Esquema do registro de decisão; escopo, fontes e taxonomia |
| `analises/` | Catálogo de 37 teses, lista numerada, 32 fichas (`fichas/00-INDICE.md`) e dossiê TES-001 v4 (`teses/`) |
| `relatorios/` | Relatórios de cada etapa |
| `auditoria/` | Relatórios de antialucinação por lote |
| `revisao/` | Revisões independentes (rodadas 1 e 2) |
| `briefs/` | Instruções dadas a cada etapa de leitura e revisão |
| `jurimetria/` | Funil e composição do piloto |

## O que ficou fora (de propósito)
- **Textos integrais** obtidos pelo PDPJ, PJe e DJEN (`evidencias/`), **registros brutos** (`dados/`), **base derivada** (`derivados/`) e **estado de execução** (`estado/`). Esse material traz dados pessoais das partes e vem de acesso autenticado.
- **Configuração de máquinas, caminhos locais e credenciais.** Os scripts leem do ambiente:
  - `PDPJ_API_CHAVE_ARQ` e `PDPJ_API_BASE`: servidor REST de leitura da PDPJ;
  - `DATAJUD_API_KEY`: chave pública da API do DataJud;
  - `PANGEA_DB` e `ACERVO_STJ`: acervo local.
  `<ACERVO>` nos textos indica a pasta do acervo local de jurisprudência.
- CNPJ e CPF de partes aparecem como `[CNPJ omitido]` / `[CPF omitido]`.

Sem esses insumos, os scripts não rodam do zero; servem para mostrar e reproduzir o método.

## Regras do método (resumo)
1. Denominador só da trilha neutra; achado dirigido vai para o repertório, nunca para a taxa.
2. Conta-se **processo**, não decisão; julgados repetidos são deduplicados.
3. Todo excerto é conferido por código como literal.
4. Resultado por questão, do ponto de vista do contribuinte; admissibilidade não é adesão; tutela não é mérito.
5. Walton em todo dossiê (esquema, perguntas críticas, contra-analogia).
6. O órgão julgador vale pelo texto da decisão, nunca pelo metadado do banco.
