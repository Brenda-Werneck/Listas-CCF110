#Leia 15 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.

vetor = []

for i in range(15):
    n = int(input(f"Digite {i + 1}º valor para o vetor:"))
    vetor.append(n)

for i in range(15):
    cont = 0
    for j in range(2, vetor[i]):
        if vetor[i] % j == 0:
            cont += 1
    if cont == 0:
        if vetor[i] != 1:
            print(f"{i + 1}º do vetor: {vetor[i]} é primo")