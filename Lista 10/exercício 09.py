#Escreva um programa que lê uma frase e uma string antiga e uma string nova. O programa deve imprimir uma string contendo a frase original, mas com a última ocorrência da string antiga substituída pela string nova. Exemplo:
#	Frase: "Quem parte e reparte fica com a maior parte"
#	String antiga: "parte"
#	String nova: "parcela"
#	Resultado a ser impresso no programa principal: "Quem parte e reparte fica com a maior parcela"

f, a, n = input("Frase: ").split(), input("Antiga: "), input("Nova: ")
if a in f:
    for i in range(len(f)-1,0, -1):
        if a in f[i]:
            f[i] = n
            break
    for i in range(len(f)):
        print(f[i], end=" ")
else:
    print("Não encontrado.")