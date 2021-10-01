#Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais uma comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda. Elabore um algoritmo para calcular e escrever o salário do vendedor num dado mês recebendo como dados de entrada o nome do vendedor, o número de carros vendidos e o valor total das vendas.

nome = input("Digite o nome do vendedor: ")
numcarros = int(input(f"Digite o número de carros vendidos pelo vendedor {nome}: "))
valortot = int(input(f"Digite o valor total das vendas do vendedor {nome} em reais: "))
salario = 500 + (50 * numcarros) + (valortot * 0.05)
print(f"O salário do vendedor {nome} é R${salario}")