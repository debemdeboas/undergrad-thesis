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
| a     | b     | a && b | a  \|\| b | !a    | !b    |
| ----- | ----- | ------ | --------- | ----- | ----- |
| false | false | false  | false     | true  | true  |
| false | true  | false  | true      | true  | false |
| true  | false | false  | true      | false | true  |
| true  | true  | true   | true      | false | false |
---
# PROGRAMAS COM SELEÇÃO

Instruções de seleção

- Usando instrução if em
- - Seleção simples
- Seleção Composta
- Seleção Aninhada
- Seleção Encadeada

Usando switch
---
# PROGRAMAS COM SELEÇÃO

Instruções de seleção

Usando instrução Switch

| ExpressaoSwitch |
| --------------- |
| Case            | Codigo |
| Case 2          | Codigo |
| Case N          | Codigo |
| Default         | Codigo |
---
# PROGRAMAS COM SELEÇÃO

Usando instrução Switch

Sintaxe:

```java
switch (expressão) {
    case valor1:
        // bloco de código que será executado
        break;
    case valor2:
        // bloco de código que será executado
        break;
    case valorN:
        // bloco de código que será executado
        break;
    default:
        // bloco de código que será executado se nenhum dos cases for aceito
}
```
---
# PROGRAMAS COM SELEÇÃO

Usando instrução Switch
switch (expressão): é onde passamos a variável de teste que servirá de referência para as comparações que o programa deve fazer;
case: é onde definimos o valor que será comparado com a variável de teste e o código que será executado caso sejam compatíveis;
break: é a declaração opcional de quebra;
default: é a declaração opcional padrão, na qual definimos o código que deve ser executado, se nenhum dos valores declarados nos cases for compatível com o valor passado na variável de teste.
---
# PROGRAMAS COM SELEÇÃO

Usando instrução Switch

Importante:

- cada switch pode conter um ou N cases;
- os valores dos cases não podem ser repetidos, caso contrário ocorrerá um erro durante a compilação do Código;
- o valor de cada case deve ser do mesmo tipo da expressão switch;
- os valores dos cases não podem ser variáveis;
- a variável passada no switch deve ser de um dos tipos aceitos pela estrutura (short, byte, long, int, enum, string).