#3- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) aparece pela primeira vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1
print('-'*50)
lista2 =[]
print('Digite 5 números')
for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    lista2.append(num)
num2 = int(input(f'Digite um número para ver se consta na lista: '))
if num2 in lista2:
   print(f'O número esta na posição {lista2.index(num2)} da lista')
else:
    print('-1')