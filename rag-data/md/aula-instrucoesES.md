# Instruções de entrada e saída

Profa. Andréa Aparecida Konzen

Fundamentos de Programação

Escola Politécnica - PUCRS
---
# Instruções de Entrada 

Como o usuário como deve informar os dados (via teclado)

Scanner
import java.util.Scanner

Criar o Scanner dentro da classe
Scanner teclado = new Scanner(System.in);

Receber via teclado o que deve ser guardado na variável
nomedavariavel = teclado.nextLine();
---
# Instruções de saída

Como o usuário deve informar a saída (tela)

System.out.print("Informe o nome:");
System.out.print(variavel);
---
# Criação das variáveis e constantes

Constantes são valores que não se alteram:

- Por convenção, seus identificadores são escritos em caixa alta.
- A declaração de constantes exige a palavra reservada final.

final tipo identificadorConstante = valor;
Exemplo: final double TAXA = 25;
---
# Criação das variáveis e constantes

Instruções de entrada

- permitem receber os valores informados pelo usuário
- usamos a classe Scanner para ler os dados informados via teclado.
- necessário:
  - Importar a classe Scanner: import java.util.Scanner;
  - e Instanciar um objeto Scanner: Scanner in = new Scanner(System.in);
---
# Criação das variáveis e constantes
Instruções de entrada

Para ler um:
- Int use nextInt()
- Double use nextDouble()
- String use: nextLine()

Exemplo:
double raio = in.nextDouble();
---
# Criação das variáveis e constantes
Instruções de Saída

Escreve na tela informações para o usuário System.out.Print("item: " + item);

System.out.println("item: " + item);

Exemplo: System.out.print("Informação do valor do item:");
---
Veja como fica em Java...

```java
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
```