#

# Instruções de entrada e saída

# Instruções de entrada e saída

Profa. Andréa Aparecida Konzen

Fundamentos de Programação

Escola Politécnica - PUCRS
---
#

# Instruções de Entrada

# Instruções de Entrada

Este documento é um conjunto de slides de faculdade. Há código.
---
#

# Instruções de Saída

# Instruções de Saída

22
#

GMLmzd2

6C)- Criação das variáveis

OLw-#y

2 mc?

2Jx
---
#
# Criação das variáveis e constantes

# Criação das variáveis e constantes

# Constantes

Constantes são valores que não se alteram:

- Por convenção, seus identificadores são escritos em caixa alta.
- A declaração de constantes exige a palavra reservada final.

final tipo identificadorConstante = valor;
Exemplo: final double TAXA = 25;
---
#

# Criação das variáveis e constantes

# Criação das variáveis e constantes

L6An

3Iuutodo sakdta

permitem receber os valores informados pelo usuário:

usamos a classe Scanner para ler os dados informados via teclado.

necessário Importar a classe Scanner

import java.util.Scanner;
// e Instanciar um objeto Scanner:
Scanner in = new Scanner(System.in);
---
#

# Slides de Faculdade

# Criação das variáveis e constantes

2Icuusada Entada

Para ker umIntuse 8 noxtIat ()

- 8trlnguge:nextDoublo
- doubleu8e : nextLLno ()

Exemel:doubloraio in.noxtDouble () ;
---
#
# Slides de Faculdade

# Criação das variáveis e constantes

aula de Saída

Escreve na tela informações para o usuário System.out.Print("item: " + item);

System.out.println("item: " + item);

Exemplo System.out.print("Informação do valor do item:");
---
#

# Slides de Faculdade

# Código em Java para cálculo do volume de uma esfera

import java.util.Scanner;
import java.lang.Math;

public class VolumeDaEsfera {
public static void main(String args[]) {
Scanner teclado = new Scanner(System.in);
double raio, volume;
System.out.print("Informe o raio: ");
raio = teclado.nextDouble();
volume = 4.0/3 * Math.PI * Math.pow(raio, 3);
System.out.println("Volume: " + volume);
}
}
---
#

# Slides de Faculdade

# EntradaSaida

# ex-EntradaSaida

- Compilar
- Desfazer
- Recortar
- Copiar
- Colar
- Procurar
- Fechar
- Codigo-fonte

+*

Escreva uma descrição da classe EntradaSaida aqui.

@version (seu número da versão ou uma data)

@author (um nome)

public class EntradaSaida {
// biblioteca para as entradas
import java.util.Scanner;

public static void tecladoMain(String args[]) {
Scanner teclado = new Scanner(System.in); // criação do Scanner

// declaração das variáveis
double valor1;
String nome;
int valor2;

System.out.print("Informe o nome: ");
nome = teclado.nextLine();

System.out.print("Digite o valor 1: ");
valor1 = teclado.nextDouble();

System.out.print("Informe o valor 2: ");
valor2 = teclado.nextInt();

System.out.println("Nome: " + nome + " Valor 1: " + valor1 + " Valor 2: " + valor2);
}
}