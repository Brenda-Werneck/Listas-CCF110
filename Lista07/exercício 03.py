#Elabore um algoritmo que receba 15 valores e coloque esses valores em um vetor. Mostre em qual posição se encontra o item de maior valor e qual é esse valor e em qual posição se encontra o item de menor valor e qual é esse valor.

vetor = []
maior = -100000000000
menor = 100000000000
v_maior = 0
v_menor = 0

for i in range(15):
    n = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(n)
for i in range(15):
    if vetor[i] > maior:
        maior = vetor[i]
        v_maior = i
    if vetor[i] < menor:
        menor = vetor[i]
        v_menor = i
print(f"O maior é {maior} e se encontra na {v_maior + 1}ª posição. \nE o menor é {menor} e se encontra na {v_menor + 1}ª posição.")
