N = int(input())
C = int(input())
matriz = [[0 for i in range(N)] for j in range(N)]
cont = 1
s = input().split()
posicao = 0
for i in range(N):
    for j in range(N):
        matriz[i][j] = s[posicao]
        posicao += 1
x = 0

while x <= N*2:
    for i in range(N):
        if matriz[C][i] in "1" and C != i:
            matriz[C][i] = "9" #tirar como 1 pra nao contar 2x
            matriz[i][C] = "9" #tirar como 1 pra nao contar 2x
            cont += 1
            aux = i
            for j in range(N):
                if matriz[aux][j] in "1" and aux != j:
                    cont += 1
                    matriz[aux][j] = "9" #tirar como 1 pra nao contar 2x
                    matriz[j][aux] = "9" #tirar como 1 pra nao contar 2x
                    aux2 = j
                    for k in range(N):
                        if matriz[aux2][k] in "1" and aux2 != k:
                            cont += 1
                            matriz[aux2][k] = "9"
                            matriz[k][aux2] = "9"
                            aux3 = k
                            for l in range(N):
                                if matriz[aux3][l] in "1" and aux3 != l:
                                    cont += 1
                                    matriz[aux3][l] = "9"
                                    matriz[l][aux3] = "9"
                                    aux4 = l
                                            
    x += 1
print(cont)
