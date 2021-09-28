#Construa um algoritmo que determine se um dado número N (recebido através do teclado) é par ou ímpar.

N = int(input("Digite um número:" ))
if N % 2 == 0:
    print(f"{N} é par")
else:
    print(f"{N} é ímpar")