#Elabore um algoritmo no qual haja um vetor de 15 posições e que os valores do vetor sejam informados pelo usuário. Após isso ordene o vetor de forma crescente.

vetor = []

for i in range(15):
    vetor.append(int(input("Digite um valor: ")))

for i in range(15):
    aux = 0
    for j in range(14):
        if vetor[j] > vetor[j+1]:
            aux = vetor[j+1]
            vetor[j+1] = vetor[j]
            vetor[j] = aux

for i in range(15):
    print(vetor[i])