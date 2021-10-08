#Criar um algoritmo que leia um número (NUM) e então escreva os múltiplos de 3 e 5, ao mesmo tempo, no intervalo fechado de 1 a NUM.

NUM = int(input("Digite o fim do intervalo: "))

for i in range(NUM + 1):
    if (i + 1) % 15:
        print(i + 1)