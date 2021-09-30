#Escreva um programa que lê uma frase e uma string antiga e uma string nova. O programa deve imprimir uma string contendo a frase original, mas com a última ocorrência da string antiga substituída pela string nova. Exemplo:
#	Frase: "Quem parte e reparte fica com a maior parte"
#	String antiga: "parte"
#	String nova: "parcela"
#	Resultado a ser impresso no programa principal: "Quem parte e reparte fica com a maior parcela"

f, a, n, s = input("Frase: ").split(), input("Antiga: "), input("Nova: "), ""
if a in f:
    for x in f:
        if s != "":
            space = " "
        else:
            space = ""
        if x == a:
            s += space + n
        else:
            s += space + x
    print(s)
else:
    print("Não encontrado.")