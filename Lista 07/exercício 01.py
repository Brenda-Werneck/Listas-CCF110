#Elabore um programa que leia 10 valores e salve-os em um vetor. Depois imprima esses valores e a média desses valores.

soma = 0
vetor = []

for i in range(10):
    n = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(n)

for i in range(10):
    soma += vetor[i]

media = soma / 10

for i in range(10):
    print(f"{i + 1}º valor do vetor: {vetor[i]}")
    
print(f"Média = {media}")