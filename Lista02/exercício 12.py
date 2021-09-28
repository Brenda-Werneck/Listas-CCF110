#Escreva um algoritmo que leia um número e escreva a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.


num = int(input("Digite um número: "))
if num >= 0:
    raiz = (num) ** (1/2)
    print(f"Raiz quadrada é {raiz}")
if num < 0:
    quad = num ** 2
    print(f"{num} ao quadrado é {quad}")    
