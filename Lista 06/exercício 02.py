#Elabore um algoritmo que preencha um vetor de 10 elementos com valores informados pelo usuário. Em seguida, peça ao usuário para que digite um número e o compare com os valores no vetor, escrevendo os valores menores que o número digitado pelo usuário.

vetor = []

for i in range(10):
    n = int(input("Digite um valor para o vetor:"))
    vetor.append(n)

num = int(input("Digite um número:"))

for i in range(10):
    if vetor[i] < num:
        print (vetor[i])
