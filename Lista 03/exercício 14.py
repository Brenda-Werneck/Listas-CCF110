#Em uma eleição presidencial, existem quatro candidatos. Os votos são informados através de código. Os dados utilizados para o escrutínio obedecem à seguinte codificação:
#	1, 2, 3 e 4 = voto para os respectivos candidatos;
#	5 voto nulo;
#	6 voto em branco;

#Elaborar um algoritmo que calcule e escreva:
#	O total de votos para cada candidato;
#	O total de votos nulos;
#	O total de votos em branco;
#	O percentual dos votos em branco e nulos sobre o total.

voto = 1
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0 
tot = 0

while voto >= 1 and voto <= 6:
    voto = int(input("Digite: \n1 para o candidato Fulano; \n2 para o candidato Sicrano; \n3 para o candidato Beltrano; \n4 para o candidato Metano; \n5 para nulo; \n6 para voto em branco \n"))
    if voto >= 1 and voto <= 6:
        if voto == 1:
            cont1 += 1
        if voto == 2:
            cont2 += 1
        if voto == 3:
            cont3 += 1
        if voto == 4:
            cont4 += 1
        if voto == 5:
            cont5 += 1
        if voto == 6:
            cont6 += 1
        if voto >= 1 and voto <= 6:
            tot += 1
print(f"\nO candidato Fulano recebeu {cont1} votos \nO candidato Sicrano recebeu {cont2} votos \nOcandidato Beltrano recebeu {cont3} votos \nO candidato Metano recebeu {cont4} votos \nHouveram {cont5} votos nulos \nO percentual de votos brancos e nulos é: {(((cont6 + cont5) / tot) * 100)}%")