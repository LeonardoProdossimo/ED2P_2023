"""
Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:

a) De quem foi a melhor volta da prova, e em que volta
b) Classificação final em ordem (1º o campeão)
c) Qual foi a volta com a média mais rápida
"""
import random as r

ContagemVoltas = ["Pilotos ", "Volta01", "Volta02", "Volta03", "Volta04", "Volta05", "Volta06", "Volta07", "Volta08", "Volta09", "Volta10"]
matriz = []

def insereVoltas():
    print("-"*95)
    for i in range(6):
        voltas = []
        for j in range(10):
            voltas.append(r.randint(100,200))
        matriz.append(voltas)
    imprimeVoltas()

def imprimeVoltas():
    for k in range(len(matriz[0])+1):
        print(f"{ContagemVoltas[k]}", end = "\t")
    print()
    print("-"*95)
    for l in range(len(matriz)):
        for m in range(len(matriz[0])):
            ContagemVoltas[m]
            if(m == 0):
                print(f"Corredor{l+1}", end = "\t")
            print(matriz[l][m], end = "\t")
        print()
    melhorTempo()

def melhorTempo():
    melhorTempo = min(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] <= melhorTempo:
                melhorTempo = matriz[i][j]
                corredor = i + 1
                volta = j + 1
    print("-"*95)
    print(f"Corredor{corredor} obteve o melhor tempo em sua {volta}° volta com o tempo de {melhorTempo} segundos")
    melhorMedia()

def melhorMedia():
    melhorVolta = []
    for i in range(len(matriz[0])):
        volta = 0
        for j in range(len(matriz)):
            volta += matriz[j][i]
        melhorVolta.append((volta/len(matriz)))
    print("-"*95)
    print(f"A {melhorVolta.index(min(melhorVolta))+1}º volta obteve a melhor média com o tempo médio de {min(melhorVolta):.2f} segundos")
    podio()

def podio():
    print("-"*95)
    print("Pódio")
    medias = []
    media = 0
    for i in range(len(matriz)):
        media = sum(matriz[i]) / len(matriz[i])
        medias.append(media)
    for j in range(len(matriz)):
        index = medias.index(min(medias))
        print(f"{j+1}º lugar ---> Corredor{index+1} com a média de {medias[index]:.2f} segundos")
        medias.pop(index)
    print("-"*95)

insereVoltas()

