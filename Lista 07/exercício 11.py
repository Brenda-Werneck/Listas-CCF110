#Fazer um algoritmo que:
#a.	Leia o valor inteiro de n (n ≤ 1000) e os n valores de um vetor A de valores numéricos, ordenados de forma crescente;
#b.	Determine e escreva, para cada número que se repete no conjunto, a quantidade de vezes em que ele aparece repetido;
#c.	Elimine os elementos repetidos, formando um novo conjunto;
#d.	Escreva o conjunto obtido.

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

for i in range(n):
    for j in range(i + 1, n):
        if A[j] == A[i]:
            for k in range(j, n - 1):
                A[k] = A[k + 1]
            n -= 1
        else:
            j += 1

for i in range(n):
    print(A[i])