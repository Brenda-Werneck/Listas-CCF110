#Faça um programa que lê uma string que representa uma cadeia de DNA e gera a cadeia complementar. Exemplo:
#	Entrada: AATCTGCAC
#	Saída: TTAGACGTG

n, m, nn = input(), {"A": "T", "T": "A", "G": "C", "C": "G", "A": "T"}, ""
for x in n: nn += m[x]
print(nn)
