#Fazer um algoritmo para calcular e escrever a seguinte soma:
#S = (37 x 38)/1 + (36 x 37)/2 + (35 x 36)/3 + ... + (1 x 2)/37

soma = 0
cont = 1

for i in range(37, 0, -1):
    soma += i * (i + 1) / cont
    cont += 1
print(f"Soma  = {soma}")