#Construa um algoritmo para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corporal), que é definida como sendo a relação entre o peso (PESO) e o quadrado da Altura (ALTURA) do indivíduo. Ou seja,

#   IMC = PESO / (ALTURA^2)
 
#A situação do peso é determinada pela tabela abaixo:
#Condição	            Situação
#IMC abaixo de 20	    Abaixo do peso
#IMC de 20 até 25	    Peso Normal
#IMC de 25 até 30	    Sobrepeso
#IMC de 30 até 40	    Obeso
#IMC de 40 e acima	    Obeso Mórbido

altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em kg: "))
IMC = peso / (altura ** 2)
if IMC < 20:
    print("Situação: abaixo do peso")
if IMC >= 20 and IMC < 25:
    print("Situação: peso normal")
if IMC >= 25 and IMC < 30:
    print("Situação: sobrepeso")
if IMC >= 30 and IMC < 40:
    print("Situação: obeso")
if IMC >= 40:
    print("Situação: obeso mórbido")