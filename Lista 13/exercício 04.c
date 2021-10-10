//Elabore um algoritmo que inverta um número de 3 dígitos. O algoritmo deve utilizar uma função que receba um número e o retorne invertido.
//Exemplo:
//Número digitado: 154
//Número invertido: 451

#include <stdio.h>
#include <stdlib.h>

int inversao(int n)
{
    int rev, resto;
    rev = 0;

    while (n!= 0)
    {
        resto = n % 10;
        rev = rev * 10 + resto;
        n /= 10;
    }
    return rev;
}

int main()
{
    int n;
    printf("Digite um número: ");
    scanf("%d", &n);
    printf("Número invertido = %d\n", inversao(n));

    system("PAUSE");
    return 0;
}