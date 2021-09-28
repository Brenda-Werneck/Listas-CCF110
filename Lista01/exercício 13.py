#Escreva um algoritmo que leia do teclado dois números: divisor e dividendo. O algoritmo deve apresentar o quociente e o resto da divisão. Caso o valor do divisor seja zero, o algoritmo deve escrever “Divisão não permitida” e encerrar.

divisor = int(input("Digite o primeiro número: "))
dividendo = int(input("Digite o segundo número: "))
if divisor != 0:
    quociente = dividendo // divisor
    resto = dividendo % divisor
    print(f"Quociente da divisão de {dividendo} por {divisor} é {quociente} \nO resto dessa divisão é {resto}")
else:
    print("Divisão não permitida")