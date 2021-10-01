#Escreva um algoritmo que leia um número (1 a 7) e escreva o dia da semana correspondente. Caso o usuário digite um número fora do intervalo válido, deve ser escrita a mensagem “Dia da semana inválido”.

dia = int(input("Digite um número: "))
if dia > 7 or dia < 1:
    print("Dia da semana inválido")
else:
    if dia == 1:
        print("Domingo")
    if dia == 2:
        print("Segunda-feira")
    if dia == 3:
        print("Terça-feira")
    if dia == 4:
        print("Quarta-feira")
    if dia == 5:
        print("Quinta-feira")
    if dia == 6:
        print("Sexta-feira")
    if dia == 7:
        print("Sábado")