//Crie um algoritmo que utilize uma função que define se um número é primo ou não, a função retornará 1 ou 0 para informar tal resultado.

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int teste(int n)
{
    return n;
}

void PRIMO(int n)
{
    int i, cont;
    int primo = teste(n);
    cont = 0;
    for (i = 2; i < primo; i++)
    {
        if (primo % i == 0)
        {
            cont += 1;
        }
        else
        {
            cont = cont;
        }
    }
    if (cont != 0)
    {
        printf("0\n");
    }
    else
    {
        printf("1\n");
    }
}

int main()
{
    int n;
    printf("\nDigite um número: ");
    scanf("%d", &n);
    if (teste(n) == 1)
    {
        printf("%d é primo\n", n);
    }
    else if(teste(n) == 0)
    {
        printf("%d não é primo\n", n);
    }


    system("PAUSE");
    return 0;
}