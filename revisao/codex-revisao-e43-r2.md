## GRAVE

Não há achado grave novo criado pelas correções.

1. **Item 1 — resolvido.** Não encontrei ficha que ainda conclua “admissibilidade” apenas pelo rótulo “2ª Vice-Presidência”. Os casos apontados foram reclassificados pelo texto da decisão, inclusive nas TES-07 e TES-21 ([correções:7](auditoria/correcoes-pos-codex-e43.jsonl:7), [TES-21:27](analises/fichas/TES-21-planta-generica-de-valores.md:27)). As demais menções distinguem expressamente metadado, acórdão transcrito e decisão real de admissibilidade; o índice registra essa conferência ([00-INDICE.md:55](analises/fichas/00-INDICE.md:55)).

2. **Item 2 — não resolvido; o motivo não se sustenta.** A H1 alcança recurso **inadmitido**, negativa de seguimento e óbices equivalentes ([harmonizacao-t3-v1.md:15](metodologia/harmonizacao-t3-v1.md:15)). Aqui ocorreu o contrário: a preliminar municipal foi examinada e rejeitada, e o agravo da contribuinte foi conhecido ([registro:123](estado/t3/releitura-h2/DEC-TJBA-fd5f8aeaf0cc.json:123), [Acórdão:177](evidencias/pdpj/DEC-TJBA-fd5f8aeaf0cc/0047-Acórdão.txt:177)). A regra 5 exige resultado por questão e apenas adverte que admissibilidade não é adesão ao mérito ([CLAUDE.md:17](CLAUDE.md:17)); ela não manda apagar uma vitória processual efetivamente decidida. O dicionário também reserva `sem_exame` à questão não examinada e define `favoravel_integral` como obtenção integral do pedido naquela questão ([dicionário:33](metodologia/dicionario-de-dados.md:33), [dicionário:36](metodologia/dicionario-de-dados.md:36)). O “irmão” não valida a solução: nele a preliminar da contribuinte foi rejeitada e o recurso do Município conhecido, portanto a contribuinte perdeu aquela questão ([eec4d6425623:123](dados/decisoes/DEC-TJBA-eec4d6425623.json:123)). A Q1 de `fd5f8aeaf0cc` continua devendo ser `favoravel_integral`, com benefício processual, sem confundi-la com vitória de mérito.

## MÉDIO

3. **Item 3 — resolvido.** Os 32 JSON têm `n_acervo` como total do recorte e `n_acervo_fav` como subconjunto favorável; os valores coincidem com as duas colunas do índice. Exemplo: TES-16, 1.079 e 172 ([JSON:5](analises/fichas/TES-16-dano-moral-protesto-cobranca-indevida.json:5), [índice:30](analises/fichas/00-INDICE.md:30)).

4. **Item 4 — resolvido.** O nono recibo agora possui versão e fonte próprias da antialucinação, além de nota que explica o reaproveitamento do script ([ajustes-conferencia-it.jsonl:9](auditoria/ajustes-conferencia-it.jsonl:9)).

5. **Item 5 — parcialmente resolvido.** O snapshot deixou de ser sobrescrito e o código de saída do validador é testado ([fechar_releitura_h2.py:70](scripts/fechar_releitura_h2.py:70), [linha 75](scripts/fechar_releitura_h2.py:75)). Porém o registro e o recibo são gravados antes da validação ([linhas 71–76](scripts/fechar_releitura_h2.py:71)); se ela reprovar, o estado inválido já ficou persistido e o log fará a retomada pular o item ([linhas 24–29](scripts/fechar_releitura_h2.py:24)). Portanto, os dois defeitos concretos foram corrigidos, mas a operação continua não transacional.

6. **Item 6 — resolve os riscos originais.** Uma resposta vazia não substitui uma lista boa ([pdpj_inteiro_teor.py:52](scripts/pdpj_inteiro_teor.py:52)); a retomada exige texto e metadado, e o texto é instalado por troca atômica depois do metadado ([linhas 82–90](scripts/pdpj_inteiro_teor.py:82)). Há, contudo, uma regressão nova descrita ao final.

7. **Item 7 — parcialmente resolvido.** O código futuro registra separadamente o resultado no Markdown e no JSON ([aplicar_antialucinacao.py:34](scripts/aplicar_antialucinacao.py:34), [linha 37](scripts/aplicar_antialucinacao.py:37)). Mas os 237 recibos já existentes continuam sem os campos `md` e `json` ([aplicacao-antialucinacao.jsonl:1](auditoria/aplicacao-antialucinacao.jsonl:1), [linha 237](auditoria/aplicacao-antialucinacao.jsonl:237)). A correção é apenas prospectiva.

8. **Item 8 — resolvido.** O índice agora é construído por número CNJ e as evidências são associadas ao processo correspondente ([conferir_fichas.py:39](scripts/conferir_fichas.py:39), [linhas 62–66](scripts/conferir_fichas.py:62)). O relatório atual soma 602 excertos, sem falhas nem itens fora do processo.

9. **Item 9 — resolvido.** As afirmações apontadas passaram a trazer contagem e recorte ou foram retiradas: quatro contrárias explicitamente não denominadoras na TES-04 ([linha 130](analises/fichas/TES-04-ilegitimidade-passiva-execucao.md:130)); 11 de 11, com período, na TES-08 ([linha 115](analises/fichas/TES-08-aliquota-e-seletividade.md:115)); e limite explícito sobre a ausência do primeiro grau na TES-37 ([linha 69](analises/fichas/TES-37-gratuidade-executado.md:69)).

## LEVE

10. **Item 10 — resolvido.** O frontmatter identifica v4 e revisão já feita, e tanto o título quanto a formulação dizem v4 ([TES-001:8](analises/teses/TES-001-imunidade-onus-da-destinacao.md:8), [linha 13](analises/teses/TES-001-imunidade-onus-da-destinacao.md:13), [linha 18](analises/teses/TES-001-imunidade-onus-da-destinacao.md:18)).

## Achado novo criado pelas correções

- **MÉDIO — retomada pode quebrar após interrupção durante a gravação do metadado PDPJ.** A correção passou a gravar diretamente o `.meta.json` antes do texto ([pdpj_inteiro_teor.py:85](scripts/pdpj_inteiro_teor.py:85)). Se houver interrupção durante esse `json.dump`, fica um JSON parcial; na retomada, o código tenta carregá-lo sem tratamento antes de verificar o par completo e encerra o lote com erro ([linha 79](scripts/pdpj_inteiro_teor.py:79)). O metadado também precisa de arquivo temporário e troca atômica.

Não identifiquei achado novo grave ou leve. Nenhum arquivo foi alterado.
