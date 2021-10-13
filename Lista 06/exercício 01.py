#Elabore um algoritmo que leia um vetor de 30 posições e uma variável a. Em seguida, mostre o produto da variável por cada item do vetor. Mostre também se o produto gerado entre os termos é par ou ímpar.

vetor = []

for i in range(30):
    n = int(input("Digite um valor para o vetor:"))
    vetor.append(n)

a = int(input("Digite um número: "))

for i in range(30):
    prod = vetor[i] * a
    if prod % 2 == 0:
        print(f"Produto = {prod}  \né par")
    else:
        print(f"Produto = {prod} \né ímpar")