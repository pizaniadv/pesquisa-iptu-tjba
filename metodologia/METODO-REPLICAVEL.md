---
tipo: guia-de-metodo
data: 2026-11-06
produzido-por: claude-code
versao-core: 1.0
status: vigente
---

# Método replicável: repertório jurisprudencial por tributo

Este guia nasceu do IPTU (05 e 06/11/2026). Por ordem do titular (06/11/2026, 00:51), o projeto vai se estender a todos os tributos, municipais, estaduais e federais, um por sessão. Para abrir um tributo novo, copie a estrutura para `labs/pesquisa-<tributo>` e troque **só** o que está marcado como específico.

## 1. Etapas (o que se reaproveita)

| Etapa | O que faz | Script / regra | Custo de referência (IPTU) |
|---|---|---|---|
| E1. Varredura neutra | Lê os bancos locais por expressão regular (rg, prioridade BelowNormal) e gera recibos | `scripts/varrer_f.py` | minutos (Windows, leve) |
| E1. Triagem automática (T1) | Agrupa julgados repetidos (regra v2: número, classe e texto) e marca indícios (dispositivo, eixos, Município recorrente) | `scripts/triar.py` | segundos |
| E1. Delta recente | Busca na API do tribunal o que é posterior ao banco local; cobertura parcial declarada | `scripts/delta_tjba_api.py` (servidor de coleta) | horas no servidor de coleta |
| E1. Moldura do 1º grau | DataJud por assunto ou classe → sorteio de números → DJEN | `scripts/moldura_datajud.py` (servidor de coleta) | horas no servidor de coleta |
| E3. Piloto | Amostra estratificada, leitura pelo Opus às cegas, validação por código | `selecionar_piloto.py`, `validar.py`, `schemas/decisao.schema.json` | cerca de 1 M Opus |
| **E4-2. Catálogo de teses** (primeiro) | Sonnet lê as ementas com indício favorável; tese, tema, via e trecho literal | `extrair_ementas_fav.py`, `estado/brief-catalogo-teses-v1.md`, `consolidar_catalogo.py` | cerca de 6 M Sonnet para 2.108 ementas |
| Lista numerada | O titular corta pelo número | `analises/lista-numerada-de-teses-v1.md` | — |
| E4-3. Fichas por família | Base de ementas do acervo inteiro (contrárias), DJEN e API por termo, PANGEA; um Opus por família | `base_ementas.py`, `dirigida_e43.py`, `tjba_assunto_e43.py`, `pacote_e43.py`, `estado/brief-ficha-tese-v1.md`, `conferir_fichas.py` | cerca de 2,5 M Opus para 31 fichas |
| E4-1. Dossiê profundo (só nas escolhidas) | T2 Sonnet calibrada → T3 Opus → harmonização → tabela por processo → inteiro teor | `pacote_t2.py`, `consolidar_t2.py`, `fatiar_t3.py`, `harmonizar_t3.py`, `tabela_tes001.py` | cerca de 6 M Opus para 233 decisões |
| Inteiro teor | DJEN por número; PDPJ pelo servidor de coleta; PJe 2º grau pelo Chrome com o titular logado | `djen_por_numero.py`, `pdpj_inteiro_teor.py`, `vigia_codex.py`, `receptor_pje.py` | — |

**Regras que valem sempre:**
1. Denominador só da trilha neutra.
2. Contar **processo**, não decisão.
3. Todo excerto conferido por código.
4. Regra congelada antes da execução.
5. Calibração antes da produção.
6. Harmonização por regra escrita, com o valor anterior guardado.
7. Revisor (Codex) só com a árvore parada.
8. Antialucinação antes de qualquer texto sair.

## 2. O que é específico do IPTU (trocar)

| Peça | Arquivo | O que trocar |
|---|---|---|
| Filtro de termos da varredura | `scripts/varrer_f.py` (`PRE`) | o nome do tributo e suas variantes (ISS, ICMS, ITBI, IRPJ etc.) |
| Taxonomia e ontologia | `config/taxonomia.yaml` | eixos do tributo, conceitos com âncoras do Atlas, motivos de exclusão |
| Escopo e fontes | `config/pesquisa.yaml`, `dados/fontes.json` | tribunais e bancos: CARF e TRFs (federais); CONSEF e TJ (estaduais); CMT e TJ (municipais) |
| Termos das teses | `estado/E4-3/teses.json` | regex, chave da API e frases do DJEN de cada tese |
| Temas do catálogo | `estado/brief-catalogo-teses-v1.md` | a lista fechada de temas |
| Assunto do DataJud | `scripts/moldura_datajud.py` | o código de assunto do CNJ |

## 3. Armadilhas já conhecidas
- **Banco local do TJBA:** vai só até 12/2025 e traz quase só ementa e dispositivo.
- **API do TJBA:** subconta; exige `Origin` e `Referer`, datas e a sintaxe `TRIBUTO AND "frase"`.
- **Portal do TJBA:** repete julgados; deduplicar antes de contar.
- **DJEN:**
  - no TJBA traz a decisão monocrática inteira e, do acórdão, só a ementa;
  - cobertura a partir de cerca de 2024;
  - responde "muito ocupado" e exige retentar.
- **Codex do CNJ:** quando cai, o PDPJ inteiro fica sem texto, e a ferramenta da casa grava o erro como se fosse texto: filtrar.
- **Indício por palavra:** pega outros tributos (na imunidade, 20 de 23 exclusões eram ITBI ou ISS).
- **Recurso inadmitido:** não é adesão; registrar como `sem_exame`.
