#Crie um algoritmo que permita ler 1 nota de cada um de 10 alunos de uma turma e os respectivos nomes, identifique qual é a maior e a menor nota, mostre os respectivos nomes dos alunos que as obtiveram.

turma = []
vetor = []
maior_nota = 0
menor_nota = 0
nome_maior = ""
nome_menor = ""

for n in range(10):
    vetor.append(str(input("Nome: ")))
    vetor.append(float(input("Nota: ")))
    turma.append(vetor[:])
    vetor.clear()
    if n == 0:
        maior_nota = menor_nota = turma[n][1]
    if maior_nota < turma[n][1]:
        maior_nota = turma[n][1]
    if menor_nota > turma[n][1]:
        menor_nota = turma[n][1]

for c in range(10):
    if maior_nota == turma[c][1]:
        print(f"{turma[c][0]}", end=",")
print(f"Tirou a maior nota que é: {maior_nota}")

for c in range(10):
    if menor_nota == turma[c][1]:
        print(f"{turma[c][0]}", end=",")
print(f"Tirou a menor nota que é: {menor_nota}")