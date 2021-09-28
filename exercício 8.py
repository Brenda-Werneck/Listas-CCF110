#O custo ao consumidor de um carro novo é a soma do custo de fábrica com o percentual do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo do consumidor.

custofab = float(input("Digite o custo de fábrica do carro em reais: "))
distribuidor = custofab * 0,28
impostos = custofab * 0,45
custocons = custofab + distribuidor + impostos
print(f"O custo do consumidor É R${custocons}")