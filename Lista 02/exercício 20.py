#Numa festinha de fim de curso, foi feito um sorteio para distribuir o dinheiro restante em caixa. Dez pessoas foram sorteadas com direito a tentar a sorte mais uma vez, da seguinte forma: Deveriam apanhar uma bola numerada de 0 a 9 e conforme o algarismo sorteado o prêmio seria:

#   Número da Bola	    Prêmio (% do valor do caixa)
#           0	                    05
#           1	                    25
#           2                       10
#           3	                    07
#           4	                    08
#           5	                    05
#           6	                    15
#           7	                    12
#           8	                    03
#           9	                    10

#Faça um algoritmo que leia o número da bola sorteada e o valor do dinheiro restante em caixa. Em seguida, o algoritmo deve calcular o prêmio recebido individualmente pela pessoa.

valorcaixa = float(input("Digite o valor do dinheiro no caixa: "))
bola = int(input("Digite um número: "))
if bola > 9 or bola < 0:
    print("Bolinha inválida")
else:
    if bola == 0:
        premio = 0.05 * valorcaixa
        print(f"Prêmio = R$ {premio}")
    if bola == 1:
        premio = 0.25 * valorcaixa
        print(f"Prêmio = R$ {premio}")
    if bola == 2:
        premio = 0.10 * valorcaixa
        print(f"Prêmio = R$ {premio}")
    if bola == 3:
        premio = 0.07 * valorcaixa
        print(f"Prêmio = R$ {premio}")
        if bola == 4:
            premio = 0.08 * valorcaixa
            print(f"Prêmio = R$ {premio}")
        if bola == 5:
            premio = 0.05 * valorcaixa
            print(f"Prêmio = R$ {premio}")
        if bola == 6:
            premio = 0.15 * valorcaixa
            print(f"Prêmio = R$ {premio}")
        if bola == 7:
            premio = 0.12 * valorcaixa
            print(f"Prêmio = R$ {premio}")
        if bola == 8:
            premio = 0.03 * valorcaixa
            print(f"Prêmio = R$ {premio}")
        if bola == 9:
            premio = 0.10 * valorcaixa
            print(f"Prêmio = R$ {premio}")
