#Fazer um algoritmo para calcular e escrever a seguinte soma:
#S = 1/1 + 3/2 + 5/3 + 7/1 + ... + 99/50

soma = 0

for i in range(50):
    numerador = (2 * i) + 1
    denominador = i + 1
    soma += numerador / denominador
print(f"Soma = {soma}")