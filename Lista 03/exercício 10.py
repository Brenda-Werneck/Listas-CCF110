#Elabore um algoritmo que calcule N! (fatorial de N), sendo que o valor inteiro de N é fornecido pelo usuário. Sabendo que:
#	N! = 1 * 2 * 3 * … * (N – 1) * N;
#	0! = 1, por definição.

prod = 1
N = int(input("Digite o valor que deseja calcular o fatorial: "))

for i in range(N, 0, -1):
    if N == 0:
        print(f"{N}! = 1")
    else:
        prod = prod * i
print(f"{N}! = {prod}")