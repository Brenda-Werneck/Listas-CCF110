#Escreva um algoritmo que leia do teclado dois números: divisor e dividendo. O algoritmo deve apresentar o quociente e o resto da divisão. Caso o valor do divisor seja zero, o algoritmo deve escrever “Divisão não permitida” e encerrar.

divisor = int(input("Digite o divvisor: "))
dividendo = int(input("Digite o dividendo: "))
quociente = dividendo // divisor
resto = dividendo % divisor
if resto == 0:
    print("Divisão não permitida")
else:
    print(f"Quociente da divisão de {dividendo} por {divisor} é quociente \nO resto dessa divisão é {resto}")