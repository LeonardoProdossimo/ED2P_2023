import json
from tabulate import tabulate

estoque = {}
op = 1

def adiciona_estoque(cod, quant):
    for codigo in estoque:
        if cod == codigo:
            estoque[codigo]["quantidade"] = quant
            if(quant > 0):
                estoque[codigo]["disponivel"] == True
            break
    return "sucesso"

def exibeProdutos(todos, disp, nDisp, cod):
    dados_formatados = []

    # Organize o dicionário em uma lista de listas, onde cada lista interna representa uma linha da tabela
    for codigo, produto in estoque.items():
        preco_formatado = "{:.2f}".format(produto["preco"])
        if(produto["disponivel"] == True):
            disponivel = "Disponivel"
        else:
            disponivel = "Não disponivel"
        if (todos):
                dados_formatados.append([codigo, produto["nome"], produto["quantidade"], preco_formatado, disponivel])
        elif (disp):
            if(produto["disponivel"] == True):
                dados_formatados.append([codigo, produto["nome"], produto["quantidade"], preco_formatado, disponivel])
        elif (nDisp):
            if(produto["disponivel"] == False):
                dados_formatados.append([codigo, produto["nome"], produto["quantidade"], preco_formatado, disponivel])
        else:
            if(codigo == cod):
                dados_formatados.append([cod, produto["nome"], produto["quantidade"], preco_formatado, disponivel])
    
        # Use o tabulate para criar a tabela formatada
    tabela = tabulate(dados_formatados, headers=["Código", "Nome", "Quantidade", "Preço", "Disponível"], tablefmt="grid")

    # Exibe a tabela no prompt
    return print(tabela)

#funçã para perguntar se deseja continuar a tentar 
def continua():
    print("Deseja continuar?")
    print("1 - Sim")
    print("2 - Não")
    op = input("OPÇÃO ---> ")
    if(op == "1"):
        return "continuar" # repetir a pergunta
    elif (op == "2"):
        return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
    else:
        print("Opção inválida!")
    return continua() 


# função para tratar erro de formato de dados
def retorna_numero(tipoDados):
    tipo = tipoDados
    if(tipo == "quantidade"):
        num = input("Digite a quantidade a ser cadastrada --> ")
    elif(tipo == "preco"):
        num = input("Digite o preço por quilo/unidade --->  ")
    elif(tipo == "porcentagem"):
        num = input("Digite a porcentagem que deseja aplicar --->  ")
    else:
        num = input("Digite o valor que deseja aplicar --->  ")

    try:
        num = float(num)
        if (num < 0):
            print("="*50)
            print("Digite um número que não seja negativo!")
            return retorna_numero(tipo)
        else:
            return num
    except ValueError: # formato errado
        print("="*50)
        print('Formato digitado inválido!')
        cont = continua()
        if(cont == "continuar"):
            return retorna_numero(tipo)  # repetir a pergunta
        elif (cont == 'sair'):
            return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
        return retorna_numero(tipo) # repetir a pergunta

#função para tratar ambiguidade no código
def retorna_codigo(cadastro):
    codigo = input("Digite o código do produto --->  ")

    if cadastro: #Se for na opção de cadastro de produto cai aqui
        if(codigo in estoque):
            print("Codigo já existente!")
            cont = continua()
            if(cont == "continuar"):
                return retorna_codigo(cadastro) # repetir a pergunta
            elif (cont == "sair"):
                return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
            
    else: #Se não for na opção de cadastro de produto cai aqui
        if codigo not in estoque:
            print("Codigo não encontrado!")
            cont = continua()
            if(cont == "continuar"):
                return retorna_codigo(cadastro) # repetir a pergunta
            elif (cont == "sair"):
                return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
            
    return codigo

#função para aplicar porcentagem ou valor
def acrescimo_desconto(tipoOperacao):
    print("="*50)
    print("1 - APLICAR POR PORCENTAGEM")
    print("2 - APLICAR VALOR ")
    op = input("OPÇÃO ---> ")
    if(op =="1"):
        valor = retorna_numero("porcentagem")
        sePorcentagem = True
    elif(op == "2"):
        valor = retorna_numero("valor")
        sePorcentagem = False
    else:
        cont = continua()
        if(cont == "continuar"):
            return acrescimo_desconto(tipoOperacao) # repetir a pergunta
        elif (op == "sair"):
            return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
    novoValor = diferenciaTodos(sePorcentagem, valor, tipoOperacao)
    return novoValor

