//Crie um algoritmo para resolver equações de segundo grau. O algoritmo deve utilizar funções para calcular:
//O valor de delta;
//O valor das raízes.

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
    double a, b, c;
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