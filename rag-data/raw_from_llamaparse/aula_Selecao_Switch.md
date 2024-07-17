#

# Programas com Seleção

# Programas com Seleção

# PROFA. ANDRÉA APARECIDA KONZEN

# FUNDAMENTOS DE PROGRAMAÇÃO

# ESCOLA POLITÉCNICA - PUCRS

Material adaptado a partir do material da Profa Silvia
---
#
# Programas com Seleção

# Programas com Seleção

- Diferente dos programas puramente sequenciais, agora nem todas as instruções serão executadas.
- Para isso será necessário trabalhar com expressões lógicas.
- Expressões Lógicas são aquelas que resultam em true ou false.
---
#
# Programas com Seleção

# Programas com Seleção

- Expressões Lógicas são aquelas que resultam em true ou false.
- Para definir expressões lógicas, usamos operadores:
- Relacionais: >, <, >=, <=, !=, ==
- Lógicos: && (E), || (ou) e ! (não)
---
#

# Programas com Seleção

# Programas com Seleção

# Operadores Lógicos:

- && (E)
- || (ou)
- ! (não)

# Tabela Verdade:

a
b
a && b
a || b
!a
!b

false
false
false
false
true
true

false
true
false
true
true
false

true
false
false
true
false
true

true
true
true
true
false
false
---
#
# Programas com Seleção

# Instruções de seleção

# Usando instrução if em

- Seleção simples
- Seleção Composta
- Seleção Aninhada
- Seleção Encadeada

# Usando switch

- Seleção múltipla
---
#
# Programas com Seleção

# Instruções de seleção

Usando instrução Switch

ExpressaoSwitch
Case    Codigo
Case 2  Codigo
Case N  Codigo
DefaultCodigo
---
#

# Programas com Seleção

# Usando instrução Switch

# Sintaxe:

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
---
#

# Slides de Faculdade

# Programas com Seleção

Usando instrução Switch

- switch (expressão): é onde passamos a variável de teste que servirá de referência para as comparações que o programa deve fazer;
- case: é onde definimos o valor que será comparado com a variável de teste e o código que será executado caso sejam compatíveis;
- break: é a declaração opcional de quebra;
- default: é a declaração opcional padrão, na qual definimos o código que deve ser executado, se nenhum dos valores declarados nos cases for compatível com o valor passado na variável de teste.
---
#

# Slides de Faculdade

# PROGRAMAS COM SELEÇÃO

Usando instrução Switch

Importante:

- Cada switch pode conter um ou N cases;
- Os valores dos cases não podem ser repetidos, caso contrário ocorrerá um erro durante a compilação do Código;
- O valor de cada case deve ser do mesmo tipo da expressão switch;
- Os valores dos cases não podem ser variáveis;
- A variável passada no switch deve ser de um dos tipos aceitos pela estrutura (short, byte, long, int, enum, string).