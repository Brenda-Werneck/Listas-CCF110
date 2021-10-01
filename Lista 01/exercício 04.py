#Escreva um algoritmo que leia uma temperatura em graus Celsius e apresente a temperatura convertida em graus Fahrenheit. A fórmula de conversão é: F = (C * 1,8) + 32.

celsius = float(input("Digite a temperatura em graus Celsius: "))
f = (celsius * 1,8) + 32
print(f"A temperatura é {f}F")