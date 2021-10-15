#Crie um algoritmo que leia valores para uma matriz M[2x2]. Calcule e escreva o determinante. Para cálculo do determinante de uma matriz de ordem 2, é simplesmente computar a diferença entre os produtos das diagonais principal e secundária, respectivamente.

prod = 1
prod2 = 1
matriz = [[0 for i in range(10)] for j in range(2)]
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
for i in range(2):
    for j in range(2):
        if i == j:
            prod = matriz[i][j] * prod
        if i != j:
            prod2 = matriz[i][j] * prod2
determinante = prod - prod2
print(determinante)