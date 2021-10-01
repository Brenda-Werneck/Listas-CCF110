#Escreva um algoritmo para determinar se um dado número N (recebido através do teclado) é positivo, negativo ou nulo.

N = int(input("Digite um número: "))
if N > 0:
    print(f"{N} é positivo")
if N < 0:
    print(f"{N} é negativo")
else:
    print(f"{N} é nulo")