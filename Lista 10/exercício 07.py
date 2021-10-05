#Em uma universidade são distribuídas 300 senhas para a fila do bandejão, que funciona da seguinte forma: As filas começam a se formar pela manhã. Até às 11h, horário de abertura do restaurante, os alunos podem guardar lugar para no máximo 3 outros colegas, depois disso a fila é congelada. Se a quantidade de pessoas na fila + lugares guardados ultrapassar 300, os extras ficarão sem senha. 
#Escreva um programa que percorre uma lista com as matrículas dos alunos que estão aguardando na fila. Para cada aluno, começando do último, descubra quantos alunos de fato comerão no bandejão (em dias de comida ruim, pode ser que sobrem senhas!). Para tanto, pergunte para quantas pessoas ele está guardando lugar na fila e se ele irá continuar na fila (para esta pergunta ele deverá responder ‘S’ ou ‘N’). Com essa informação, atualize a fila, inserindo a matrícula daqueles que ainda irão chegar e removendo aqueles que vão sair da fila. Imprima a fila final, de acordo com ordem de chegada (se a fila for maior que 300, remova os excedentes antes de imprimir a fila).

f = [input("Matrícula: ") for _ in range(300)]
x = len(f)

while x >= 0:
    if input("S ou N: ").lower() == "n":
        f.pop(len(f) - x - 1)
    p = int(input("Guardando para quantas pessoas: "))
    if p < 4: 
        x -= p
    x -= 1

print(f"Quantidade de pessoas na fila: {len(p)}")