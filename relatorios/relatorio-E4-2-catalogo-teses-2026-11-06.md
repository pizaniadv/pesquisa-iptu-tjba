---
tipo: relatorio-de-pesquisa
data: 2026-11-06
produzido-por: claude-code
versao-core: 1.0
status: draft
---

# Relatório E4-2: catálogo de teses de IPTU no TJBA (nível de ementa)

**O que é:** um mapa das teses que decidiram casos de IPTU no TJBA entre 2020 e 2026 (até 12/2025 pelo banco acervo local, e o que veio de 2026 pela API do TJBA).

**Universo:**
- os candidatos da trilha neutra com **indício automático de vitória do contribuinte**, que é Município recorrente com recurso desprovido, ou contribuinte recorrente com recurso provido;
- ficam fora os candidatos de imunidade (IPTU-04), já tratados na E4-1.

São 2.108 ementas.

**Executor:** Sonnet, pela regra `estado/brief-catalogo-teses-v1.md`. Excertos conferidos por código: 2.108 de 2.108 literais. Leitura só da ementa, com teto de 3.000 caracteres. Não houve leitura pelo Opus nem revisão humana.

**O que não é:** taxa de êxito. O universo foi escolhido por indício favorável e serve para **descobrir teses**, não para medir tendência. A unidade é a decisão, sem a fusão por processo que se fez na E4-1. Fonte: `analises/catalogo-teses-v1.csv` (linha a linha, com número, órgão, data e excerto).

## 1. Teses por tema (decisões pertinentes, 1.863 de 2.108)
| Tema | Favorável | Parcial | Desfavorável | Sem exame | Incerto |
|---|---|---|---|---|---|
| Prescrição originária (5 anos da constituição; despacho/citação) | 364 | 14 | 151 | 14 | 12 |
| Prescrição intercorrente (art. 40 da LEF) | 183 | 2 | 31 | 8 | 24 |
| Execução de valor irrisório (Tema 1.184/STF, Res. CNJ 547/2024) | 163 | 5 | 19 | 23 | 16 |
| Ilegitimidade passiva na execução | 128 | 0 | 1 | 5 | 3 |
| Abandono ou inércia do exequente (art. 485, III, do CPC)* | ~121 | | | | |
| Honorários e sucumbência | 55 | 3 | 0 | 0 | 6 |
| Sujeição passiva | 42 | 1 | 0 | 4 | 2 |
| Alíquota e seletividade | 30 | 6 | 0 | 3 | 2 |
| Base de cálculo e valor venal | 29 | 2 | 4 | 0 | 2 |
| Falta de CPF, endereço ou qualificação do executado* | ~26 | | | | |
| Nulidade da CDA | 24 | 0 | 0 | 0 | 0 |
| Cobrança em duplicidade | 20 | 0 | 0 | 0 | 0 |
| Execução contra falecido ou espólio* | ~18 | | | | |
| Majoração por decreto | 16 | 1 | 1 | 1 | 1 |
| Isenção | 15 | 0 | 0 | 0 | 0 |
| Dano moral, protesto ou cobrança indevida* | ~15 | | | | |
| Parcelamento ou suspensão da exigibilidade* | ~15 | | | | |
| Extinção por pagamento ou parcelamento | 14 | 1 | 13 | 1 | 0 |
| Zona rural ou urbana | 13 | 1 | 0 | 2 | 3 |
| Progressividade | 13 | 4 | 0 | 1 | 0 |
| Planta genérica de valores | 12 | 0 | 4 | 9 | 7 |
| Área tributável (metragem física) | 11 | 1 | 0 | 0 | 0 |
| Desapropriação ou imissão na posse | 10 | 0 | 0 | 0 | 0 |
| Promitente comprador sem posse | 4 | 0 | 0 | 0 | 1 |
| Compensação, notificação do lançamento, repetição | 2 a 3 cada | | | | |

\* Subgrupos tirados do tema "outro" (228 favoráveis) por palavra-chave da tese. A contagem é aproximada.

## 2. Teses menos óbvias encontradas (no tema "outro")
- **Bitributação entre municípios:** Salvador × Lauro de Freitas, em área limítrofe. Há cobrança do município incompetente, CDA nula e consignação em pagamento homologada (Lei Estadual 2.713/1969).
- **Área de proteção ambiental não edificável:** restrição absoluta, sem incidência de IPTU.
- **Revisão de ofício do lançamento vedada:** erro de direito, porque as características construtivas já eram conhecidas do Fisco.
- **Sanção política:** o alvará de construção não pode exigir quitação do IPTU (Súmulas 70, 323 e 547 do STF).
- **Lançamento anulado por erro de cálculo do limite máximo do tributo:** legalidade estrita.
- **Garantia e penhora:**
  - menor onerosidade: aceita o próprio imóvel tributado no lugar de Sisbajud ou Bacenjud;
  - impenhorabilidade da poupança até 40 salários mínimos;
  - impenhorabilidade da conta de idoso (mínimo existencial).
- **Processo:** decisão surpresa (arts. 9º e 10 do CPC); gratuidade de justiça ao executado aposentado.

## 3. Achados de método
- **A extinção da execução domina.** As teses "processuais" (prescrição, valor irrisório, ilegitimidade, abandono, falta de CPF) somam a maior parte das vitórias. As teses de mérito do tributo (base de cálculo, progressividade, majoração, alíquota, zona rural, área, isenção) aparecem em dezenas, não em centenas.
- **Prescrição originária tem muitas derrotas (151).** Nem todo caso com indício favorável é vitória. Isso confirma que o indício automático é só indício.
- **Ementas cortadas no teto de 3.000 caracteres:**
  - **2ª Vice-Presidência e decisões monocráticas:** foram classificadas como "incerto".
  - **Art. 932, IV, do CPC:** em alguns casos o executor inferiu "favorável" da citação desse artigo. Essas classificações são para conferir.
- **Não pertinentes (245):** outro tributo (ITBI, ISS, ICMS, TFF), questões entre particulares e ementas que não nomeiam o tributo. Neste último caso o executor foi conservador, e o critério oscilou entre lotes: alguns marcaram como pertinente pelo eixo do indício.

## 4. Próximo passo sugerido
Escolher de 4 a 6 teses para dossiê (Walton e Élenchos, com leitura pelo Opus de amostra representativa e inteiro teor pelo PJe ou pela PDPJ). Candidatas, por volume e utilidade:
1. prescrição originária, com o marco da constituição e o efeito do despacho de citação;
2. prescrição intercorrente;
3. execução de valor irrisório (Tema 1.184);
4. ilegitimidade passiva (promitente comprador, alienante, espólio);
5. nulidade da CDA e cobrança em duplicidade;
6. teses de mérito do tributo (majoração por decreto, planta genérica, progressividade, área, bitributação entre municípios).
