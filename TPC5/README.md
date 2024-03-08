# TPC4

## Autor
- Duarte Ribeiro (a100764)

Foi-nos pedido para simular uma máquina de _vending_, onde o foco principal do exercício era a análise léxica de cada um dos comandos. Optei por criar quatro tipos de tokens:
 - Currency: Identifica dinheiro, e que é reconhecido por uma função que o transformava num inteiro em cêntimos
 - Num : Identifica números, utilizado para o ID do produto a selecionar, transformado para inteiro
 - Delimiter: Usado para delimitar as moedas a introduzir
 - Reserved: Palavras reservadas (listar,moeda,selecionar,sair)
A cada linha o tipo de token é detetado e a lógica do programa depois é executada dependendo do token.