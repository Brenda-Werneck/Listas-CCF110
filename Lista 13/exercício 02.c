//Escreva um algoritmo que informe se um número é par ou ímpar. O algoritmo deve utilizar uma função que retorne 0 caso o número seja par e 1 caso o número seja ímpar.

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int teste(int n)
{
    return n % 2;
}

void parouimpar(int n)
{
    int poi = teste(n);
    if (poi == 0)
    {
        printf("0\n");
    }
    else
    {
        printf("1\n");
    }
}

int main()
{
    int n;
    printf("\nDigite um número: ");
    scanf("%d", &n);
    if (teste(n) == 1)
    {
        printf("%d é ímpar\n", n);
    }
    else if(teste(n) == 0)
    {
        printf("%d é par\n", n);
    }

    system("PAUSE");
    return 0;
}