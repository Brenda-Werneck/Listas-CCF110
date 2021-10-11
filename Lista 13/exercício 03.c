//Crie um algoritmo que utilize uma função que define se um número é primo ou não, a função retornará 1 ou 0 para informar tal resultado.

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int PRIMO(int n)
{
    int i, cont, zoum;;
    cont = 0;
    for (i = 2; i < n; i++)
    {
        if (n % i == 0)
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
        zoum = 0;
        return zoum;
    }
    else if (cont == 0)
    {
        zoum = 1;
        return zoum;
    }
}

int main()
{
    int n;
    printf("\nDigite um número: ");
    scanf("%d", &n);
    PRIMO(n);
    if (PRIMO(n) != 0)
    {
        printf("%d é primo\n", n);
    }
    else if(PRIMO(n) == 0)
    {
        printf("%d não é primo\n", n);
    }


    system("PAUSE");
    return 0;
}