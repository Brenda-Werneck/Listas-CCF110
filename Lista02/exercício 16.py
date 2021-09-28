#Escreva um algoritmo que leia um número de mês (1 a 12) e escreva em qual trimestre esse mês se encaixa. Caso o usuário digite um número fora do intervalo válido, deve ser escrita a mensagem “Mês inválido”.

mes = int(input("Digite um número: "))
if mes > 12 or mes < 1:
    print("Mês inválido")
else:
    if mes >= 1 and mes <= 3:
        print("Primeiro trimestre")
        if mes >= 4 and mes <= 6:
            print("Segundo trimestre")
        if mes >= 7 and mes <= 9:
            print("Terceiro trimestre")
        if mes >=10 and mes <= 12: 
            print("Quarto trimestre")
