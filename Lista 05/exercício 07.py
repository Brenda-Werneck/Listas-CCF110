#Criar um algoritmo que receba vários números inteiros e positivos e escreva a média dos números múltiplos de 3. A execução deve encerrar quando um número não positivo for lido.

n = 0 
soma = 0
cont = 0
while True:
    n = int(input("Digite um número: "))
    if n <= 0:
        break
    if n % 3 == 0:
        soma += n
        cont += 1
    media = soma / cont
print(media)