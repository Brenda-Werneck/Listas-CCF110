#Faça um programa que funciona como uma agenda telefônica. A agenda deve ser guardada em uma lista com o seguinte formato: [[‘Ana’, ‘99999-1234’], [‘Bia’, ‘99999-5678’]]. (Não utilize esses dados. Isso é só um exemplo da estrutura. Leia todos os dados do teclado). O programa deve ter um menu que tenha as seguintes opções: 
#a.	Adicionar telefones na agenda -- isso deve ser feito de forma que ela se mantenha sempre ordenada
#b.	Procurar um telefone -- o usuário informa um nome e o programa mostra o número do telefone, ou diz que não está na agenda
#A busca deve ser inteligente: deve parar assim que encontrar um nome maior do que o nome que está sendo buscado, ao invés de percorrer a lista sempre até o final para concluir que um nome não está na agenda.

agenda = [[0 for j in range(2)] for i in range(10)]
cont = 0
while True:
    N = int(input("O que deseja realizar? Digite: \n1) Para adicionar um contato \n2) Para buscar um Telefone \n3) Parar a execução"))
    if N == 3:
        print("Saindo...")
        break
    elif N == 1:
        nome, telefone = input("Digite o nome e o telefone: ").split()
        agenda[cont][0] = nome
        agenda[cont][1] = telefone
        print("INSERIDO COM SUCESSO!")
    elif N ==2:
        s = input("Digite o nome que deseja pesquisar: ")
        for i in range(len(agenda)):
            if s == agenda[i][0]:
                print(f"Telefone {agenda[i][1]}")
    else:
        print("OPÇÃO INVÁLIDA")
    cont += 1
