#Criar um algoritmo que leia 1000 números e escreva o maior e o menor número digitado.

maior = 0
menor = 100
vetor = []

for i in range(1000):
    n = int(input(f"Digite o {i + 1}º número:"))
    vetor.append(n)
for i in range(1000):
    if vetor[i] > maior:
        maior = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]
print(f"Maior = {maior} \nMenor = {menor}")
