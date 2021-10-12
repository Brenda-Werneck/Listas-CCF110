//Escreva um algoritmo que receba um vetor de inteiros de 5 posições. Crie uma função que retorne quais elementos deste vetor são divisíveis por 3.

#include <stdio.h>
#include <stdlib.h>

void divtres(int vetor[5])
{
    int i;
    for (i = 0; i < 5; i++)
    {
        if (vetor[i] % 3 == 0)
        {
            printf("%d ", vetor[i]);
        }
    }
}

int main()
{
    int vetor[5], i;
    for (i = 0; i < 5; i++)
    {
        printf("\nDigite o %dº número: ", i + 1);
        scanf("%d", &vetor[i]);
    }
    divtres(vetor);
    printf("\n");
    system("PAUSE");
    return 0;
}