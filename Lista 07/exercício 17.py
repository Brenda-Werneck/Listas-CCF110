#Um armazém trabalha com 100 mercadorias diferentes identificadas pelos números inteiros de 1 a 100. O dono do armazém anota a quantidade de cada mercadoria vendida durante o mês. Ele tem uma tabela que indica, para cada mercadoria, o preço de venda. Escreva um algoritmo para calcular o faturamento mensal do armazém. A tabela de preços é fornecida seguida pelos números das mercadorias e as quantidades vendidas. Quando uma mercadoria não tiver nenhuma venda, é informado o valor zero no lugar da quantidade.

qtd = []
preco = []
faturamento = 0

for i in range(100):
    qtd.append(int(input()))

for c in range(100):
    preco.append(float(input()))

for i, v in enumerate(qtd):
    for l, k in enumerate(preco):
        faturamento += faturamento + (qtd[i] * preco[l])

print(f"Faturamento mensal: R${faturamento:.2f}")

