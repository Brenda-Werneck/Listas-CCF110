#Elaborar um algoritmo que calcule e apresente a área e o perímetro de um quadrado. As dimensões do quadrado devem ser informadas pelo usuário.

lado = float(input("Digite o valor do lado do quadrado em cm: "))
area = lado ** 2
perimetro = 4 * lado
print(f"O perímetro do quadrado é {perimetro}cm \n A área é {area}cm²")