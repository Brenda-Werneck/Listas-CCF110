#Construa um algoritmo para calcular a média de valores PARES e ÍMPARES, de 50 números que serão digitados pelo usuário. Ao final, o algoritmo deve mostrar estas duas médias. O algoritmo deve mostrar também o maior número PAR digitado e o menor número ÍMPAR digitado. Esses dados devem ser armazenados em um vetor. Além disso, devem ser escritos os valores PARES maiores que a média PAR, bem como os valores ÍMPARES menores que a média ÍMPAR.

soma_par = 0
soma_impar = 0
cont_par = 0
cont_impar = 0
vetor = []
maior = -10000000000
menor = 10000000000

for i in range(50):
    n = int(input(f"Digite {i + 1}º valor para o vetor: "))
    vetor.append(n)

for i in range(50):
    if vetor[i] % 2 == 0:
        soma_par += vetor[i]
        cont_par += 1
        if vetor[i] > maior:
            maior = vetor[i]
    else:
        soma_impar += vetor[i]
        cont_impar += 1
        if vetor[i] < menor:
            menor = vetor[i]

media_par = soma_par / cont_par
media_impar = soma_impar / cont_impar

print(f"A média de valores pares é {media_par}")
print(f"A média de valores ímpares é {media_impar}")
print(f"O maior número par é {maior}")
print(f"O menor número ímpar é {menor}")

for i in range(50):
    if vetor[i] % 2 == 0 and vetor[i] > media_par:
        print(f"O número par {vetor[i]} é maior que a média par = ({media_par})")
    if vetor[i] % 2 != 0 and vetor[i] < media_impar:
        print(f"O número ímpar {vetor[i]} é menor que a média = ({media_impar})")
