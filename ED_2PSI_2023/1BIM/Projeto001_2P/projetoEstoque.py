import json
import assistente

estoque = {}
op = 1

#tenta carregar o arquivo e armazenar no dicionário se falhar ou não existir exibe o print tratando o erro para não parar o programa
try:
    with open("ED_2PSI_2023\\Projeto001_2P\\base_dados\\estoque.json", "r") as json_file:
        estoque = json.load(json_file)
except:
    print("ARQUIVO NÃO EXISTE!")


#programa no terminal
while op != "0":
    print("====================== MENU ======================")
    print("1 - ADICIONAR PRODUTO")
    print("2 - CONSULTAR PRODUTO POR CODIGO")
    print("3 - CONSULTAR TODOS OS PRODUTOS")
    print("4 - EXCLUIR PRODUTO POR CODIGO")
    print("5 - ALTERAR PREÇO DO PRODUTO")
    print("6 - APLICAR ACRESCIMO/DESCONTO NOS PRODUTOS")
    print("7 - ADICIONAR ESTOQUE")
    print("8 - REMOVER ESTOQUE")
    print("9 - SALVAR")
    print("0 - SALVAR E SAIR")
    op = input("OPÇÃO ---> ")

    if(op == "1"):
        print("="*50)
        print("============== CADASTRO DE PRODUTOS ==============")
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
        print("============== CONSULTA POR CODIGO ===============")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        assistente.exibeProdutos(estoque, False, False, codigo)

    elif(op == "3"):
        print("="*50)
        print("============= CONSULTAR TODO ESTOQUE =============")
        print("1 - CONSULTAR TODO ESTOQUE")
        print("2 - CONSULTAR PRODUTOS DISPONIVEIS")
        print("3 - CONSULTAR PRODUTOS INDISPONIVEIS")
        op = input("OPÇÃO ---> ")
        if (op == "1"):
            print("="*50)
            assistente.exibeProdutos(estoque, True, False, "")
        elif (op =="2"):
            print("="*50)
            assistente.exibeProdutos(estoque, False, True, "")
        elif (op =="3"):
            print("="*50)
            assistente.exibeProdutos(estoque, False, False, "")
        else:
            print("Opção inválida!")

    elif(op == "4"):
        print("="*50)
        print("================ EXCLUIR REGISTRO ================")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        prod = estoque[codigo]["nome"]
        print(f"Deseja realmente excluir o produto {prod.upper()} permanentemente?")
        print("1 - Sim")
        print("2 - Não")
        op = input("OPÇÃO ---> ")
        if(op == "1"):
            estoque.pop(codigo)
            print("Produto excluido com sucesso!")
        else:
            print("Operação cancelada!")
            continue

    elif(op == "5"):
        print("="*50)
        print("================= ALTERAR PREÇO ==================")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        novopreco = assistente.retorna_numero("preco")
        estoque [codigo]["preco"] = novopreco
        print("Preço alterado com sucesso!")

    elif(op == "6"):
        print("="*50)
        print("========= APLICAR DESCONTO OU ACRESCIMO ==========")
        print("1 - ACRESCIMO")
        print("2 - DESCONTO")
        op = input("OPÇÃO ---> ")
        if(op == "1"):
            fim = assistente.acrescimo_desconto(estoque, "acrescimo")
            if(fim == "sair"):
                continue
            print("Atualizado com sucesso!")
        elif(op == "2"):
            fim = assistente.acrescimo_desconto(estoque, "desconto")
            if(fim == "sair"):
                continue
            print("="*50)
            print("Atualizado com sucesso!")
        else:
            print("Opção inválida!")

    elif(op == "7"):
        print("="*50)
        print("=============== ADICIONAR ESTOQUE ================")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        quant = assistente.retorna_numero("quantidade")
        assistente.adic_remov_estoque(estoque, codigo, quant, True)
        
    elif(op == "8"):
        print("="*50)
        print("================ REMOVER ESTOQUE =================")
        codigo = assistente.retorna_codigo(estoque, False)
        if(codigo == "sair"):
            continue
        prod = estoque[codigo]["nome"]
        quant = assistente.retorna_numero("quantidade")
        corrigeEstoque = assistente.adic_remov_estoque(estoque, codigo, quant, False)
        if(corrigeEstoque == "sucesso"):
            print("="*50)
            print("Estoque corrigido com sucesso!")
        else:
            print("="*50)
            print(f"Saldo no estoque insuficiente para remover, você tem {int(corrigeEstoque)} unidades do produto {prod.upper()}!" 
                   "\nTente novamente!")

    elif(op == "9"):
        print("="*50)
        with open("ED_2PSI_2023\\Projeto001_2P\\base_dados\\estoque.json" , "w") as json_file:
            json.dump(estoque , json_file, indent = 4)
        print("Salvo com sucesso!")

    elif(op == "0"):
        print("="*50)
        print("SAINDO..")
        print("="*50)

    else:
        print("="*50)
        print("OPÇÃO INVÁLIDA!")


with open("ED_2PSI_2023\\Projeto001_2P\\base_dados\\estoque.json" , "w") as json_file:
            json.dump(estoque , json_file, indent = 4)