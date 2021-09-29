#Faça um algoritmo para ler a renda pessoal em salários mínimos de N pessoas. O usuário deve definir esse valor N e posteriormente digitar a renda de cada pessoa. O algoritmo deve mostrar, ao final, o valor referente à média das rendas e também à mediana.

N = int(input("Digite quantas pessoas utilizarão o algoritmo nesse momento: "))
meio = N // 2

vetor = []
soma = 0

for i in range(N):
    n = int(input(f"Digite o número de salários mínimos da {i + 1}ª pessoa: "))
    vetor.append(n)
for i in range(N):
    soma += vetor[i]

media = soma / N

if N % 2 == 0:
    mediana = (vetor[meio - 1] + vetor[meio])/2
else:
    mediana = vetor[meio]
    
print(f"Média = {media}")
print(f"Mediana = {mediana}")
