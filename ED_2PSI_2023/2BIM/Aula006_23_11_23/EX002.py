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
mult = r.randint(0,10)
print(f"Número que irá multiplicar é: {mult}")
print()

print("Matriz Antes")
for i in range(3):
    numeros = []
    for j in range(3):
        numeros.append(r.randint(1,10))
    matriz.append(numeros)
    print(matriz[i])
    matriz[i][i] *= mult
    
print()
print("Matriz Depois")
for k in range(3):
    print(matriz[k])

