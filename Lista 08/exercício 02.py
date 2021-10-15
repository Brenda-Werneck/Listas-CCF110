#Crie um algoritmo que leia uma matriz 7x7 e um valor N e diga em qual posição da matriz, linha e coluna, esse valor N se encontra. Caso esse valor não esteja na matriz, imprima uma mensagem de erro.

matriz = [[0 for i in range(7)] for j in range(7)]

for i in range(7):
    for j in range(7):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
N = int(input("Digite um valor: "))
for i in range(7):
    for j in range(7):
        if matriz[i][j] == N:
            print(f"linha: {i}, coluna: {j}")
        else:
            print("ERRO")