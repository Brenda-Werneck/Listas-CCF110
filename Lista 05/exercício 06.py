#Escreva um algoritmo que receba 15 números e escreva quantos números maiores que 30 foram digitados.

cont = 0
vetor = []
for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)
for i in range(15):
    if vetor[i] > 30:
        cont += 1
print(cont)