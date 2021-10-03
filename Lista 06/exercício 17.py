#Crie um algoritmo para uma empresa multinacional o qual controlará a compra de mercadoria da empresa, o valor monetário das compras será em dólar. Ao final o programa deverá mostrar uma relação das compras que terão o nome do produto e seu preço. O preço  deve ser mostrado em real e também em dólar.

dados = []
vetor = []

while True:
    vetor.append(str(input("Nome do produto: ")))
    vetor.append(int(input("Valor do produto em dólar: US$")))
    dados.append(vetor[:])
    vetor.clear()
    resp = " "
    while resp not in "NS":
        resp = str(input("Quer continuar[N/S]: ")).upper()
    if resp == "N":
        break
for n in range(len(dados)):
    print(f"O produto {dados[n][0]} custa US${dados[n][1]:.2f} ou R${dados[n][1] * 5.38:.2f}")
