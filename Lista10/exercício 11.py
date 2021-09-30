#Faça um programa que leia uma frase e retorne o número de palavras que a frase contém. 

text = input()
substring = " "

total_occurrences = (text.count(substring) + 1)

print("A frase tem " + str(total_occurrences) + " palavras")