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
    char temp, tempdesejada;

    printf("Digite qual a medida temperatura que está usando (C, K ou F): ");
    scanf("%c", &temp);
    printf("Digite qual a medida temperatura que deseja converter (C, K ou F): ");
    scanf("%c", &tempdesejada);
    if (temp == "C")
    {
        printf("Digite a temperatrura em ºC: ");
        scanf("%lf", &c);
        if (tempdesejada == "K")
        {
            printf("%2lf K", CK(c));
        }
        if (tempdesejada == "F")
        {
            printf("%2lf F", CF(c));
        }
    }
    if (temp == "K")
    {
        printf("Digite a temperatrura em Kelvin: ");
        scanf("%lf", &k);
        if (tempdesejada == "C")
        {
            printf("%2lf ºC", KC(k));
        }
        if (tempdesejada == "F")
        {
            printf("%2lf F", KF(k));
        }
    }
    if (temp == "F")
    {
        printf("Digite a temperatrura em Fahrenheit: ");
        scanf("%lf", &f);
        if (tempdesejada == "C")
        {
            printf("%2lf ºC", FC(f));
        }
        if (tempdesejada == "K")
        {
            printf("%2lf K", FK(f));
        }
    }

    system("PAUSE");
    return 0;
}