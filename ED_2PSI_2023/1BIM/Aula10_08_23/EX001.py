lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
print('-'*50)
#a)imprima o maior número
print(f'O número {max(lista)} é o maior número da lista!')
print('-'*50)

#b)impra o menor número
print(f'O número {max(lista)} é o menor número da lista!')
print('-'*50)

#c)imprima os números pares
lista2=[]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
       lista2.append(lista[i])
print(f'Estes são os números pares: {lista2}')
print('-'*50)

#d)imprima os números de ocorrências do primeiro elemento da lista
lista2.clear()
for i in range(len(lista)):
    if lista[i] == lista[0]:
        lista2.append(lista[i])
print(f'O primeiro elemento aparece {len(lista2)} vezes na lista!')
print('-'*50)

#e)imprima a média dos elementos
soma = 0
for i in range(len(lista)):
    num = soma + lista[i]
    soma = num
print(f'A média de todos os números da lista é: {soma/len(lista):.2f}')
print('-'*50)

#f)imprima a soma dos elementos de valor negativo 
soma = 0
for i in range(len(lista)):
    if lista[i] < 0:
        num = soma + lista[i]
        soma = num
print(f'A soma dos números negativos da listaresulta em: {soma}')
print('-'*50)