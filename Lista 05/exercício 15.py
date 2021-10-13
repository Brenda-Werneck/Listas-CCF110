#Um cinema possui capacidade de 100 lugares e está sempre com ocupação total. Certo dia, cada espectador respondeu a um questionário, no qual constava:
#idade;
#opinião em relação ao filme, segundo as seguintes notas:
#Nota	        Significado
#A	        Ótimo
#B	        Bom
#C	        Regular
#D	        Ruim
#E	        Péssimo

#Elabore um algoritmo que, lendo estes dados, calcule e escreva:
#	a quantidade de respostas ótimo;
#	a diferença percentual entre respostas bom e regular;
#	a média de idade das pessoas que responderam ruim;
#	a porcentagem de respostas péssimo e a maior idade que utilizou esta opção;
#	a diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim.

contA = 0 
contB = 0
contC = 0 
contD = 0
contE = 0 
somaidade = 0
maioridaderuim = 0
maioridadeotimo = 0
maioridadepessimo = 0 
matriz = [[0 for i in range(100)] for j in range(2)]

for j in range(100):
    matriz[0][j] = int(input("Digite a sua idade: "))
    matriz[1][j] = input("Digite sua nota ao filme: ")
for j in range(100):
    if matriz[1][j] == "A":
        contA += 1
        if matriz[0][j] > maioridadeotimo:
            maioridadeotimo = matriz[0][j]
    if matriz[1][j] == "B":
        contB += 1
    if matriz[1][j] == "C":
        contC += 1
    if matriz[1][j] == "D":
        somaidade += matriz[0][j]
        contD += 1
        if maioridaderuim > matriz[0][j]:
            maioridaderuim = matriz[0][j]
    if matriz[1][j] == "E":
        contE += 1
        if matriz[0][j] > maioridadepessimo:
            maioridadepessimo = matriz[0][j]
difidadeAeD = maioridadeotimo - maioridaderuim
difperc = contB - contC
mediaidaderuim = somaidade / contD
print(f"Quantidade de respostas ótimo: {contA}")
print(f"Diferença percentual entre respostas bom e regular: {difperc}%")
print(f"Média da idade das pessoas que responderam ruim: {mediaidaderuim} anos")
print(f"Porcentagem de respostas péssimo: {contE}%")
print(f"Maior idade que respondeu péssimo: {maioridadepessimo} anos")
print(f"Diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim: {difidadeAeD} anos")