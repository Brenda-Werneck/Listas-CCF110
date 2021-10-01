#Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
# Não eleitor (abaixo de 16 anos);
# Eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
# Eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).

idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Não eleitor")
if idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
if (idade >= 16 and idade <18) or idade > 65:
    print("Eleitor facultativo")