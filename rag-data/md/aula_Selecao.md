# Programas com Seleção

PROFA. ANDRÉA APARECIDA KONZEN

FUNDAMENTOS DE PROGRAMAÇÃO

ESCOLA POLITÉCNICA - PUCRS

Material adaptado a partir do material da Profa Silvia
---
PROGRAMAS COM SELEÇÃO

- Diferente dos programas puramente sequenciais, agora nem todas as instruções serão executadas.
- Para isso será necessário trabalhar com expressões lógicas.
- Expressões Lógicas são aquelas que resultam em true ou false.
---
PROGRAMAS COM SELEÇÃO

- Expressões Lógicas são aquelas que resultam em true ou false.
- Para definir expressões lógicas, usamos operadores:
- Relacionais: >, <, >=, <=, !=, ==
- Lógicos: && (E), || (ou) e ! (não)
---
| a     | b     | a && b | a \|\| b | !a    | !b    |
| ----- | ----- | ------ | -------- | ----- | ----- |
| false | false | false  | false    | true  | true  |
| false | true  | false  | true     | true  | false |
| true  | false | false  | true     | false | true  |
| true  | true  | true   | true     | false | false |
---
# PROGRAMAS COM SELEÇÃO

Definindo expressões lógicas...

Considere a seguinte declaração: int num1, num2, num3;

Construa uma expressão lógica que resulte em true, quando:

1. num1 é positivo
2. num2 é par
3. num3 está no intervalo [0;10]
4. num1 não está no intervalo [0;10]
5. num2 é o maior dos 3
6. num2 é divisível por 7
7. num2 e num3 são múltiplos
---
# PROGRAMAS COM SELEÇÃO

Instruções de seleção

Usando instrução if em
- Seleção simples
- Seleção Composta
- Seleção Aninhada
- Seleção Encadeada

Usando switch
- Seleção múltipla
---
# PROGRAMAS COM SELEÇÃO

Usando instrução if em Seleção simples

Sintaxe:

```
if(expressão lógica) instrução;
```

ou

```
if(expressão lógica)  {
    instrução1;
    instrução2;
    ...
}
```
---
# PROGRAMAS COM SELEÇÃO

Usando instrução if em Seleção simples

Problema: Verificar se um número inteiro é:
- true
- positivo
- negativo
- zero

Solução: Programando no BlueJ ...