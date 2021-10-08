#Criar um algoritmo que possa ler um conjunto de pedidos de compra e calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#	Número de pedido;
#	Data do pedido (dia, mês, ano);
#	Preço unitário;
#	Quantidade.
#O algoritmo deverá processar novos pedidos até que o usuário digite (zero) como número de pedido.

total = 0

while True:
    num = int(input("Digite o número do pedido: "))
    if num == 0:
        break
    data = input("Data do pedido DD/MM/AA: ")
    precouni = float(input("Digite o preço unitário: "))
    quant = int(input("Digite a quantidade: "))
    total += precouni * quant
print(f"Total = R${total}")