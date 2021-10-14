#Elabore um algoritmo que crie dois vetores com 10 posições. O usuário digitará os valores do primeiro vetor. O segundo vetor vai receber os valores do primeiro vetor em ordem invertida (o último elemento do primeiro vetor será o primeiro do segundo, o penúltimo elemento do primeiro vetor será o segundo elemento e assim por diante).

vetor = []

for i in range(10):
    n = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(n)

for i in range(10):
    Y = vetor[::-1]

for j in range(10):
    print("vetor[{}] = {}".format(j + 1, Y[j]))