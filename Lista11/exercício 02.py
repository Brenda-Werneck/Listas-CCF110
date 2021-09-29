from random import randint

qtdade = int(input("Qauntidade de pessoas: "))
nomes, sobrenomes = [], []
arquivo = open("nomeeidade.txt", "w")

for i in range(qtdade):
    nomes.append(input("Nome: "))
    sobrenomes.append(input("Sobrenome: "))
    arquivo.write(f"{nomes[i]} {sobrenomes[i]} {randint(10, 50)}" + ("\n" if i < qtdade - 1 else ""))

arquivo.close()