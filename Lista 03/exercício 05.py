#Escreva um algoritmo que receba 100 números do usuário e escreva a metade de cada número.

vetor = []
vetor2 = []
for i in range(100):
    n = int(input(f"Digite o {i + 1}º número:"))
    vetor.append(n)
for i in range(100):
    metade = vetor[i] / 2
    vetor2.append(metade)
for i in range(100):
    print(vetor2[i])