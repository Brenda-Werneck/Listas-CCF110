#Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva o produto dos elementos que estão abaixo da diagonal principal.

produto = 1
matriz = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
for i in range(10):
    for j in range(10):
        if i > j:
            produto = produto * matriz[i][j]
print(produto)