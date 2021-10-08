#Construa um algoritmo para encontrar o maior e o menor número de uma série de números positivos fornecidos pelo usuário através do teclado. O dado finalizador é o número –1, e este não deve ser considerado.

n = 0
maior = 0
menor = 10000

while True:
    n = int(input("Digite um número: "))
    if n <= 0:
        break
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f"Maior = {maior} \nMenor = {menor}")