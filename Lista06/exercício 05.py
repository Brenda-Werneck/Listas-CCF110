#Escreva um algoritmo que leia a nota de 15 alunos de uma turma, armazene esses dados em um vetor e depois calcule a média geral das notas e imprima na tela.

vetor = []
soma = 0

for i in range(15):
    n = int(input("Digite um valor para o vetor: "))
    vetor.append(n)

for i in range(15):
    soma += vetor[i]
    
media = soma / 15
print(f"Média = {media}")
