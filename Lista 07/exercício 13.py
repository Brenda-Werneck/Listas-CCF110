#Fazer um algoritmo que:
#   a.	Leia um vetor A com 30 valores numéricos distintos;
#   b.	Leia outro vetor B com 30 valores numéricos;
#   c.	Leia o valor de uma variável X;
#   d.	Verifique qual o elemento de A que é igual a X;
#   e.	Escreva o elemento de B de posição correspondente à do elemento de A igual a X.

A = []
B = []

for i in range(10):
    N = int(input(f"Digite o {i + 1}º valor do vetor A. \n(apenas valores distintos):"))
    A.append(N)

for i in range(10):
    M = int(input(f"Digite o {i + 1}º valor do vetor B: "))
    B.append(M)

x = int(input("Digite uma variável: "))
aux = 0

for i in range(10):
    if A[i] == x:
        aux = i

print(f"O {aux + 1}º elemento do vetor B é: {B[aux]}")