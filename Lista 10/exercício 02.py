#Faça um programa que percorre duas listas e intercala os elementos de ambas, formando uma terceira lista. A terceira lista deve começar pelo primeiro elemento da lista menor. 

#Exemplo:
#lista1 = [1, 2, 3, 4]
#lista2 = [10, 20, 30, 40, 50, 60]
#lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]

import random

lista1 = []
lista2 = []
lista3 = []
cont1 = 0
cont2 = 0

for i in range(random.randint(1, 6)):
    lista1.append(random.randint(1, 6))
for i in range(random.randint(1, 6)):
    lista2.append(random.randint(1, 6))

if len(lista1) < len(lista2):
    while True:
        if cont1 < len(lista1):
            lista3.append(lista1[cont1])
        if cont2 < len(lista2):
            lista3.append(lista2[cont2])
        else:
            break
        cont1 += 1
        cont2 += 1
else:
    while True:
        if cont1 < len(lista1):
            lista3.append(lista2[cont2])
        cont1 += 1
        cont2 += 1

for i in range(len(lista3)):
    print(lista3[i])