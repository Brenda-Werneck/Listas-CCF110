#Faça um algoritmo que leia um valor N (N ≤ 20) e os N valores de um vetor. Ordene os valores recebidos em forma crescente e decrescente e escreva os vetores ordenados.

N = int(input("Digite um valor: "))
A = []

if N <= 20:
    for i in range(N):
        num = int(input(f"Digite o {i + 1}º número do vetor: "))
        A.append(num)

    for i in range(N):
        aux = 0
        for j in range(N - 1):
            if A[j] > A[j + 1]:
                aux = A[j]
                A[j] = A[j + 1]
                A[j + 1] = aux
    for i in range(N):
        print(A[i])

    for i in range(N):
        aux = 0
        for j in range(N - 1):
            if A[j] < A[j + 1]:
                aux = A[j]
                A[j] = A[j + 1]
                A[j + 1] = aux
    for i in range(N):
        print(A[i])