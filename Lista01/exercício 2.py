#Fazer um algoritmo que leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e escrever quantos salários mínimos essa pessoa ganha.

minimo = float(input("Digite o valor do salário mínimo atual em reais: "))
salario = float(input("Digite o valor do seu salário atual em reais: "))
qtdadesala = salario / minimo
print(f"A quantidade de salários mínimos que você recebe é: {qtdadesala}")