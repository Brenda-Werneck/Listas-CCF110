//Escreva um algoritmo que receba três números. Elabore uma função que retorne o menor número entre os digitados.

#include <stdio.h>
#include <stdlib.h>

double menornum(double n1, double n2, double n3)
{
    double menor;
    menor = n1;
    if (n2 < menor)
    {
        menor = n2;
    }
    if (n3 < menor)
    {
        menor = n3;
    }
    return menor;
}

int main()
{
    double n1, n2, n3;

    printf("Digite o primeiro número: ");
    scanf("%lf", &n1);
    printf("Digite o segundo número: ");
    scanf("%lf", &n2);
    printf("Digite o terceiro número: ");
    scanf("%lf", &n3);

    printf("Menor = %lf\n", menornum(n1, n2, n3));

    system("PAUSE");
    return 0;
}