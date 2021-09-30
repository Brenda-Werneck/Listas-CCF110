#Crie um algoritmo que leia uma matriz A[NxN] (N ≤ 10) e verifique (informe) se tal matriz é ou não simétrica (At = A).

N = int(input("Digite um valor: "))
A = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
check = 0
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            check += 1
if check == 0:
    print("A matriz é simétrica")
else:
    print("A matriz não é simétrica")
