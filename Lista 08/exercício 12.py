#Leia uma matriz 4x5 de inteiros, calcule e escreva a soma de todos os seus elementos.

matriz = [[0 for i in range(4)] for j in range(5)]
soma = 0

for i in range(5):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
for i in range(5):
    for j in range(4):
        soma += matriz[i][j]
print(f"Soma = {soma}")