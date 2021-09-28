#Escreva um algoritmo para determinar se um número A é divisível por um outro número B. Esses valores devem ser fornecidos pelo usuário.

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
if A % B == 0:
    print(f"{A} é divisível por {B}")
else:
    print(f"{A} não é divisível por {B}")