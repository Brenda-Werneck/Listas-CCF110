#Crie um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas de uma loja, em que cada linha represente um mês do ano, e cada coluna, uma semana do mês. Para fins de simplificação considere que cada mês possui somente 4 semanas. Calcule e escreva:

#	Total vendido em cada mês do ano;
#	Total vendido em cada semana durante todo o ano;
#	Total vendido no ano.

matriz = [[0 for i in range(4)] for j in range(12)]
somames = 0
somatot = 0

for i in range(12):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite o valor da semana {j + 1} do {i + 1}º mês: "))
for i in range(12):
    somatot += somames
    for j in range(4):
        somames += matriz[i][j]
        print(f"Foram vendidos R${matriz[i][j]} na semana {j +1} do {i + 1}º mês")
    print(f"Foram vendidos R${somames} nas 4 semanas do {i + 1}º mês")
print(f"Foram vendidos R${somatot} nos 12 meses do ano")