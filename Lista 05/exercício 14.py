#A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores, ou seja:
# + para i ímpar
# - para i par
#Criar um algoritmo que escreva os N primeiros termos da série de FETUCCINE, sabendo-se que para existir esta série serão necessários pelo menos três termos.

A1 = int(input("Digite o primeiro termo: "))
A2 = int(input("Digite o segundo termo: "))
N = int(input("Digite o número de termos: "))

if N < 3:
    print('Número de termos insuficiente para formar uma sequência.')
    exit()

for i in range(N):
    i += 3
    if i % 2 == 0:
        A3 = A2 - A1
    else:
        A3 = A2 + A1
    print(A1, end=' ')
    A1 = A2
    A2 = A3