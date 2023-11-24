N = 5
M = 5

import random as r
matriz = []

for i in range(N):
    lista = []
    for j in range(M):
        num  = r.randint(1,100)
        lista.append(num)
    matriz.append(lista)

print("------")
qtd = 0
for i in range(N):
    for j in range(M):
        print(matriz[i][j],end='\t')
        if(matriz[i][j] % 2 == 0):
            qtd += 1
    print()
print()
print(f"Quantidade de números pares é: {qtd}")
print()