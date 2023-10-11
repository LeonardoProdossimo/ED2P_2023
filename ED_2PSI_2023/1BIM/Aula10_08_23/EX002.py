#2Fça um vetor que preencha 10 posições e conte quantos valores diferentes existem no vetor
print('-'*50)
vetor = []
lista2 = []
print('Digite 10 números')
for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    vetor.append(num)
for num in vetor:
    if vetor.count(num) == 1:
        lista2.append(num)
print(f'Existem {len(lista2)} números diferentes na lista')
