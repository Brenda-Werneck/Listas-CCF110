#Escrever um algoritmo que leia 20 valores para uma variável n e, para cada um deles, calcule a tabuada de 1 até n. Mostre a tabuada na forma: 
#1 x n = n 
#2 x n = 2n
#3 x n = 3n
#....... 
#n x n = n^2

prod = 1
vetor = []
vetor2 = []

for i in range(20):
    n = int(input(f"Digite o {i + 1} º número: "))
    vetor.append(n)

for i in range(20):
    for j in range(n):
        prod = 
