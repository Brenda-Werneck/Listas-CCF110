#Escreva um algoritmo que receba quinze números do usuário e armazene em um vetor a raiz quadrada de cada número. Caso o valor digitado seja menor que zero, o número –1 deve ser atribuído ao elemento do vetor. Após isso, o algoritmo deve escrever todos os valores armazenados.

vetor = []

for i in range(15):
    n = int(input("Digite um valor para o vetor: "))
    vetor.append(n)

for i in range(15):
    if vetor[i] < 0:
        raiz = -1
    if vetor[i] >= 0:
        raiz = vetor[i] ** (1/2)
    print(raiz)