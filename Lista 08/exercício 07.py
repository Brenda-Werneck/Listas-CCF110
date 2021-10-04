#Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva todos os elementos exceto os elementos da diagonal secundária.

matriz = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
for i in range(10):
    for j in range(10):
        if i + j != 9:
            print(matriz[i][j])
