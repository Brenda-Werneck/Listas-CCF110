//Crie uma função que leia uma medida em metros e converta-a para pés e polegadas, sabendo que 1 pé = 12 polegadas e 1 metro = 39.37 polegadas.

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double polegadas(double m)
{
    return m * 39.37;
}

double pes(double polegadas)
{
    return polegadas / 12;
}

int main()
{
    double metro;
    printf("Digite os metros: ");
    scanf("%lf", metro);
    printf("\nPolegadas = %lf", polegadas(metro));
    printf("\nPés = %lf\n", pes(polegadas(metro)));
    system("PAUSE");
    return 0;
}