//Elabore um algoritmo que receba os valores de um vetor de inteiros de 15 posições. Crie uma função que calcule e retorne a soma destes valores.

#include <stdio.h>
#include <stdlib.h>

int soma(int vetor[15])
{
    int soma, i;
    soma = 0;
    for (i = 0; i < 15; i++)
    {
        soma += vetor[i];
    }
    return(soma);
}

int main()
{
    int vetor[15], i;
    for (i = 0; i < 15; i++)
    {
        printf("\nDigite o %dº número: ", i + 1);
        scanf("%d", &vetor[i]);
    }
    printf("Soma = %d", soma(vetor));
    
    system("PAUSE");
    return 0;
}