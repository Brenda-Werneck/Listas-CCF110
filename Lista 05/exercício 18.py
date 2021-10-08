#Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 3 centímetros por ano. Construir um algoritmo que calcule iterativamente e escreva quantos anos serão necessários para que Juca seja maior que Chico.

cont = 0
chico = 150
juca = 110

while juca <= chico:
    chico += 2
    juca += 3
    cont += 1
print(f"Serão necessários {cont} anos")