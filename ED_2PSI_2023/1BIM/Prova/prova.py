import json

funcionarios = {}

listaOrdem = []
listaMenorIdade = []
listaMaiorIdade = []
listaMenorSalario = []
listaMaiorSalario = []

try:
    with open("Prova\\dados_prova.json", "r") as json_file:
        funcionarios = json.load(json_file)
except:
    print("ARQUIVO NÃO EXISTE!")


def fucionariosOrdemAlfabetica():
    print("====Nomes em ordem alfabética====")
    for chave in funcionarios:
        listaOrdem.append(funcionarios[chave]["nome"])
    for nome in sorted(listaOrdem):
        print(f"Nome: {nome}, ")

def funcionarioMaisVelho():
    print("====Funcionários com mais idade====")
    for chave in funcionarios:
        listaMaiorIdade.append(funcionarios[chave]["idade"])
    for chave in funcionarios:
        if(funcionarios[chave]["idade"] == max(listaMaiorIdade)):
            nome = funcionarios[chave]["nome"]
            idade = funcionarios[chave]["idade"]
            salario = funcionarios[chave]["salario"]
            
            print(f"CPF: {chave}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Salario: {salario}")
            print("="*50)

def funcionarioMaisNovo():
    print("====Funcionários com menos idade====")
    for chave in funcionarios:
        listaMenorIdade.append(funcionarios[chave]["idade"])
    for chave in funcionarios:
        if(funcionarios[chave]["idade"] == min(listaMenorIdade)):
            nome = funcionarios[chave]["nome"]
            idade = funcionarios[chave]["idade"]
            salario = funcionarios[chave]["salario"]
            
            print(f"CPF: {chave}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Salario: {salario}")
            print("="*50)

def funcionarioMaisRico():
    print("====Maior Salário====")
    for chave in funcionarios:
        listaMaiorSalario.append(funcionarios[chave]["salario"])
    for chave in funcionarios:
        if(funcionarios[chave]["salario"] == max(listaMaiorSalario)):
            nome = funcionarios[chave]["nome"]
            idade = funcionarios[chave]["idade"]
            salario = funcionarios[chave]["salario"]
            
            print(f"CPF: {chave}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Salario: {salario}")
            print("="*50)

def funcionarioMaisPobre():
    print("====Menor Salário====")
    for chave in funcionarios:
        listaMenorSalario.append(funcionarios[chave]["salario"])
    for chave in funcionarios:
        if(funcionarios[chave]["salario"] == min(listaMenorSalario)):
            nome = funcionarios[chave]["nome"]
            idade = funcionarios[chave]["idade"]
            salario = funcionarios[chave]["salario"]
            print(f"CPF: {chave}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Salario: {salario}")
            print("="*50)


fucionariosOrdemAlfabetica()
print("="*50)
funcionarioMaisVelho()
print("="*50)
funcionarioMaisNovo()
print("="*50)
funcionarioMaisRico()
print("="*50)
funcionarioMaisPobre()
