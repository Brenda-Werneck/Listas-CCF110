#Dada a razão de uma P.A. (progressão aritmética), e um termo qualquer k (), escreva um algoritmo para calcular qualquer outro termo, n, (). Leia os valores que considerar necessários.

r = float(input("Digite a razão: "))
ak = float(input("Digite o primeiro termo: "))
n = float(input("Digite o termo desejado: "))
k = float(input("Digite qualquer termo: "))
an = ak + (n - k) * r
print(an)
