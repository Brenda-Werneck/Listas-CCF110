//Escreva um algoritmo que informe se um número é par ou ímpar. O algoritmo deve utilizar uma função que retorne 0 caso o número seja par e 1 caso o número seja ímpar.

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double Delta(double a, double b, double c)
{
    return (b * b) - 4 * a * c;
}

void raizes(double a, double b, double c)
{
    double delta = Delta(a, b, c);
    if (delta < 0)
    {
        printf("Delta negativo\n");
    }
    else
    {
        double x1 = (-b + sqrt(delta)) / (2 * a);
        double x2 = (-b - sqrt(delta)) / (2 * a);
        printf("x1 = %lf\n", x1);
        printf("x2 = %lf\n", x2);
    }
}

int main()
{
    double n;
    n = 0;
    printf("\nDigite o valor de a: ");
    scanf("%lf", &a);
    printf("\nDigite o valor de b: ");
    scanf("%lf", &b);
    printf("\nDigite o valor de c: ");
    scanf("%lf", &c);
    raizes(a, b, c);

    system("PAUSE");
    return 0;
}