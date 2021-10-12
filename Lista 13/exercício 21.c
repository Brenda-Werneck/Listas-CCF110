//Escreva um algoritmo que receba um vetor de vinte posições. Elabore uma função que retorne a soma dos quadrados dos elementos deste vetor.

#include <stdio.h>
#include <stdlib.h>

int soma(int vetor[20])
{
    int soma, i;
    soma = 0;
    for (i = 0; i < 20; i++)
    {
        soma += (vetor[i] * vetor[i]);
    }
    return(soma);
}

int main()
{
    int vetor[20], i;
    for (i = 0; i < 20; i++)
    {
        printf("\nDigite o %dº número: ", i + 1);
        scanf("%d", &vetor[i]);
    }
    printf("Soma = %d\n", soma(vetor));
    
    system("PAUSE");
    return 0;
}