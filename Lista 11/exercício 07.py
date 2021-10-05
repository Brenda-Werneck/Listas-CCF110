#Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere dois outros arquivos, um contendo os endereços IP válidos e outro contendo os endereços inválidos. O formato de um endereço IP é num1.num.num.num, onde num1 vai de 1 a 255 e num vai de 0 a 255.

arquivoIPS = open("ips.txt","r")
arquivoIPSValidos = open("ipsValido.txt","w")
arquivoIPSinvalidos = open("ipsinvalidos.txt","w")

for linha in arquivoIPS:
    ip = linha.strip("\n").split(".")
    cont = 1
    if (int(ip[0]) >= 1 and int(ip[0]) <= 255):
        for i in range(1,4):
            if(int(ip[i]) >= 0 and int(ip[i]) <= 255):
                cont += 1
    if cont == 4:
        arquivoIPSValidos.writelines(linha)
    else:
        arquivoIPSinvalidos.writelines(linha)
        
arquivoIPS.close()
arquivoIPSValidos.close()
arquivoIPSinvalidos.close()