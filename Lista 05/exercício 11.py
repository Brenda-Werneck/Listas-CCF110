#Escreva um algoritmo que calcule o resto da divisão de A por B (número inteiros e positivos), ou seja, A mod B, através de subtrações sucessivas. Esses dois valores são passados pelo usuário através do teclado.

A = int(input("Digite um número inteiro: "))
B = int(input("Digite outro número inteiro: "))

while A >= B:
    A = int(A - B)
print(f"Resto da divisão = {A}")