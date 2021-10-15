#Crie um algoritmo que entre com valores inteiros para uma matriz M[3x3] e escreva a matriz final, conforme mostrado a seguir: A matriz gira 90º
 
matriz = [[0 for i in range(3)] for j in range(3)]
giro90 = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para o índice ({i + 1}, {j + 1}): "))
for i in range(3):
    for j in range(3):
        if i == 0:
            giro90[j][2] = matriz[i][j]
        if i == 1:
            giro90[j][1] = matriz[i][j]
        if i == 2:
            giro90[j][0] = matriz[i][j]
print("Matriz após girar 90º")
for i in range(3):
    print(giro90[i])