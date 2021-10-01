#Construa um algoritmo que leia dois números A e B. Em seguida, o algoritmo deve informar se A é maior, menor ou igual a B.

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
if A - B > 0:
    print(f"{A} é maior que {B}")
if A - B < 0:
    print(f"{A} é menor que {B}")
if A - B == 0:
    print(f"{A} é igual a {B}")