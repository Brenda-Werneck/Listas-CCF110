//Escreva um algoritmo que leia um número e escreva a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
    float num, quad, raiz;
    printf("\nDigite o número: ");
    scanf("%f", &num);
    if (num < 0) 
    {
        quad = num * num;
        printf("\nnúmero ao quadrado = %f\n", quad);
        system("PAUSE");
    }
    if (num >= 0)
    {
        raiz = sqrt(num);
        printf("\nraíz quadrada do número = %f\n", raiz);
        system("PAUSE");
    }
    return 0;
}