#Faça um programa que recebe os nomes de dois arquivos. O primeiro arquivo contém nomes de alunos e o segundo arquivo contém as notas dos alunos. No primeiro arquivo, cada linha corresponde ao nome de um aluno e no segundo arquivo, cada linha corresponde às notas dos alunos (uma ou mais). Assuma que as notas foram armazenadas como strings, e estão separadas umas das outras por espaços em branco. Leia os dois arquivos e gere um terceiro arquivo que contém o nome do aluno seguido da média de suas notas.

arquivoNomes = open("nomes.txt","r")
arquivoNotas = open("notas.txt","r")
arquivo = open("geral.txt","w")

tam = len(arquivoNomes.readlines())
arquivoNomes.close()
arquivoNomes = open("nomes.txt","r")

for i in range(tam):
    nome = arquivoNomes.readline()
    notas = arquivoNotas.readline().split()
    soma = 0
    for j in range(len(notas)):
        soma += int(notas[j])
    media = soma / len(notas)
    media = str(media)
    frase = nome.strip("\n") + " " + media + "\n"
    arquivo.writelines(frase)

arquivoNomes.close()
arquivoNotas.close()
arquivo.close()