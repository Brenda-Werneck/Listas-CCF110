//Escreva um algoritmo para ler três notas de um aluno. Elabore uma função para calcular e retornar a média aritmética destas notas.

#include <stdio.h>
#include <stdlib.h>

double Media(double n1, double n2, double n3)
{
    return (n1 + n2 + n3) / 3;
}

int main()
{
    int n1, n2, n3;

    printf("Digite a primeira nota: ");
    scanf("%d", &n1);
    printf("Digite a segunda nota: ");
    scanf("%d", &n2);
    printf("Digite a terceira nota: ");
    scanf("%d", &n3);

    printf("Média = %.2lf\n", Media(n1, n2, n3));

    system("PAUSE");
    return 0;
}