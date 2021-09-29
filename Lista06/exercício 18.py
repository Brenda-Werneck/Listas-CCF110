#Escreva um algoritmo que receba o número da conta e o saldo de várias pessoas. O algoritmo deve, após a leitura de todas as contas, escrever todas as contas, os respectivos saldos e uma das mensagens: positivo/negativo. Ao final, deverá sair o total de clientes com saldo negativo, o total de clientes da agência, o saldo da agência e o percentual de pessoas com saldo negativo. O algoritmo acaba quando se digita um número negativo para a conta.

dados = []
vetor = []

while True:
    vetor.append(int(input("Número da conta: ")))
    if vetor[0] < 0:
        break
    vetor.append(float(input("Digite o saldo da conta: ")))
    dados.append(vetor[:])
    vetor.clear()
cont_negt = soma = 0
for n in range(len(dados)):
    print(f"Conta = {dados[n][0]}, Saldo = R$ {dados[n][1]:.2f}", end="")
    if dados[n][1] >= 0:
        print("Saldo positivo")
    else:
        print("Saldo negativo")
        cont_negt += 1
    soma += dados[n][1]
print(f"A agência tem {len(dados)} clientes no total")
print(f"A agência tem {cont_negt} clientes com saldo negativo, o que representa {(100 * cont_negt) / len(dados)}% dos "
      f"clientes")
print(f"A agência tem um saldo de R${soma}")
