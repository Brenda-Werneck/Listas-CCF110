#Crie um algoritmo que leia o valor gasto com despesas realizadas em um restaurante e escreva o valor da gorjeta (10%) e o valor total com a gorjeta.

despesa = float(input("Digite o valor gasto em reais: "))
gorjeta = despesa / 10
valortotal = gorjeta + despesa
print(f"O valor da gorjeta é R${gorjeta} \nE o valor total com a gorjeta é R$ {valortotal}")