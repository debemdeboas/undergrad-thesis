Programas com Repetição

PROFA. ANDRÉA APARECIDA KONZEN
FUNDAMENTOS DE PROGRAMAÇÃO
ESCOLA POLITÉCNICA - PUCRS

Material de Profa Andréa Aparecida Konzen
---
# PROGRAMAS COM Repetição

Até agora nossos programas foram feitos para 1 registro apenas. Por exemplo:

- Cálculo da média para 1 aluno
- Verificação de conta bancária para um cliente
- Índice de massa corporal para 1 pessoa

Estes são apenas exemplos mais comuns...
---

As estruturas de repetição são recursos fundamentais na programação que permitem executar uma sequência de instruções várias vezes de maneira automática.
---

Permitem automatizar tarefas repetitivas, reduzir o tempo de desenvolvimento de software e melhorar a eficiência e a qualidade do código.
lini Con Lion Conncct quando voce se sentir triste olhe os programas que voce fez quando estava comecandoprogramar
---

Antes de entrar nos comandos é importante saber:
Variáveis do tipo Contadores:
controlar uma repetição ou o número de vezes que uma ação for executada.
Ex.:
contar de 1 em 1
valor = 0;
...
valor = valor +1;
---

Antes de entrar nos comandos é importante saber:
Variáveis do tipo Acumuladores:
somar valores quaisquer, representando algo significativo para a lógica do programa.
Exs:
a soma de todos os valores de produtos de uma lista de compras;
a multiplicação de todos os valores de 1 a n para o calculo de um fatorial;
a soma das idades de todos os alunos.
valorAcumulado = 0;
...
valorAcumulado = valorAcumulado + valor;
---

Existem três tipos básicos de estruturas de repetição:

- While
- For
- Do-While
---

|While|executa um conjunto de instruções enquanto uma condição for verdadeira.|
|---|---|
|Significado:|pode ser executado várias vezes ou nenhuma, dependendo do valor da condição. A condição é avaliada antes de cada execução do loop.|
---
|
|---|
|While|While (A = TRUE) DoB|
| |End While|
| |FALSE|
| |A|
| |TRUE|
---
while (condição) {
// Bloco de código
}
---

While

Exemplo: Imprimir números de 0 a 9

```java
int i = 0;
while (i < 10) {
  System.out.println(i);
  i++;
}
```
---
For

- usada quando sabemos exatamente quantas vezes queremos executar um conjunto de instruções.
- Composto por três partes: inicialização, condição e incremento.
---
|Programas com Repetição|
|---|
|For|Inicialização|Definição do valor inicial da variável de controle do loop.|
| |Condição|Especificação a condição para a execução do loop.|
| |Incremento|Atualização do valor da variável de controle do loop.|
---
|PROGRAMAS COM|Repetição|
|---|---|
|For|INITIALIZATION|
| |CONDITIONfalse|
| |true|
| |LOOP BODY|
| |UPDATE|
| |For loop|
---
# PROGRAMAS COM Repetição

for

```java
for (inicialização; condição; atualização) {
  // Bloco de código
}
```
---
For 

Exemplo: Imprimir números de 0 a 9

```java
for (int i=0; i<10; i++){
  System.out.println(i);
}
```
---
Do-While

estrutura de repetição que executa um conjunto de instruções pelo menos uma vez e, em seguida, repete a execução enquanto uma condição é verdadeira. A condição é avaliada após cada execução do loop, ou seja, o loop será executado pelo menos uma vez, independentemente do valor da condição.
---
Do-While

```java
do {
  // Bloco de código|
} while (condição);
```
---
PROGRAMAS COM Repetição

Do-While
Exemplo: imprimir números de 0 a 9
A variável i é inicializada com 0 antes do loop. O bloco de código dentro do do é executado uma vez, imprimindo 0 na saída. Em seguida, a variável i é incrementada em 1. O loop continua a ser executado enquanto i for menor do que 10. Na próxima iteração, o valor de i é 1, então o bloco de código imprime 1 na saída e assim por diante, até que i atinja o valor de 9 e o loop termine.
int i = 0;
do {
System.out.println(i);
i++;
} while (i < 10);
---
PROGRAMAS COM Repetição

Break e Continue

Funcionalidade: controle de fluxo do programa.

break interrompe o loop completamente. O programa continuará a partir da próxima linha após o loop.

continue interrompe a iteração atual do loop e continua com a próxima iteração.
---
PROGRAMAS COM Repetição

Break e Continue - exemplos

for (int i = 0; i < 10; i++) {
if (i == 5) {                O seguinte for imprimirá os
continue;                   números de 0 a 9, mas
}                                pulará o número 5
System.out.println(i);
}
---
PROGRAMAS COM Break e Continue - exemplos

Repetição
while continuará executando até que o usuário digite o valor 0. Quando o usuário digitar 0, o loop será interrompido com a instrução break e o programa imprimirá uma mensagem de saída. Se o usuário digitar qualquer outro valor diferente de 0, o programa continuará imprimindo o valor na tela.

while (true) {

&nbsp;&nbsp;&nbsp;&nbsp;System.out.print("Digite um número (digite 0 para sair): ");

&nbsp;&nbsp;&nbsp;&nbsp;numero = scanner.nextInt();

if (numero == 0) {

&nbsp;&nbsp;&nbsp;&nbsp;System.out.println("Você digitou 0, saindo do programa...");

&nbsp;&nbsp;&nbsp;&nbsp;break; }

System.out.println("Você digitou o número " + numero);

}