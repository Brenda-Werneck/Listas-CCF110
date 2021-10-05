#Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas. Exemplo: Nome = Thor. Resultado gerado pelo programa: ROHT

n = input("Digite o nome do usuário: ")
for i in range(len(n)):
    print(n[len(n) - i - 1].capitalize(), end="")