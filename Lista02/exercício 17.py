#A prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação, e informar se o empréstimo pode ou não ser concedido.

salbruto = float(input("Digite o salário bruto em reais: "))
valorprest = float(input("Digite o valor da prestação em reais: "))
if valorprest <= 0.3 * salbruto:
    print("Empréstimo pode ser concedido")
if valorprest > 0.3 * salbruto:
    print("Empréstimo não pode ser concedido")
    