#O valor aproximado do número   pode ser calculado usando-se a série: 
#S = 1 - (1/(3^3)) + (1/(5^3)) + (1/(7^3)) + (1/(9^3)) ...
#Sendo  pi = raiz cubica de S.32, faça um algoritmo que calcule e escreva o valor de usando os 51 primeiros termos da séria acima.  (Dica: Observe que agora não são apenas somas)

soma = 0

for i in range(51):
    d = (2 * i) + 1
    if i % 2 == 0:
        soma += 1 / (d ** 3)
    else:
        soma -= 1 / (d ** 3)
pi = (soma * 32) ** (1/3)
print(pi)
