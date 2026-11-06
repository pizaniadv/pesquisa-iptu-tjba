---
tipo: protocolo-anexo
data: 2026-11-05
produzido-por: claude-code
versao-core: 1.0
status: vigente
---

# T2 — triagem de pertinência, regra v1 (anexo ao protocolo v2 §5, item 4)

Congelada em 05/11/2026, antes da primeira execução (calibração no piloto e lote E4-IPTU04). Mudança só por nova versão, com justificativa em `auditoria/correcoes.jsonl`.

## 1. Unidade, entrada e executor
- Unidade: o candidato (uma decisão).
- Entrada: um **pacote** determinístico, montado por `scripts/pacote_t2.py` a partir de `evidencias/extracoes/<id>.txt` (já limpo pela `limpar_html v1`):
  - a ementa inteira, com teto de 3.000 caracteres;
  - janelas de ±350 caracteres em torno de `iptu | predial | territorial | imun | isen | tribut | lançamento | cda | execução fiscal`, fundidas, com teto de 2.500;
  - os últimos 700 caracteres do conteúdo, onde costuma estar o dispositivo.
  - O sha256 do pacote fica no recibo.
- Executor: Sonnet (subagente), em lotes de até 50 pacotes. O executor não consulta nenhuma outra fonte.

## 2. Vereditos
- **`pertinente`**: a decisão examina (ou declara não examinar por motivo processual) uma questão em que o IPTU é a **obrigação tributária** discutida entre contribuinte (ou responsável) e ente tributante. Entram:
  - lançamento, cobrança, execução fiscal, imunidade, isenção, base de cálculo, sujeição passiva, prescrição, repetição;
  - taxa cobrada junto com o IPTU, quando o IPTU também está em causa.
- **`nao_pertinente`**, com um motivo de `config/taxonomia.yaml`:
  - **EXC-07**: o IPTU só como dado de fato. Exemplos: encargo de locação, valor cobrado pela construtora, conta do imóvel a reembolsar, comprovante, partilha, alimentos, condomínio, dever entre particulares sem o ente na causa sobre o crédito. Esse é o padrão dos 5 casos excluídos no piloto (`auditoria/exclusoes-registros.jsonl`).
  - **EXC-01, EXC-02 ou EXC-05**: conforme a taxonomia.
- **`duvida`**: o pacote não basta para decidir. **Dúvida nunca exclui**: vai à T3 (Opus), que lê o texto inteiro.

## 3. Campos da saída (um JSON por linha)
`{"id", "veredito", "motivo" (EXC-0x ou null), "eixos" (IPTU-xx efetivamente examinados, lista, pode ser vazia), "imunidade_ou_isencao_examinada" (true/false/null), "excerto" (cópia literal do pacote, 20 a 300 caracteres, que sustenta o veredito), "nota" (até 200 caracteres)}`

## 4. Conferência por código (`scripts/consolidar_t2.py`)
- Cada linha é validada: campos, enums e excerto literal no texto limpo do `.txt` (`limpar_html v1` aplicada ao `.txt`; nos `.txt` do piloto, extraídos ainda com HTML, é isso que dá o texto do pacote; tolerância só para espaços colapsados, a mesma do `validar.py`).
- Linha reprovada: o candidato **não** sai do funil; volta como `duvida` com o motivo "T2 reprovada na conferência".
- Recibo por candidato em `auditoria/triagem-T2-<lote>.jsonl`, com modelo, versão desta regra, versão do brief, sha256 do pacote e veredito.

## 5. Calibração (antes de produção)
Rodar a T2 sobre os 24 registros do piloto, cujo desfecho de pertinência já é conhecido. Aceite:
- os 5 EXC-07 do piloto saem `nao_pertinente` ou `duvida`;
- **nenhum** dos 19 mantidos sai `nao_pertinente`.

Falhando o aceite, o brief é corrigido (nova versão) e a calibração se repete. A produção só começa com a calibração aprovada.

## 6. O que a T2 não é
- É indício e filtro de pertinência, não classificação. O resultado favorável ou desfavorável é da T3.
- O denominador da jurimetria continua sendo o candidato da trilha neutra: a T2 só registra quantos saíram por pertinência e por quê.
