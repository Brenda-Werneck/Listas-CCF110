#Criar um algoritmo que receba 10 números positivos e escreva a raiz quadrada de cada número. Para cada entrada de dados deverá haver um trecho de proteção para que um número negativo não seja aceito.

vetor = []

for i in range(10):
    n = int(input("Digite um número: "))
    vetor.append(n)
for i in range(10):
    if vetor[i] < 0:
        vetor[i] = int(input(f"Digite um novo valor pois {vetor[i]} é inválido "))

for i in range(10):
    raiz = vetor[i] ** (1/2)
    print(raiz)