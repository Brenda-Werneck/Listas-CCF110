#Implementar um algoritmo para calcular o sen(X). O valor de X deverá ser digitado em graus. O valor do seno de X será calculado pela soma dos 15 primeiros termos da série a seguir (Para que seja calculado corretamente, é necessário que se transforme o valor de X lido em graus para radianos):
 
#sen(x) = x - (x^3)/3! + (x^5)/5! - (x^7)/7! + (x^9)/9! - (x^11)/11! + ...

import math

senx = 0
divisor = 1
x = int(input("Digite o ângulo que deseja calcular o seno: "))
xrad = x * (3.14159 / 180)

for i in range(1, 30, 2):
    for j in range(1, i):
        divisor = divisor * j
    if i == 3 or i == 7 or i == 11 or i == 15 or i == 19 or i == 23 or i == 27:
        senx -= ((xrad ** i)/divisor)
    elif i == 1 or i == 5 or i == 9 or i == 13 or i == 17 or i == 21 or i == 25 or i == 29:
        senx += ((xrad ** i)/divisor)
print(f"Seno de {x}º = {senx}")