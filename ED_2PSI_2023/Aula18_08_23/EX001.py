perguntas = ("Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","Já trabalhou com a vítima? ")
sim = 0
for i in range(len(perguntas)):
    resp = input(perguntas[i] + 'Sim ou Não')
    if resp.upper() == 'SIM':
        sim = sim+1
if sim == 2:
    print( 'Pessoa suspeita')
elif sim == 3 or sim == 4 :
    print( 'Cúmplice')
elif sim == 5:
    print( 'Assassino')
else: 
   print( 'Inocente')