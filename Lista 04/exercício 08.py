#Seja uma sequência A,B,C, ... determinando um Progressão Geométrica (P.G.), o termo médio (B) de uma P.G. é determinado pela média geométrica de seus termos, sucessor (C) e antecessor (B). Com base neste enunciado construa um algoritmo que calcule o termo médio (B) através de A, C.

A = float(input("Digite o termo antecessor da P.G: "))
C = float(input("Digite o termo sucessor da P.G: "))
B = (A * C) ** (1/2)
print(f"Termo médio da P.G = {B}")