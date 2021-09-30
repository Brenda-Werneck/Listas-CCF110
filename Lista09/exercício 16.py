#Crie um algoritmo que leia uma matriz A[2x2] e calcule a respectiva inversa A-1.

A = [[0 for i in range(2)] for j in range(2)]
for i in range(2):
    for j in range(2):
        A[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
mult = ((A[0][0] * A[1][1]) - (A[0][1] * A[1][0]))
At = [[0 for i in range(2)] for j in range(2)]
try:
    for i in range(2):
        for j in range(2):
            if i == j:
                At[i][i] = A[1-i][1-i] / mult
            else:
                At[i][j] = (-1 * A[i][j]) / mult
    for i in range(2):
        print(At[i])
except:
    print("Impossível calcular a inversa")
