#1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova

import random as r

matriz = []
listaMinoridade = []

for i in range(10):
    pessoas = []
    pessoas.append(f'Ciclano{i+1}')
    pessoas.append(r.randint(1,80))
    matriz.append(pessoas)
    listaMinoridade.append(pessoas[1])

print("Matriz")
for i in range(len(matriz)):
    for j in range(len(pessoas)):
        print(matriz[i][j],end='\t')
    print()

ind = listaMinoridade.index(min(listaMinoridade))
print(f"A pessoa mais nova é {matriz[ind][0]} e sua idade é {min(listaMinoridade)} anos")

