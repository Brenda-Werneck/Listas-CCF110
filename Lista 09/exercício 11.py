#Crie um algoritmo que entre com valores inteiros para uma matriz M[3x3] e escreva a matriz final, conforme mostrado a seguir: A matriz gira 270º
 
M = [[int(input(f"Valor para({i + 1},{j + 1}): ")) for j in range(3)] for i in range(3)]
M270 = [[M[j][2 - i] for j in range(3)] for i in range(3)]
print("Matriz após girar 180ª")
for i in range(3):
    print(M270[i])