#Construa um algoritmo que leia dois valores numéricos e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.

num = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
soma = num + num2
if soma > 10:
    print(soma)
