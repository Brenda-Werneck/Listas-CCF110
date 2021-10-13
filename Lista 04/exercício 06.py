#Certo dia o professor de Johann Friederich Carl Gauss (aos 10 anos de idade) mandou que os alunos somassem os números de 1 a 100. Imediatamente Gauss achou a resposta – 5050 – aparentemente sem cálculos. Supõe-se que já aí, Gauss, houvesse descoberto a fórmula de uma soma de uma progressão aritmética.
#Construa um algoritmo para realizar a soma de uma P.A. de N termos, com o primeiro a1 e o último an.

n = int(input("Digite a quantidade de termos: "))
a = float(input("Digite o primeiro termo: "))
an = float(input("Digite o enésimo número: "))
sn = ((a + an) * n) / 2
print(f"Soma da P.A de {n} termos = {sn}")