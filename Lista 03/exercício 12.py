#A série de Fibonacci é formada pela seguinte sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 … etc. Escreva um algoritmo que gere e imprima a série de Fibonacci até o vigésimo termo.

vetor = []

for i in range(20):
    num = 1
    vetor.append(num)
for i in range(20):
    if i == 0 or i == 1:
        vetor[i] = vetor[i]
    else:
        vetor[i] = vetor[i - 1] + vetor[i -2]
print("Série de Fibonacci:")
for i in range(20):
    print(f"{vetor[i]}")