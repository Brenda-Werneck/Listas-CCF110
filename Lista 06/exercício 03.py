#Escreva um algoritmo que leia um vetor de 20 posições e mostre-o. Em seguida, troque o primeiro elemento com o último, o segundo com o penúltimo, o terceiro com o antepenúltimo, e assim sucessivamente. Mostre o novo vetor depois da troca.

N = []

for i in range(20):
    x = int(input())
    N.append(x)

for i in range(20):
    print(N[i])

Y = N[::-1]

for j in range(20):
    print("N[{}] = {}".format(j,Y[j]))
