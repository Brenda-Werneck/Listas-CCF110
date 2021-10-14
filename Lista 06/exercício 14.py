#Crie um algoritmo para um lava jato o qual tem-se as seguintes entrada de dados:
#	Número identificador (id);
#	Valor a pagar.

#Armazene esses dados em vetores distintos e em seguida mostre a lista de dados do lava jato. O programa deve ser encerrado quando se digita um número negativo para o id do cliente. Ao fim, deve ser apresentado o valor total do caixa.

id = []
pagar = []
soma = 0

while True:
    id.append(int(input("Digite o ID do cliente: ")))
    if id[len(id) - 1] < 0:
        break
    pagar.append(float(input("Digite o valor a pagar: R$")))
    soma += pagar[len(pagar) - 1]
print(f"Números identificadores[id]: {id}")
print(f"Valor a pagar dos id: {pagar}")
print(f"O valor total em caixa é: R${soma:.2f}")