#função para escolher todos ou apenas um item da lista
def diferenciaTodos(sePorcentagem, valor, tipoOperacao):
    print("="*50)
    print("1 - APLICAR POR CODIGO")
    print("2 - APLICAR EM TODOS")
    op = input("OPÇÃO ---> ")
    if(op =="1"):
        todosValores = False
        codigo = retorna_codigo(False)
    elif(op == "2"):
        codigo = ""
        todosValores = True
    else:
        print("="*50)
        print('Opção inválida!')
        cont = continua()
        if(cont == "continuar"):
            return diferenciaTodos(tipoOperacao, valor)  # repetir a pergunta
        elif (cont == "sair"):
            return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código

    if(tipoOperacao =="acrescimo"):
        novoValor = novoPreco(codigo, sePorcentagem, valor, "acrescimo", todosValores)
    else:
        novoValor = novoPreco(codigo, sePorcentagem, valor, "desconto", todosValores)
    return novoValor

#para calcular o novo preco de acordo com os parâmetros
def novoPreco(codigo, sePorcentagem, valor, tipoOperacao, todosValores):
    porcen = ((valor/100)+1)
    if(todosValores):
        for prod in estoque:
            if(tipoOperacao == "acrescimo"):
                if(sePorcentagem):
                    estoque[prod]["preco"] = estoque[prod]["preco"] * porcen
                else:
                    estoque[prod]["preco"] =  estoque[prod]["preco"] + valor
            else:
                if(sePorcentagem):
                    estoque[prod]["preco"] = (estoque[prod]["preco"] * (porcen - 1)) - estoque[prod]["preco"]
                else:
                    estoque[prod]["preco"] = estoque[prod]["preco"] - valor
    else:
        if(tipoOperacao == "acrescimo"):
            if(sePorcentagem):
                estoque[codigo]["preco"] = estoque[codigo]["preco"] * porcen
            else:
                estoque[codigo]["preco"] = estoque[codigo]["preco"] + valor
        else:
            if(sePorcentagem):
                estoque[codigo]["preco"] = (estoque[codigo]["preco"] * (porcen - 1)) + estoque[codigo]["preco"]
            else:
                estoque[codigo]["preco"] = estoque[codigo]["preco"] - valor
    return "sucesso"

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
        codigo = retorna_codigo(True)
        if(codigo == "sair"):
            continue
        nome = input("Digite o nome do produto -->  ")
        quant = retorna_numero("quantidade")
        preco  = retorna_numero("preco")
        if(quant > 0):
             disponivel = True
        else:
             disponivel = False
        estoque [codigo] = {"nome": nome,"quantidade": quant, "preco" : preco, "disponivel": disponivel}
    elif(op == "2"):
        print("="*50)
        print("CONSULTA POR CODIGO")
        codigo = retorna_codigo(False)
        if(codigo == "sair"):
            continue
        exibeProdutos(False, False, False, codigo)

    elif(op == "3"):
        print("="*50)
        print("CONSULTAR TODO ESTOQUE")
        print("1 - CONSULTAR TODO ESTOQUE")
        print("2 - CONSULTAR PRODUTOS DISPONIVEIS")
        print("3 - CONSULTAR PRODUTOS INDISPONIVEIS")
        op = input("OPÇÃO ---> ")
        if (op == "1"):
            print("="*50)
            exibeProdutos(True, False, False, "")
        elif (op =="2"):
            print("="*50)
            exibeProdutos(False, True, False, "")
        elif (op =="3"):
            print("="*50)
            exibeProdutos(False, False, True, "")
        else:
            print("Opção inválida!")
            continue

    elif(op == "4"):
        print("="*50)
        print("EXCLUIR REGISTRO")
        codigo = retorna_codigo(False)
        if(codigo == "sair"):
            continue
        estoque.pop(codigo)
        print("Produto excluido com sucesso!")

    elif(op == "5"):
        print("="*50)
        print("ALTERAR PREÇO")
        codigo = retorna_codigo(False)
        if(codigo == "sair"):
            continue
        novopreco = retorna_numero("preco")
        estoque [codigo]["preco"] = novopreco
        print("Preço alterado com sucesso!")

    elif(op == "6"):
        print("="*50)
        print("APLICAR DESCONTO OU ACRESCIMO")
        print("1 - ACRESCIMO")
        print("2 - DESCONTO")
        op = input("OPÇÃO ---> ")
        if(op == "1"):
            fim = acrescimo_desconto("acrescimo")
            print("Atualizado com sucesso!")
        elif(op == "2"):
            fim = acrescimo_desconto("desconto")
            print("Atualizado com sucesso!")
        else:
            print("Opção inválida!")
            continue
    elif(op == "7"):
        print("="*50)
        print("ADICIONAR ESTOQUE")
        codigo = retorna_codigo(False)
        if(codigo == "sair"):
            continue
        quant = retorna_numero("quantidade")
        adiciona_estoque(codigo, quant)

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