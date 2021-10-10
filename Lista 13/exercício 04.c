//Elabore um algoritmo que inverta um número de 3 dígitos. O algoritmo deve utilizar uma função que receba um número e o retorne invertido.
//Exemplo:
//Número digitado: 154
//Número invertido: 451

#include <stdio.h>

int inver(int n)
{
    int u, d, c, mun;
    u = (n % 100) % 10;
    d = (n % 100) / 10;
    c = (n - n % 100) / 100;
    mun = u * 100+ d * 10 + c;
    return(mun);
}
int main()
{
    int num,res;
    printf("Digite um numero: ");
    scanf("%d", &num);
    printf("Numero digitado: %d\n", num);
    printf("Numero invertido: %d\n", inver(num));
    return(0);
}