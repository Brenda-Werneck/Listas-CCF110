#Elabore um algoritmo que leia um vetor de 20 posições. Depois imprima qual é o maior e o menor valor presente no vetor.

vetor = []
maior = -10000000000
menor = 10000000000

for i in range(20):
    n = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(n)

for i in range(20):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print(f"O maior é {maior} e o menor é {menor}")
