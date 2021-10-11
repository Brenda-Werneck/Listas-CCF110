// Crie um programa que receba valores para um vetor de inteiros de 10 posições. Elabore uma função que retorne os valores do vetor em ordem crescente.

#include <stdio.h>
#include <stdlib.h>

int crescente(int vetor[10])
{
    int aux, i, j;
    for(i = 0; i < 10; i++)
    {
        for(j = i + 1; j < 9; j++)
        {
            if(vetor[i] > vetor[j])
            {
                aux = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = aux;
            }
        }
    }
}

int main()
{
    int i, vetor[10];

    for (i = 0; i < 10; i++)
    {
        printf("\nDigite o %dº número: ", i + 1);
        scanf("%d", &vetor[i]);
    }
    crescente(vetor);

    for (i = 0; i < 10; i++)
    {
        printf("%d\n", vetor[i]);
    }

    system("PAUSE");
    return 0;
}