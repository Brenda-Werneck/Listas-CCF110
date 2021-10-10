//Escreva um algoritmo que leia 5 notas de 10 alunos. Elabore uma função que some as notas de cada aluno e retorne se o aluno foi aprovado ou reprovado.
//Obs.: Se a média das somas das notas for menor que 60, o aluno estará reprovado.

#include <stdio.h>
#include <stdlib.h>

double Media(double n1, double n2, double n3, double n4, double n5)
{
    return (n1 + n2 + n3 + n4 + n5) / 5;
}

int main()
{
    int i;
    for (i = 0; i < 10; i++)
    {
        int n1, n2, n3, n4, n5;

        printf("Digite a primeira nota: ");
        scanf("%d", &n1);
        printf("Digite a segunda nota: ");
        scanf("%d", &n2);
        printf("Digite a terceira nota: ");
        scanf("%d", &n3);
        printf("Digite a quarta nota: ");
        scanf("%d", &n4);
        printf("Digite a quinta nota: ");
        scanf("%d", &n5);

        if (Media(n1, n2, n3, n4, n5) < 60)
        {
            printf("Reprovado\n");
        }
        else
        {
            printf("Aprovado\n");
        }
    }

    system("PAUSE");
    return 0;
}
