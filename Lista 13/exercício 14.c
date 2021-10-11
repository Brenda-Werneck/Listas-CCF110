//Faça um programa que leia uma quantidade de horas, minutos e segundos. Crie uma função que calcule e retorne a soma destes valores em segundos.

#include <stdio.h>
#include <stdlib.h>

int totsegundos(int horas, int minutos, int seg)
{
    int total;
    total = ((horas * 60) * 60) + (minutos * 60) + seg;
    return (total);
}

int main()
{
    int h, min, s;

    printf("\nDigite as horas: ");
    scanf("%d", &h);
    printf("\nDigite os minutos: ");
    scanf("%d", &min);
    printf("\nDigite os segundos: ");
    scanf("%d", &s);

    printf("Total em segundos = %d\n", totsegundos(h, min, s));

    system("PAUSE");
    return 0;
}