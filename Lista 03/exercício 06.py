#Faça um algoritmo que mostre os números de x até z.

x = int(input("Digite o primeiro valor para o intervalo: "))
z = int(input("Digite o segundo valor para o intervalo: "))
for i in range(x, (z + 1)):
    print(i)