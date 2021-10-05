#Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas. Exemplo:
#Nome = Thor
#Resultado gerado pelo programa:
#T
#TH
#THO
#THOR

n, curr = input(), ""

for x in range(len(n)):
    curr += n[x]
    for _ in range(x - (x * 2)):
        curr += n[x]

    print(curr.upper(), end="\n")