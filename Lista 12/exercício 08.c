//Construa um algoritmo para fazer a soma de vários valores inteiros e positivos, fornecidos pelo usuário através do teclado. O dado que finaliza a sequência de entrada é o número –1, e este não deve ser considerado.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
    int valor, soma;
    soma = 0;
    valor = 0;

    while (valor != -1)
    {
        printf("\nDigite um valor: \n");
        scanf("%d", &valor);
        if (valor != -1)
        {
            soma += valor;
        }
    }
    printf("\nSoma = %d", soma);

    return 0;
}