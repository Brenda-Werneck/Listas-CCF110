//Fazer um algoritmo para calcular e escrever a seguinte soma:
//S = (37x38)/1 + (36x37)/2 + (35x36)/3 + ...+(1x2)/37

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
    float soma, cont, i;

    soma = 0;
    cont = 1;

    for (i = 37; i > 0; i--)
    {
        soma += i * (i + 1) / cont;
        cont += 1;
    }
    printf("\nSoma = %f\n", soma);

    return 0;
}