#Crie um algoritmo que possa armazenar as alturas de dez atletas de cinco delegações que participarão dos jogos de verão. Armazene esses dados em uma matriz. Depois, escreva a maior altura de cada delegação.

matriz = [[0 for i in range(10)] for j in range(5)]

for i in range(5):
    for j in range(10):
        matriz[i][j] = int(input(f"Digite a altura do {j + 1}º atleta para a delegação {i +1} (em cm): "))
for i in range(5):
    maior = 0
    for j in range(10):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(f"A maior altura da delegação {i + 1} é: {maior}cm")