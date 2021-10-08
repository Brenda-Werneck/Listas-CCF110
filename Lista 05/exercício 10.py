#Escreva um algoritmo que realize o produto de A (número real) por B (número inteiro), ou seja, A * B, através de adições (somas). Esses dois valores são passados pelo usuário através do teclado.

A = float(input("Digite o número real: "))
B = int(input("Digite o número inteiro: "))
soma = 0

for i in range(B):
    soma += A
print(f"Produto de {A} x {B} = {soma}")