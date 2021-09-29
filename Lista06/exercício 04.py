#Escreva um algoritmo que leia um vetor de 25 posições e imprima na tela em qual posição desse vetor se encontra o número N. Esse valor N deve ser lido do teclado. Caso esse valor não esteja no vetor, imprima uma mensagem de erro.

vetor = []
erro = 0

for i in range(25):
    n = int(input("Digite um valor para o vetor: "))
    vetor.append(n)

N = int(input("Digite um número: "))

for i in range(25):
    if vetor[i] == N:
        erro += 1
        print(i)
if erro == 0:
    print("ERRO!")
