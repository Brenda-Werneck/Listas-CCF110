qtdModelos, qtdpermitida = map(int, input().split())

for i in range(qtdModelos):
    nomeModelo, qtdItensModelo = input().split()
    qtdItensModelo = (int)(qtdItensModelo)

    vetor = []
    for j in range(qtdItensModelo):
        acessorio, preco = input().split()
        preco = (int)(preco)
        vetor.append(preco)

    vetor.sort(reverse=True)
    precoTot = 0

    for k in range(qtdpermitida):
        precoTot += vetor[k]

    print(precoTot)