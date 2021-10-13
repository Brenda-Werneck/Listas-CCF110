#Dada a razão de uma P.G. (progressão geométrica) e um termo qualquer, k (). Escreva um algoritmo para calcular qualquer outro termo, n, (). Leia os valores que considerar necessários.

q = float(input("Digite a razão: "))
ak = float(input("Digite o primeiro termo: "))
n = float(input("Digite o termo desejado: "))
k = float(input("Digite qualquer termo: "))
an = ak * q ** (n - k)
print(an)