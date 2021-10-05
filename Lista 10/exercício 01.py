#Faça um programa que simule um lançamento de dados. Lance o dado 10 vezes e armazene os resultados em um vetor. Depois, monte um outro vetor contendo quantas vezes cada valor foi obtido. Imprima os dois vetores. Use uma função para gerar números aleatórios, simulando os lançamentos dos dados. 

#Exemplo de uma possível saída:
# [3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
# [1, 0, 3, 1, 4, 1]

import random

vetor = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor.append(random.randint(1, 6))
for i in range(10):
    vetor2.append(vetor.count(vetor[i]))
for i in range(10):
    print(vetor[i], end="")

print()

for i in vetor2:
  if i not in vetor3:
    vetor3.append(i)

for i in range(len(vetor3)):
    print(vetor3[i], end="")