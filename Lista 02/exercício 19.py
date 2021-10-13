#Criar um algoritmo que, a partir da idade e peso do paciente, calcule a dosagem de determinado medicamento e escreva a receita informando quantas gotas do medicamento o paciente deve tomar por dose. Considere que o medicamento em questão possui 500 mg por ml, e que cada ml corresponde a 20 gotas.Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou acima de 60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos devem tomar 875 mg; Para crianças e adolescentes abaixo de 12 anos a dosagem é calculada pelo peso corpóreo conforme a tabela a seguir:

#Peso           Dosagem
#5kg a 9kg  	125mg
#9kg a 16kg 	250mg
#16kg a 24kg	275mg
#24kg a 30kg	500mg
#Acima de 30kg	750mg

#Sugestão: Faça os intervalos incluindo o valor menor e deixando o valor maior de fora. Exemplo: 5kg, inclusive, até 9kg. Depois: 9kg, inclusive, até 16kg. E assim por diante.

idade = int(input("Digite sua idade em anos: "))
peso = float(input("Digite seu peso em kg: "))
if idade >= 12 and peso >= 60:
    print("Você deve tomar 1000mg")
if idade >= 12 and peso < 60:
    print("Você deve tomar 875mg")
if idade < 12 and peso >= 5 and peso < 9:
    print("Você deve tomar 125mg")
if idade < 12 and peso >= 9 and peso < 16:
    print("Você deve tomar 250mg")
if idade < 12 and peso >= 16 and peso < 24:
    print("Você deve tomar 275mg")
if idade < 12 and peso >= 24 and peso < 30:
    print("Você deve tomar 500mg")
if idade <12 and peso >= 30:
    print("Você deve tomar 750mg")
