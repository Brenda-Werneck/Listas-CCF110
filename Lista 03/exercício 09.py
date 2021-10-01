#Construa um algoritmo para calcular a média de um conjunto de valores inteiros e positivos, fornecidos pelo usuário através do teclado. O dado que finaliza é o número –1, e este não deve ser considerado.

soma = 0
cont = 0
n = 0

while n != -1:
    n = int(input("Digite um número: "))
    if n != -1:
        soma += n
        cont += 1
media = soma / cont
print(f"Média = {media}")


