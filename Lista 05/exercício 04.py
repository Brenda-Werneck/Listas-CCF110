#Criar um algoritmo que escreva todos os números de 1 até 100, inclusive, e a soma do quadrado desses números.

somaquad = 0

for i in range(101):
    somaquad += ((i + 1) ** 2)
    print(i + 1)
print(somaquad)