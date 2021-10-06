//Elabore um algoritmo que crie dois vetores com 10 posições. O usuário digitará os valores do primeiro vetor. O segundo vetor vai receber os valores do primeiro vetor em ordem invertida (o último elemento do primeiro vetor será o primeiro do segundo, o penúltimo elemento do primeiro vetor será o segundo elemento e assim por diante).


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main()
{
    int vetor1[10], vetor2[10];
    for (int i = 0; i < 10; i++)
    {
        printf("Item nº %d:", i + 1);
        scanf("%d", &vetor1[i]);
        vetor2[9-i] = vetor1[i];
    }
    for (int i = 0; i < 10; i++)
    {
        printf("Vetor 2, elemento %d: %d\n", i + 1, vetor2[i]);
    }
    system("PAUSE");
    return 0;
}
