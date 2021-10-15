#Uma floricultura conhecedora de sua clientela gostaria de fazer um algoritmo que pudesse controlar sempre um estoque mínimo de determinadas plantas, pois todo dia, pela manhã, o dono faz novas aquisições. Criar um algoritmo que deixe cadastrar 50 tipos de plantas e nunca deixar o estoque ficar abaixo do ideal. Para cada planta, o dono gostaria de cadastrar o nome, o estoque ideal e a quantidade em estoque. Dessa forma o algoritmo pode calcular a quantidade que o dono da loja precisa comprar no próximo dia. Essa quantidade a ser comprada deve ser escrita (quando maior que zero) como uma lista para o dono da floricultura.

matriz = [[0 for i in range(3)] for j in range(50)]

for i in range(50):
    matriz[i][0] = input(f"Digite o nome da planta {i + 1}: ")
    matriz[i][1] = int(input(f"Digite o valor para o estoque ideal de {matriz[i][0]}: "))
    matriz[i][2] = int(input(f"Digite a quantidade em estoque de {matriz[i][0]}: "))

for i in range(50):
    qtdcompra = matriz[i][1] - matriz[i][2]
    if qtdcompra > 0:
        print(f"É necessário comprar {qtdcompra} de {matriz[i][0]}")
    else:
        print(f"Já possui o estoque ideal de {matriz[i][0]}")