#A Caixa Econômica Federal (CEF) concederá um crédito especial com juros de 2% aos seus clientes de acordo com o saldo médio no último ano. Fazer um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. Escrever uma mensagem informando o saldo médio e o valor de crédito.

#Saldo médio	        Percentual
#De 0 a 500	        Nenhum crédito
#De 501 a 1000	        30% do valor do saldo médio
#De 1001 a 3000	        40% do valor do saldo médio
#Acima de 3001	        50% do valor do saldo médio

saldomedio = int(input("Digite o saldo médio: "))
if saldomedio < 500:
    print(f"Com saldo médio de R${saldomedio}: nenhum crédito")
if saldomedio > 500 and saldomedio <= 1000:
    print(f"Com saldo médio de {saldomedio}: crédito de 30% = R${0.3 * saldomedio}")
if saldomedio > 1001 and saldomedio <= 3000:
    print(f"Com saldo médio de {saldomedio}: crédito de 40% = R${0.4 * saldomedio}")
if saldomedio > 3001:
    print(f"Com saldo médio de {saldomedio}: crédito de 50% = R${0.5 * saldomedio}")