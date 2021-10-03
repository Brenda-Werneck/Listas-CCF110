#Escreva um algoritmo que receba a altura de 10 atletas. Esse algoritmo deve escrever a altura daqueles atletas que têm altura maior que a média.

vetor = []
soma = 0

for i in range(10):
    altura = int(input("Digite a altura do atleta em cm: "))
    vetor.append(altura)

for i in range(10):
    soma += vetor[i]
media = soma/10

for i in range(10):
    if vetor[i] > media:
        print(vetor[i])
