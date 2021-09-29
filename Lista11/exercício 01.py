#Faça um programa que escreve um arquivo com números em ordem decrescente de 200 a 50. Cada número deve estar em uma linha. Dê o nome que quiser para o arquivo.

arquivo1 = open("decrescente.txt", "w")

for i in range(200, 49, -1):
    arquivo1.write(i + "\n")
arquivo1.close()