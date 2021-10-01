#Escreva um algoritmo que leia um número e informe se ele é divisível, individualmente, por 3 ou por 7.

num = int(input("Digite um número: "))
if num % 3 == 0: 
    print(f"{num} é múltiplo de 3")
if num % 7 == 0:
    print(f"{num} é múltiplo de 7")
else:
    print(f"{num} não é múltiplo nem de 3, nem de 7")