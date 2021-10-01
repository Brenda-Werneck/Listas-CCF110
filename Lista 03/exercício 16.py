#Uma empresa fez uma pesquisa para saber se as pessoas gostaram ou não de um novo produto lançado no mercado. Para isso, forneceu o sexo do entrevistado (1 = masculino, 2 = feminino) e sua resposta (1 = sim, 2 = não). Sabendo-se que foram entrevistadas 2.000 pessoas, faça um algoritmo que calcule e escreva:
#	O número de pessoas que responderam sim;
#	O número de pessoas que responderam não;
#	A porcentagem de pessoas do sexo feminino que responderam sim;
#	A porcentagem de pessoas do sexo masculino que responderam não.

contmasc = 0
contfem = 0
contlike = 0 
conthate = 0
contfemlike = 0
contmaschate = 0

matriz = [[0 for i in range(2)] for j in range(2000)]

for i in range(2000):
        matriz[i][0] = int(input("Digite: \n1 para sexo masculino \n2 para sexo feminino \n"))
        matriz[i][1] = int(input("Digite: \n1 para você gostou do produto \n2 para você não gostou do produto \n"))
        if matriz[i][0] == 1:
            contmasc += 1
        if matriz[i][0] == 2:
            contfem += 1
        if matriz[i][1] == 1:
            contlike += 1
            if matriz[i][0] == 2:
                contfemlike += 1
        if matriz[i][1] == 2:
            conthate += 1
            if matriz[i][0] == 1:
                contmaschate += 1
print(f"\nNúmero de pessoas que gostaram do novo produto = {contlike} \nNúmero de pessoas que não gostaram do novo produto = {conthate} \nPercentual de mulheres que gostaram do novo produto = {(contfemlike * 100) / contfem} \nPercentual de homens que não gostaram do novo produto = {(contmaschate * 100) / contmasc}")