#Escreva um algoritmo que receba um número e escreva uma das mensagens: “é múltiplo de 3” ou “não é múltiplo de 3”.

N = int(input("Digite um número: "))
if N % 3 == 0:
    print(f"{N} é multíplo de 3")
else:
    print(f"{N} não é multíplo de 3")