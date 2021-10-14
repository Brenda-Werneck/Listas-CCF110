#Faça um algoritmo que leia um vetor (variável composta) de N valores numéricos (N ≤ 20) e ordene essa variável em ordem crescente. O programa também deve ler um número k, e escrever, antes e depois da ordenação, o k-ésimo termo da variável composta.

vetor = []
N = int(input("Digite um valor: "))
k = int(input("Digite outro valor: "))

if k < N:
    if N <= 20:
        for i in range(N):
            n = int(input(f"Digite o {i + 1}º valor do vetor: "))
            vetor.append(n)

        for i in range(N):
            if i + 1 == k:
                print(f"O {k}º valor do vetor é {vetor[i]}")

        for i in range(N):
            aux = 0
            for j in range(N - 1):
                if vetor[j] > vetor[j + 1]:
                    aux = vetor[j]
                    vetor[j] = vetor[j + 1]
                    vetor[j + 1] = aux

        for i in range(N):
            if i + 1 == k:
                print(f"O {k}º valor do vetor ordenado é {vetor[i]}")
    else:
        print("Valor inválido. Tente novamente.")
else:
    print("ERRO. Tente novamente.")