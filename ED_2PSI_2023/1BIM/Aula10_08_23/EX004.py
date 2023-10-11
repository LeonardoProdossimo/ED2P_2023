#4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.
import random
print('-'*50)
lista2 =[]
for i in range(50):
    num = random.randint(6)
    if num == 6:
        lista2.append(num)
print(f'O número de ocorrências do número 6 é de: {len(lista2)}')
