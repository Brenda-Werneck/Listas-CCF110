#Escreva um algoritmo que receba dez números do usuário e armazene em um vetor o quadrado de cada número. Após isso, o algoritmo deve escrever todos os valores armazenados.

vetor = []

for i in range(10):
    n = int(input("Digite um valor para o vetor: "))
    vetor.append(n)

for i in range(10):
    quadrado = vetor[i] ** 2
    print(quadrado)