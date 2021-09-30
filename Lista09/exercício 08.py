#Crie um algoritmo que leia e armazene os elementos de uma matriz inteira M[10x10] e escrevê-la. Troque, na ordem a seguir:
#	A segunda linha pela oitava linha;
#	A quarta coluna pela décima coluna;
#	A diagonal principal pela diagonal secundária.

matriz = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
for i in range(10):
    print(matriz[i])
print("\n")

for i in range(10):
    troca = matriz[1][i]
    matriz[1][i] = matriz[7][i]
    matriz[7][i] = troca
for i in range(10):
    print(matriz[i])
print("\n")

for i in range(10):
    troca = matriz[i][3]
    matriz[i][3] = matriz[i][9]
    matriz[i][9] = troca
for i in range(10):
    print(matriz[i])
print("\n")

for i in range(10):
    troca = matriz[i][i]
    matriz[i][i] = matriz[i][10 - 1 - i]
    matriz[i][10 - 1 - i] = troca
for i in range(10):
    print(matriz[i])
print("\n")
