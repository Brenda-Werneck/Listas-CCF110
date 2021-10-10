//Elabore um algoritmo que faça, com funções, as seguintes conversões de temperatura:
//Fahrenheit para Celsius;
//Fahrenheit para Kelvin;
//Celsius para Fahrenheit;
//Celsius para Kelvin;
//Kelvin para Fahrenheit;
//Kelvin para Celsius;
//Obs.: Desenvolva uma função para cada conversão.

#include <stdio.h>
#include <stdlib.h>

double FC(double f)
{
    return ((f - 32) * 5) / 9;
}
double FK(double f)
{
    return (((f - 32) * 5) / 9) + 273.15;
}
double CF(double c)
{
    return ((c * 9) / 5) + 32;
}
double CK(double c)
{
    return c + 273.15;
}
double KF(double k)
{
    return (((k - 273.15) * 9) / 5) + 32;
}
double KC(double k)
{
    return k - 273.15;
}

int main()
{
    double c, f, k;
    int temp, tempdesejada;

    printf("Digite qual a medida de temperatura que está usando (1 - C, 2 - K ou 3 - F): ");
    scanf("%d", &temp);
    printf("Digite qual a medida de temperatura que deseja converter (1 - C, 2 - K ou 3 - F): ");
    scanf("%d", &tempdesejada);
    if (temp == 1)
    {
        printf("Digite a temperatrura em ºC: ");
        scanf("%lf", &c);
        if (tempdesejada == 2)
        {
            printf("%.2lf K\n", CK(c));
        }
        if (tempdesejada == 3)
        {
            printf("%.2lf F\n", CF(c));
        }
    }
    if (temp == 2)
    {
        printf("Digite a temperatrura em Kelvin: ");
        scanf("%lf", &k);
        if (tempdesejada == 1)
        {
            printf("%.2lf ºC\n", KC(k));
        }
        if (tempdesejada == 3)
        {
            printf("%.2lf F\n", KF(k));
        }
    }
    if (temp == 3)
    {
        printf("Digite a temperatrura em Fahrenheit: ");
        scanf("%lf", &f);
        if (tempdesejada == 1)
        {
            printf("%.2lf ºC\n", FC(f));
        }
        if (tempdesejada == 2)
        {
            printf("%.2lf K\n", FK(f));
        }
    }

    system("PAUSE");
    return 0;
}
