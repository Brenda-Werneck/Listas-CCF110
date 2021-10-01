#Escreva um algoritmo que leia 200 números e escreva quantos são pares e quantos são ímpares.

contpares = 0
contimpares = 0
vetor = []

for i in range(200):
    n = int(input(f"Digite o {i + 1}º número:"))
    vetor.append(n)
for i in range(200):
    if vetor[i] % 2 == 0:
        contpares += 1
    else:
        contimpares += 1
print(f"Pares: {contpares} \nÍmpares: {contimpares}")