#Considere que o número de uma placa de veículo é composto por quatro algarismos. Construa um algoritmo que leia este número e apresente o algarismo correspondente à casa das dezenas.

placa = int(input("Digite um número: "))
dezenas = (placa % 100) // 10
print(dezenas)