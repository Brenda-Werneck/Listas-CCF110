#Dados três valores A, B e C, construa um algoritmo que escreva os valores de forma descendente (do maior para o menor).

A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
C = float(input("Digite o terceiro número: "))
if A > B and B > C:
    print(A, B, C)
if A > C and C > B:
    print(A, C, B)
if B > A and A > C:
    print(B, A, C)
if B > C and C > A:
    print(B, C, A)
if C > A and A > B:
    print(C, A, B)
if C > B and B > A:
    print(C, B, A)
