import json
import os

estoque = {}
op = 1
try:
    with open("C:\\projetos\\GitHub\\ED2P_2023\\ED_2PSI_2023\\Aula05_09_23\\base_dados\\estoque.json", "r") as json_file:
        estoque = json.load(json_file)
except:
    print("ARQUIVO NÃO EXISTE!")

while int(op) !=4:
    print("======== MENU ========")
    print("1 - ADICIONAR")
    print("2 - CONSULTAR POR CODIGO")
    print("3 - CONSULTAR TODOS")
    print("4 - SAIR")
    op = input("OPÇÃO ---> ")
    if(int(op) == 1):
        print("="*20)
        print("CADASTRO DE PRODUTOS")
        codigo = input("Digite o código do produto --->  ")
        nome = input("Digite o nome do produto -->  ")
        preco = float(input("Digite o preço por quilo/unidade --->  "))
        estoque [codigo] = {"nome": nome, "preco" : preco}
        with open("C:\\projetos\\GitHub\\ED2P_2023\\ED_2PSI_2023\\Aula05_09_23\\base_dados\\estoque.json" , "w") as json_file:
            json.dump(estoque , json_file, indent = 4)

    elif(int(op) == 2):
        pass
    elif(int(op) == 3):
        pass
    elif(int(op) == 4):
        print("SAINDO .. ")
    else:
        print("="*20)
        print("OPÇÃO INVÁLIDA!")