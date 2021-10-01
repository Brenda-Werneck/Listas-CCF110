#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.

anos = int(input("Digite a sua idade em anos: "))
meses = int(input("Digite quantos meses completos se passaram desde o seu último aniversário:"))
dias = int(input("Digite quantos dias se passaram desde que o último mês completo fechou:"))
dias += (anos * 365) + (meses * 30)
print(f"Você já viveu {dias} dias")
