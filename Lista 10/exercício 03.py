#Faça um programa que percorre um vetor e imprime na tela o valor mais próximo da média dos valores do vetor. Exemplo:
#vetor = [2.5, 7.5, 10.0, 4.0]
#(média = 6.0)
#Valor mais próximo da média = 7.5

import random

vetor = []
soma = 0
div = random.randint(1, 5)

for i in range(div):
    vetor.append(random.randint(1, 10))
    soma += vetor[i]
media = soma/div
print(media)

diff = 0
index = 0
for i,num in enumerate(vetor):
    if media - num < diff:
        diff = media - num
        index = i
print(vetor[index])