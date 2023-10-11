nomes = []
qtd = 5
for i in range(qtd):
    nome = input(f'Digite o {i+1}º nome: ')
    nomes.append(nome)

for i in range(len(nomes)):
    print(f"Bem-vindo, {nomes[i].upper()} ")
