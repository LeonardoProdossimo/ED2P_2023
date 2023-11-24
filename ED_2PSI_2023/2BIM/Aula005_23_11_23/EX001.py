N = 3
M = 3

import random as r
matriz = []

for i in range(N):
    lista = []
    for j in range(M):
        num  = r.randint(1,100)
        lista.append(num)
        print(lista)
    matriz.append(lista)

print(matriz)

print("------")
qtd = 0
for i in range(N):
    for j in range(M):
        if(matriz[i][j] % 2 == 0):
            print(matriz[i][j],end='\t')
            qtd += 1
print()
print(f"Quantidade de números pares é: {qtd}")