// Crie um algoritmo que receba um número inteiro. Escreva uma função que retorne se este valor é positivo ou negativo.

#include <stdio.h>
#include <stdlib.h>

int positivonegativo(int n)
{
    if (n > 0)
    {
        return (1);
    }
    if (n < 0)
    {
        return (0);
    }
}

int main()
{
    int n;

    printf("Digite um número: ");
    scanf("%d", &n);

    if (n == 0)
    {
        printf("é um número neutro\n");
    }
    else if (positivonegativo(n) == 1)
    {
        printf("\nNúmero positivo\n");
    }
    else
    {
        printf("\nNúmero negativo\n");
    }

    system("PAUSE");
    return 0;
}