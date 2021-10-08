#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever um algoritmo que seja capaz de calcular iterativamente e no fim escrever o tempo necessário para que a população do país A ultrapasse a população do país B.

cont = 0
A = 5000
B = 7000

while A <= B:
    A += 0.03 * A
    B += 0.02 * B
    cont += 1
print(f"Serão necessários {cont} anos")