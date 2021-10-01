#Criar um algoritmo que efetue o cálculo da quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo gasto na viagem e a velocidade média. Distância = Tempo * Velocidade. Litros = Distância / 12. O algoritmo deverá apresentar os valores da distância percorrida e a quantidade de litros utilizados na viagem.

tempo = float(input("Digite quanto tempo durou a viagem em horas: "))
velocidade = float(input("Digite a velocidade média do carro em km/h: "))
distancia = tempo * velocidade
litros = distancia / 12
print(f"A quantidade de litros de combustível utilizada durante a viagem foi de {litros}")