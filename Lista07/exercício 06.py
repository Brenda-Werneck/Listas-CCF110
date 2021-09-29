#Elabore um algoritmo que leia um vetor de tamanho 30 preenchido com o seguinte valor: (i + 7 ∗ i) - (i + 1), sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela.

vetor = []

for i in range(30):
    n = (i + 7 * i) - (i + 1)
    vetor.append(n)

for i in range(30):
    print(vetor[i])
