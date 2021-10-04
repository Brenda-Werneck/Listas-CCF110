#Entre com valores para duas matrizes inteiras de ordem cinco. Gere e escreva a matriz diferença.

A = [[0 for i in range(5)] for j in range(5)]
B = [[0 for i in range(5)] for j in range(5)]
diferença = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        A[i][j] = int(input(f"Digite o valor para o índice ({i},{j}) da matriz A: "))
for i in range(5):
    for j in range(5):
        B[i][j] = int(input(f"Digite o valor para o índice ({i},{j}) da matriz B: "))
for i in range(5):
    for j in range(5):
        diferença[i][j] = A[i][j] - B[i][j]
for i in range(5):
    for j in range(5):
        print(diferença[i][j])
