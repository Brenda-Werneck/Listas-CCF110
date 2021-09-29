#Numa corrida há 10 corredores, de número de inscrição de 1 a 10. Faça um algoritmo que leia os valores do tempo na corrida de cada corredor. O programa deve escrever a qualificação e o tempo de corrida, do primeiro ao décimo colocado, identificando o número de inscrição do corredor referente àquela colocação. Suponha que não há tempos iguais. (Dica: Utilize o índice do vetor para indicar o número de inscrição dele. Note que se você ordenar o vetor original vai perder esse número.)

tempo = []
corredor = []

for x in range(10):
    t = float(input(f"Tempo de corrida do {x + 1}ª corredor: "))
    if x == 0 or tempo[len(tempo) - 1] < t:
        tempo.append(t)
        corredor.append(x)
    else:
        for i in range(len(tempo)):
            if t <= tempo[i]:
                tempo.insert(i, t)
                corredor.insert(i, x)
                break
for x in range(10):
    print(f"{x + 1}ª posição corredor {corredor[x] + 1}: tempo = {tempo[x]}")

