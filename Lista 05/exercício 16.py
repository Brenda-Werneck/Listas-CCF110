#Criar um algoritmo que leia um conjunto de informações (nome, sexo, idade, peso e altura) dos atletas que participaram de uma olimpíada, e informar:
#	O atleta do sexo masculino mais alto;
#	A atleta do sexo feminino mais pesada;
#	A média de idade dos atletas.

#Deverão ser lidos dados dos atletas até que seja digitado o nome @ para um atleta.

maiorAlt = 0
maiorPeso = 0
cont = 0
somaidade = 0

while True:
    nome = input("Digite o nome: ")
    if nome == "@":
        break
    sexo = input("Digite o sexo (M ou F): ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso em kg: "))
    alt = float(input("Digite a altura em metros: "))
    if sexo == "M" and alt > maiorAlt:
        maiorAlt = alt
        altnome = nome
    elif sexo == "F" and peso > maiorPeso:
        maiorPeso = peso
        pesonome = nome
    somaidade += idade
    cont += 1

print(f"O atleta mais alto é o: {altnome} com {maiorAlt}m")
print(f"A atleta mais pesada é a: {pesonome} com {maiorPeso}kg")
print(f"A média das idades é {somaidade / cont} anos")