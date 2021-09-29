#Dado um conjunto de 100 valores numéricos disponíveis num meio de entrada qualquer, fazer um algoritmo para armazená-los em um vetor B, e calcular e escrever o valor do somatório dado a seguir:
 
vetor = []
S = 0

for i in range(100):
    b = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(b)

for i in range(50):
    aux = 100
    S += ((vetor[i] - vetor[aux - 1]) ** 3)
print(f"S = {S}")
