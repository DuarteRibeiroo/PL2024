# TPC4

## Autor
- Duarte Ribeiro (a100764)

Neste trabalho foi-nos pedido para fazer um programa que analisasse lexicamente a expressão ``SELECT id, nome, salario FROM empregados WHERE salario >= 820``. Daí generalizei e optei por fazer um analisador léxico (das partes mais comuns) da linguagem SQL. O código é muito semelhante ao código exemplo apresentado pelo professor (presente na documentação do *lex*). Apenas foi necessário alterar os tipos de símbolos para a linguagem SQL e o reconhecimento dos mesmos. Como já dito acima, optei por também tornar reconhecíveis símbolos SQL não presentes na expressão dada pelo professor, por questão de tornar este trabalho um pouco mais completo, mas não revelou grande dificuldade, pois apenas era necessáriom adicionar expressões novas ou completar as já presentes.