#Faça um programa para alterar uma das notas de um aluno (usando os arquivos do exercício anterior). O programa deve receber o nome do aluno, a nota velha e a nova nota.

nome = str(input("Digite o nome do aluno que deseja realizar a modificação:"))
notavelha = str(input("Digite a nota que deseja alterar: "))
notanova = str(input(f"Digite a nova nota do aluno {nome}: "))

arquivoNomes = open("nomes.txt","r")
tam = len(arquivoNomes.readlines())
arquivoNomes.close()
arquivoNomes = open("nomes.txt","r")
flag = 0
for i in range(tam):
    if arquivoNomes.readline().strip("\n") == nome:
        posicao = 1
        flag = 1
        break
arquivoNomes.close()

if flag == 1:
    arquivoNotas = open
    ("notas.txt","r")
    linhas = arquivoNotas.readlines()
    frase = linhas[posicao].split()
    novo = ""

    for j in range(len(frase)):
        if frase[j] == notavelha:
            novo += notavelha + " "
        else:
            novo += frase[j] + " "
    novo += "\n"
    linhas[posicao] = novo
    arquivoNotas = open("notas.txt","w")
    arquivoNotas.writelines(linhas)
    arquivoNotas.close()
else:
    print("Aluno incorreto\n")