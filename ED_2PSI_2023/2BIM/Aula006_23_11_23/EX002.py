"""
2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
número k. Imprima a matriz na tela antes e depois da multiplicação.
ex:     
input
|4      6     9|
|3      2     7|
|1      2     5|

ouput, suponha k = 5
|20     6     9|
| 3    10     7|
| 1     2    25|
"""

import random as r

matriz = []
mult = 1

print("Matriz")
for i in range(3):
    numeros = []
    for j in range(3):
        numeros.append(r.randint(1,10))
        matriz.append(numeros)
        print(matriz[i][j], end=' \t')
    print()
    mult *= matriz[i][i]

print(f"O resultado da multiplicação da diagonal principal é: {mult}")
