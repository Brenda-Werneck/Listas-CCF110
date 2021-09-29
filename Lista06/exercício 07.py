#Escreva um algoritmo que armazene em um vetor o quadrado dos números ímpares no intervalo fechado de 1 a 20. Após isso, o algoritmo deve escrever todos os valores armazenados.

vetor = []

for i in range(21):
    quadrado = i ** 2
    vetor.append(quadrado)
    
for i in range(21):
    if i % 2 == 1:
        print(vetor[i])
