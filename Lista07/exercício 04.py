#Escreva um algoritmo que leia um vetor de 30 posições e depois altere as posições de índice par para o valor 0 e imprima o vetor atualizado.

vetor = []

for i in range(30):
    n = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(n)

for i in range(30):
    if i % 2 == 0:
        vetor[i] = 0

for i in range(30):
    print(vetor[i])
