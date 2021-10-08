#Dois ciclistas A e B estão andando em uma pista de ciclismo com 2 km de comprimento com velocidades de 10 m/s e 15 m/s, respectivamente. Escreva um algoritmo que determine iterativamente o tempo que levará para que esses dois ciclistas A e B se encontrem em um mesmo ponto, sabendo que eles partiram de um mesmo ponto inicial, porém em sentido contrário. O algoritmo também deve calcular o deslocamento (a distância) que cada um percorreu.

seg = 0
A = 0
B = 2000

while A != B:
    seg += 1
    A += 10
    B -= 15
print(f"{seg} segundos")
print(f"Deslocamento de A: {seg*10}m \nDeslocamento de B: {seg*15}m")