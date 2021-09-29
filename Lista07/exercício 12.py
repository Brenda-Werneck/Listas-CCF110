#Fazer um algoritmo que:
#a.	Leia um conjunto de valores inteiros correspondentes a 80 notas dos alunos de uma turma, notas estas que variam de 0 a 10;
#b.	Calcule a frequência absoluta e a frequência relativa de cada nota;
#c.	Escreva uma tabela contendo os valores das notas (de 0 a 10) e suas respectivas frequências absoluta e relativa.
#Observações:
#1.	Frequência absoluta de uma nota é o número de vezes em que aparece no conjunto de dados;
#2.	Frequência relativa é a frequência absoluta dividida pelo número total de dados;
#3.	Utilizar como vetor  somente as variáveis que forem necessárias.

vetor = []

for i in range(10):
    n = int(input(f"Digite a {i + 1}ª nota para o vetor: "))
    if 0 <= n <= 10:
        vetor.append(n)
    else:
        print("Nota inválida. Insira as notas novamente.")

for i in range(11):
    repete = 0
    for j in range(10):
        if vetor[i] == vetor[j]:
            repete += 1
    fr = repete / 10
    print(f"Frequência absoluta de {vetor[i]} = {repete}")
    print(f"Frequência relativa de {vetor[i]} = {fr}")
