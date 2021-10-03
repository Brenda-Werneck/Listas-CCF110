#Em uma cidade do interior, sabe-se que, de janeiro a abril de 1976 (121 dias), não ocorreu temperatura inferior a 15ºC nem superior a 40ºC. As temperaturas verificadas em cada dia estão disponíveis em uma unidade de entrada de dados. Fazer um algoritmo que calcule e escreva:
#	A menor temperatura ocorrida;
#	A maior temperatura ocorrida;
#	A temperatura média;
#	O número de dias nos quais a temperatura foi inferior à temperatura média.

vetor = []
maior = -15
menor = 40
soma = 0
cont = 0

for i in range(121):
    temp = int(input(f"Digite a temperatura (em ºC) no {i + 1}º dia: "))
    vetor.append(temp)

for i in range(121):
    if vetor[i] > maior and vetor[i] <= 40:
        maior = vetor[i]
    if vetor[i] < menor and vetor[i] >= 15:
        menor = vetor[i]
    soma += vetor[i]

media = soma / 121

for i in range(121):
    if vetor[i] < media:
        cont += 1

print(f"A menor temperatura ocorrida foi {menor}ºC")
print(f"A maior temperatura ocorrida foi {maior}ºC")
print(f"A temperatura média foi {media}ºC")
print(f"A temperatura foi inferior à média durante {cont} dias")
