#Crie um algoritmo que leia uma matriz 7x5 e multiplique todos os valores ímpares dessa matriz por 2. Imprima a nova matriz.

matriz = [[0 for i in range(5)] for j in range(7)]
matriz2 = [[0 for i in range(5)] for j in range(7)]

for i in range(7):
    for j in range(5):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
for i in range(7):
    for j in range(5):
        if matriz[i][j] % 2 != 0:
            matriz2[i][j] = matriz[i][j] * 2
        else:
            matriz2[i][j] = matriz[i][j]
for i in range(7):
    for j in range(5):
        print(matriz2[i][j])