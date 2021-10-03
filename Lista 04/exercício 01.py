#Uma P.A. (progressão aritmética) fica determinada pela sua razão (r) e pelo primeiro termo(). Escreva um algoritmo que seja capaz de determinar o termo n de uma P.A., dado a razão, o primeiro termo e o n referente ao termo desejado.

r = float(input("Digite a razão: "))
a1 = float(input("Digite o primeiro termo: "))
n = float(input("Digite o termo desejado: "))
an = a1 + (n - 1) * r
print(an)