//Leia valores inteiros para a matriz A[3x5]. Gere e escreva o vetor SL (soma das 3 linhas), onde cada elemento é a soma dos elementos de uma linha da matriz A. Faça o trecho que gera a matriz SL separado (laços de repetição) da entrada e da saída de dados.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
    int A[3][5], vetorSL[3];
    int i, j, posicaoSl;

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j <3; j++)
        {
            printf("Digite um valor: ");
            scanf("%d", &A[i][j]);
        }
    }    
    posicaoSl = 0;

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j <3; i++)
        {
            vetorSL[posicaoSl] += A[i][j];
        }
        posicaoSl += 1;
    }

    for (i = 0; i <3; i++)
    {
        printf("%d", vetorSL[i]);
    }

    system("PAUSE");
    return 0;
}
