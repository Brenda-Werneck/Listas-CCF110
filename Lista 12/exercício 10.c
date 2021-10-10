//Escreva um algoritmo que leia um vetor de tamanho n (informado pelo usuário) e escreva a soma de todos os elementos de índice par.


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
    int n, soma, i;
    
    printf("\nDigite o tamanho do seu vetor: \n");
    scanf("%d", &n);
    int vetor[n];
    soma = 0;

    for (i = 0; i < n; i++)
    {
        printf("\nDigite um valor para o vetor: \n");
        scanf("%d", &vetor[i]);
    }

    for (i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            soma += vetor[i];
        }
    }
        
    printf("\nSoma = %d", soma);

    return 0;
}