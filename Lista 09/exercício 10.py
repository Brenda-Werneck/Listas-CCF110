#Crie um algoritmo que entre com valores inteiros para uma matriz M[3x3] e escreva a matriz final, conforme mostrado a seguir: A matriz gira 180º
 
M = [[int(input(f"Valor para({i + 1},{j + 1}): ")) for j in range(3)] for i in range(3)]
M180 = [[M[2 - i][2 - j] for j in range(3)] for i in range(3)]
print("Matriz após girar 180°")
for i in range(3):
    print(M180[i])