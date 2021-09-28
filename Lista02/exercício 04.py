#Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

dias = int(input("Digite a sua idade em dias: "))
anos = dias // 365
resto = dias % 365
meses = resto // 30
dias = resto % 30
print(f"Você viveu {anos} anos, {meses} meses e {dias} dias")
