nomes = []
idades = []
maiores = []
menores = []
qtd = 5
maiores = 0
for h in range(qtd):
    nomes.append(input(f'Digite o {h+1}º nome: '))
    idades.append(int(input(f'Digite sua idade {nomes[h]}: ')))
for i in range(len(nomes)):
    print(f"{nomes[i]}, {idades[i]} anos ")
for l in range(qtd):
    if(idades[l]>=18):
        maiores.append(nomes[l])
    else:
        menores.append(nomes[l])
print('--> são maiores de idade: ', end='')
for j in maiores:
    print(maiores[j], end = '')
print('--> são menores de idade: ', end='')
for j in maiores:
    print(menores[j], end = '')




