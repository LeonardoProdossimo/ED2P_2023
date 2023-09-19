import json
import assistente

estoque = {}
op = 1

#tenta carregar o arquivo e armazenar no dicionário se falhar exibe o print tratando o erro para não parar o programa
try:
    with open("C:\\projetos\\GitHub\\ED2P_2023\\ED_2PSI_2023\\Projeto001_2P\\base_dados\\estoque.json", "r") as json_file:
        estoque = json.load(json_file)
except:
    print("ARQUIVO NÃO EXISTE!")

while op != "9":
    print("===================== MENU =====================")
    print("1 - ADICIONAR PRODUTO")
    print("2 - CONSULTAR PRODUTO POR CODIGO")
    print("3 - CONSULTAR TODOS OS PRODUTOS")
    print("4 - EXCLUIR PRODUTO POR CODIGO")
    print("5 - ALTERAR PREÇO DO PRODUTO")
    print("6 - APLICAR ACRESCIMO/DESCONTO NOS PRODUTOS")
    print("7 - ADICIONAR ESTOQUE")
    print("8 - SALVAR")
    print("9 - SALVAR E SAIR")
    op = input("OPÇÃO ---> ")

    if(op == "1"):
        print("="*50)
        print("CADASTRO DE PRODUTOS")
        codigo = assistente.retorna_codigo(estoque, True)
        if(codigo == "sair"):
            continue
        nome = input("Digite o nome do produto -->  ")
        quant = assistente.retorna_numero("quantidade")
        preco  = assistente.retorna_numero("preco")
        if(quant > 0):
             disponivel = True
        else:
             disponivel = False
        estoque [codigo] = {"nome": nome,"quantidade": quant, "preco" : preco, "disponivel": disponivel}

    elif(op == "2"):
        print("="*50)
        print("CONSULTA POR CODIGO")
        codigo = assistente.retorna_codigo(False)
        if(codigo == "sair"):
            continue
        assistente.exibeProdutos(estoque, False, False, False, codigo)

    elif(op == "3"):
        print("="*50)
        print("CONSULTAR TODO ESTOQUE")
        print("1 - CONSULTAR TODO ESTOQUE")
        print("2 - CONSULTAR PRODUTOS DISPONIVEIS")
        print("3 - CONSULTAR PRODUTOS INDISPONIVEIS")
        op = input("OPÇÃO ---> ")
        if (op == "1"):
            print("="*50)
            assistente.exibeProdutos(estoque, True, False, False, "")
        elif (op =="2"):
            print("="*50)
            assistente.exibeProdutos(estoque, False, True, False, "")
        elif (op =="3"):
            print("="*50)
            assistente.exibeProdutos(estoque, False, False, True, "")
        else:
            print("Opção inválida!")

    elif(op == "4"):
        print("="*50)
        print("EXCLUIR REGISTRO")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        estoque.pop(codigo)
        print("Produto excluido com sucesso!")

    elif(op == "5"):
        print("="*50)
        print("ALTERAR PREÇO")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        novopreco = assistente.retorna_numero("preco")
        estoque [codigo]["preco"] = novopreco
        print("Preço alterado com sucesso!")

    elif(op == "6"):
        print("="*50)
        print("APLICAR DESCONTO OU ACRESCIMO")
        print("1 - ACRESCIMO")
        print("2 - DESCONTO")
        op = input("OPÇÃO ---> ")
        if(op == "1"):
            fim = assistente.acrescimo_desconto(estoque, "acrescimo")
            print("Atualizado com sucesso!")
        elif(op == "2"):
            fim = assistente.acrescimo_desconto(estoque, "desconto")
            print("Atualizado com sucesso!")
        else:
            print("Opção inválida!")

    elif(op == "7"):
        print("="*50)
        print("ADICIONAR ESTOQUE")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        quant = assistente.retorna_numero("quantidade")
        estoque[codigo]["quantidade"] = quant
        if(quant > 0):
            estoque[codigo]["disponivel"] = True
        print("Adicionado com sucesso!")

    elif(op == "8"):
        print("="*50)
        with open("C:\\projetos\\GitHub\\ED2P_2023\\ED_2PSI_2023\\Projeto001_2P\\base_dados\\estoque.json" , "w") as json_file:
            json.dump(estoque , json_file, indent = 4)
        print("Salvo com sucesso!")

    elif(op == "9"):
        print("="*50)
        print("SAINDO..")
        print("="*50)

    else:
        print("="*50)
        print("OPÇÃO INVÁLIDA!")

with open("C:\\projetos\\GitHub\\ED2P_2023\\ED_2PSI_2023\\Projeto001_2P\\base_dados\\estoque.json" , "w") as json_file:
            json.dump(estoque , json_file, indent = 4)