#Criar um algoritmo que receba vários números inteiros e positivos e escreva o produto dos números ímpares digitados e a soma dos pares. O algoritmo encerra quando o zero ou um número negativo é digitado.
n = 1
vetor = []
prod = 1
soma = 0

while n > 0:
    qtd = int(input("Quantos valores deseja calcular: "))
    for i in range(qtd + 1):
        n = int(input("Digite um número (ou 0 para encerrar): "))
        if n > 0:
            vetor.append(n)
        else:
            break
    for  i in range(qtd):
        if vetor[i] % 2 == 0:
            soma += vetor[i]
        else:
            prod = prod * vetor[i]
    print(f"Soma pares = {soma} \nProduto ímpares = {prod}")