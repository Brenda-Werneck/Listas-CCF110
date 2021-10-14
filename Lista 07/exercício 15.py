#Fazer algoritmo que:
#   a.	Leia o valor inteiro de n (n ≤ 1000) e os n valores de vetor de valores numéricos;
#   b.	Ordenar o vetor e escrevê-lo ordenado.
#   c.	Determine e escreva, para cada número que se repete no conjunto, a quantidade de vezes em que ele aparece repetido;

n = int(input("Digite um valor: "))
if n <= 1000:
    A = []
    for i in range(n):
        num = int(input(f"Digite o {i +1}º valor do vetor: "))
        A.append(num)
else:
    print("Valor inválido")

for i in range(n):
    aux = 0
    for j in range(n - 1):
        if A[j] > A[j + 1]:
            aux = A[j]
            A[j] = A[j + 1]
            A[j + 1] = aux

for i in range(n):
    repete = 0
    for j in range(n):
        if A[i] == A[j]:
            repete += 1
            if repete == 2:
                print(f"O Número {A[i]} aparece {repete} vezes")