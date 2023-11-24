
linhas = 5
colunas = 5

import random as r
matriz = []

for i in range(linhas):
    lista = []
    for j in range(colunas):
        num  = r.randint(1,100)
        lista.append(num)
    matriz.append(lista)

print("------")
qtd = 0
print("Matriz")
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j],end='\t')
        if(matriz[i][j] % 2 == 0):
            qtd += 1
    print()
print()
print(f"Quantidade de números pares é: {qtd}")
print()