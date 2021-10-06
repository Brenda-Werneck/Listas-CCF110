//Elabore um algoritmo que crie dois vetores com 10 posições. O usuário digitará os valores do primeiro vetor. O segundo vetor vai receber os valores do primeiro vetor em ordem invertida (o último elemento do primeiro vetor será o primeiro do segundo, o penúltimo elemento do primeiro vetor será o segundo elemento e assim por diante).


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

    for (i=0; i<n; i++)
    {
        printf("\nDigite um valor para o vetor: \n");
        scanf("%d", &vetor[i]);
    }

    for (i=0; i<n; i++)
    {
        if (i % 2 == 0)
        {
            soma += vetor[i];
        }
    }
        
    printf("\nSoma = %d", soma);

    return 0;
}