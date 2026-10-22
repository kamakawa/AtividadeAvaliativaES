# 2. Relatório de execução

## 2.1 Como executar
- Python: 3.11.9
- Bibliotecas: datetime e unittest
- Arquivo principal: codigo/main.py
- Comandos, a partir da raiz do repositório:
  - cd codigo
  - python -m unittest -v
  - python main.py

## 2.2 Plano versus realizado

| Etapa | Previsto | Realizado (data do commit) | Quem | Observação |
|---|---|---|---|---|
| 1. Histórias de usuário | 17/10 | 18/10 | Iago | Um dia atrasado |
| 2. Projeto inicial | 17/10 | 18/10 | Eric | Um dia atrasado |
| 3. Implementação | 19/10 | 19/10 | Eric | Dentro do previsto |
| 4. Testes | 20/10 | 19/10 (Eric) 22/10 (Iago) | Eric, Iago | Eric adiantou, Iago reforçou 2 dias depois do previsto |
| 5. Documentação | 21/10 | 22/10 | Iago | Um dia atrasado |

## 2.3 Atrasos e mudanças, com justificativa
1. Atraso das etapas 1 e 2: Falta de tempo no dia por parte do Iago e Eric dependia das histórias para fazer a etapa 2.
2. Etapa 2 previa todas as histórias; o enunciado pede só uma de prioridade Alta: Falta de leitura por parte da dupla.
3. Testes escritos pelo Eric junto com a implementação, e não pelo Iago depois: O Eric já estava com o código em mãos e aproveitou. O Iago os reforçou depois.
4. Escopo reduzido em relação à Parte 1 (login, formulário de grupo, punição automática, relatório de conteúdos): Falta de leitura e simplificação por causa do prazo de entrega.
5. Itens no código que o projeto inicial não citava (dicionário MONITORES, constantes LIVRE/RESERVADO/CANCELADO): o MONITORES associa um monitor a cada disciplina, e as constantes evitam repetir textos soltos no código.
6. Atraso da etapa 5: O tempo foi usado para reforçar os testes de aceitação antes de documentar, porque o relatório e o item 2 da documentação dependem do que os testes realmente cobrem. A listagem passou a provar que cancelados ficam de fora, as mensagens das exceções passaram a ser conferidas e o cálculo do fim passou a ser testado com a reserva feita e com uma virada de hora. 
