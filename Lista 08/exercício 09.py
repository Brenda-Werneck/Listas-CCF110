#Entre com valores para uma matriz A[3x4]. Gere e escreva uma matriz B que é o triplo da matriz A.

A = [[0 for i in range(4)] for j in range(3)]
B = [[0 for i in range(4)] for j in range(3)]
for i in range(3):
    for j in range(4):
        A[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
for i in range(3):
    for j in range(4):
        B[i][j] = A[i][j] * 3
for i in range(3):
    for j in range(4):
        print(B[i][j])