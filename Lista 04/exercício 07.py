#Seja uma sequência A,B,C, ... determinando um Progressão Aritmética (P.A.), o termo médio (B) de uma P.A. é determinado pela média aritmética de seus termos, sucessor (C) e antecessor (A). Com base neste enunciado construa um algoritmo que calcule o termo médio (B) através de A, C.

A = float(input("Digite o termo antecessor da P.A: "))
C = float(input("Digite o termo sucessor da P.A: "))
B = (A + C) / 2
print(f"Termo médio da P.A = {B}")