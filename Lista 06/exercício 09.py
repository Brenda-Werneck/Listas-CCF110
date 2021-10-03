#Elabore um algoritmo que leia os valores e realize a soma de cada um dos elementos de dois vetores de 5 posições e armazene o resultado em um terceiro vetor, que deve ter seus elementos apresentados.

vetor1 = [int(input(f"Digite {x + 1}ª número do vetor 1: ")) for x in range(5)]
vetor2 = [int(input(f"Digite {x + 1}ª número do vetor 2: ")) for x in range(5)]
vet_soma = [vetor1[x] + vetor2[x] for x in range(5)]

for i in range(5):
    print(f"{vetor1[i]} + {vetor2[i]} = {vet_soma[i]}")
