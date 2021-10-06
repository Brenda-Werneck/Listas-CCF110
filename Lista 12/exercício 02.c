//O custo ao consumidor de um carro novo é a soma do custo de fábrica com o percentual do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo do consumidor.

#include <stdio.h>
#include <stdlib.h>
main()
{
    float custo, custo_fab;
    printf("\nDigite o custo de fábrica: ");
    scanf("%f", &custo_fab);
    custo = custo_fab + (0.28 * custo_fab) + (0.45 * custo_fab);
    printf("\nCusto = R$%f\n", custo);
    system("PAUSE");

    return 0;
}