#Escreva um algoritmo que leia um peso na Terra e o número de um planeta e escreva o valor do seu peso neste planeta. A relação de planetas é dada a seguir juntamente com o valor das gravidades relativas à Terra:
##          Gravidade Relativa  Planeta
#1	         0,37               Mercúrio
#2	         0,88	            Vênus
#3	         0,38	            Marte
#4	         2,64	            Júpiter
#5	         1,15	            Saturno
#6	         1,17	            Urano

peso = float(input("Digite seu peso em kg:"))
planetas = int(input("Digite o número do planeta escolhido: "))
if planetas == 1: 
    peso = peso * 0.37
    print(f"Peso em Mercúrio = {peso}")
if planetas == 2:
    peso = peso * 0.88
    print(f"Peso em Vênus = {peso}")
if planetas == 3:
    peso = peso * 0.38
    print(f"Peso em Marte = {peso}")
if planetas == 4:
    peso = peso * 2.64
    print(f"Peso em Júpiter = {peso}")
if planetas == 5:
    peso = peso * 1.15
    print(f"Peso em Saturno = {peso}")
if planetas == 6:
    peso = peso * 1.17
    print(f"Peso em Urano = {peso}")
