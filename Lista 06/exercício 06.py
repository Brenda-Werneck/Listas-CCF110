#. Escreva um algoritmo que leia um vetor de tamanho n (informado pelo usuário) e escreva a soma de todos os elementos de índice par.

n = int(input("Digite o tamanho do seu vetor: "))
vetor = []
soma = 0

for i in range(n):
    n = int(input("Digite um valor para o vetor: "))
    vetor.append(n)

for i in range(n):
    if i % 2 == 0:
        soma += vetor[i]
        
print(f"Soma = {soma}")