#Fazer um algoritmo que calcule e escreva o número de grãos de milho que se pode colocar num tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros seguintes o dobro do quadro anterior. São 64 quadros e a fórmula é:

soma = 0
for i in range(64):
    soma += (2 ** i)
print(f"{soma} grãos de milho")