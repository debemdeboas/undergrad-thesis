#

# Slides de Faculdade

# Programas com Seleção

# PROFA. ANDRÉA APARECIDA KONZEN

# FUNDAMENTOS DE PROGRAMAÇÃO

# ESCOLA POLITÉCNICA - PUCRS

Material adaptado a partir do material da Profa Silvia
---
#

# Slides de Faculdade

# PROGRAMAS COM SELEÇÃO

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

# Operadores Lógicos

- && (E)
- || (ou)
- ! (não)

# Tabela Verdade

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

# Definindo expressões lógicas...

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

# Programas com Seleção

# Instruções de seleção

- Expressão: false
- Usando instrução if em Lógica

# Sintaxe:

if(expressão lógica)  instrução;    Instrução
ou
if(expressão lógica)  {
instrução1;
instrução2;
...
}
---
#

# Programas com Seleção

# Programas com Seleção

Usando instrução if em false

- Seleção simples ExpressãoLógica

Problema:

Verificar se um número inteiro é:

- positivo
- negativo
- zero

Solução: Programando no BlueJ ...