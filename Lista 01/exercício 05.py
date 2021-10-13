#Criar um algoritmo para calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: V = 3,14159 * R2 * h, onde V é o volume, R é o raio e h é a altura.

raio = float(input("Digite o raio da lata em cm: "))
altura = float(input("Digite a altura da lata em cm: "))
volume = 3,14159 * (raio ** 2) * altura
print(f"O volume da lata é: {volume}cm³")