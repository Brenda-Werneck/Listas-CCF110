#Fazer um algoritmo que:
#	Leia o valor de X;
#	Calcule e escreva o valor do seguinte somatório:
#(X^25)/1 + (X^24)/2 + (X^23)/3 + (X^22)/4 + ... + X/25

X = int(input())
cont = 1
soma = 0
for i in range(25, 0, -1):
    if cont % 2 == 1:
        soma += (X ** i) / cont
    else:
        soma -= (X ** i) / cont
    cont += 1
print(soma)
