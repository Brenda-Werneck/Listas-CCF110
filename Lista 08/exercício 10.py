#Entre com valores inteiros para uma matriz A[4x4] e para uma matriz B[4x4]. Gere e escreva a SOMA (A + B).

A = [[0 for i in range(4)] for j in range(4)]
B = [[0 for i in range(4)] for j in range(4)]
soma = 0

for i in range(4):
    for j in range(4):
        A[i][j] = int(input(f"Digite o valor para o índice ({i},{j}) da matriz A: "))
for i in range(4):
    for j in range(4):
        B[i][j] = int(input(f"Digite o valor para o índice ({i},{j}) da matriz B: "))
for i in range(4):
    for j in range(4):
        soma += A[i][j] + B[i][j]
print(f"Soma = {soma}")

