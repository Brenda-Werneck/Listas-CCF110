#Crie um algoritmo que leia uma matriz A[NxN] (N ≤ 10) e calcule a respectiva matriz transposta At.

N = int(input("Digite um valor: "))
if N <= 10:
    A = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            A[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
    At = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            At[i][j] = A[j][i]
    for i in range(N):
        print(At[i])