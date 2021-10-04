#A gerente do cabeleireiro Sempre Bela tem uma tabela em que registra os "pés", as “mãos” e “pés e mãos”. Sabendo-se que cada uma ganha 50% do que faturou ao mês, criar um algoritmo que possa calcular e escrever quanto cada um vai receber, uma vez que não têm carteiras assinadas; os valores, respectivamente, são R$ 10,00; R$ 15,00 e R$ 30,00.

N = int(input("Informe o número de funcionárias: "))
T = [[0 for j in range(3)] for i in range(N)]
Nome = []

for i in range(N):
    Nome.append(input(f"Informe o nome da funcionária {i + 1}: "))
    T[i][0] = int(input(f"Informe o número de 'pés' feitos da funcionária {Nome[i]}: "))
    T[i][1] = int(input(f"Informe o número de 'mãos' feitos da funcionária {Nome[i]}: "))
    T[i][2] = int(input(f"Informe o número de 'pés e mãos' feitos da Funcionaria {Nome[i]}: "))
    print(f"Funcionaria: {Nome[i]} receberá no total: R${((T[i][0] * 10) + (T[i][1] * 15) + (T[i][2] * 30)) * 0.5}")
