#Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e imprima a data com o mês escrito por extenso. Exemplo:
#Data = 20/02/1995.
#Resultado gerado pelo programa: Você nasceu em 20 de fevereiro de 1995

d = input().split("/")
m = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho", 7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
print(f"Você nasceu em {d[0]} de {m[int(d[1])]} de {d[2]}")