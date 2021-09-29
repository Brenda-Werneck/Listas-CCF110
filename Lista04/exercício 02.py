#Uma P.G. (progressão geométrica) fica determinada pela sua razão (q) e pelo primeiro termo (). Escreva um algoritmo que seja capaz de determinar o termo n de uma P.G., dado a razão, o primeiro termo e o n referente ao termo desejado.

q = float(input("Digite a razão: "))
a1 = float(input("Digite o primeiro termo: "))
n = float(input("Digite o termo desejado: "))
an = a1 + 8 (q ** (n - 1))
print(an)