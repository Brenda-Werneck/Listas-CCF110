#Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva a soma dos elementos que estão acima da diagonal principal. 

matriz = [[0 for i in range(10)] for j in range(10)]
soma = 0

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i},{j}): "))
for i in range(10):
    for j in range(10):
        if j > i:
            soma += matriz[i][j]
print(f"Soma = {soma}")