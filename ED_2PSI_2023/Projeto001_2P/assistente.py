from tabulate import tabulate #biblioteca que converte listas e dicionários para forma de tabela

#função para melhor exibir o estoque
def exibeProdutos(estoque, todos, disp, nDisp, cod):

    dados_formatados = []

    # Organize o dicionário em uma lista de listas, onde cada lista interna representa uma linha da tabela
    for codigo, produto in estoque.items():

        #verificações para saber qual tipo de dados exibir
        if(produto["disponivel"] == True):
            disponivel = "Disponível"
        else:
            disponivel = "Não disponível"
        if (todos):
                dados_formatados.append([codigo, produto["nome"], produto["quantidade"], produto['preco'], disponivel])
        elif (disp):
            if(produto["disponivel"] == True):
                dados_formatados.append([codigo, produto["nome"], produto["quantidade"], produto['preco'], disponivel])
        elif (nDisp):
            if(produto["disponivel"] == False):
                dados_formatados.append([codigo, produto["nome"], produto["quantidade"], produto['preco'], disponivel])
        else:
            if(codigo == cod):
                dados_formatados.append([cod, produto["nome"], produto["quantidade"], produto['preco'], disponivel])
    
    #criando tabela formatada no estilo GRID
    tabela = tabulate(dados_formatados, headers=["Código", "Nome", "Quantidade", "Preço (R$)", "Disponível"], tablefmt="grid")

    # retorno do resultado
    return print(tabela)


#função para perguntar se deseja continuar a tentar as opções
def continua():
    print("Deseja continuar?")
    print("1 - Sim")
    print("2 - Não")
    op = input("OPÇÃO ---> ")
    if(op == "1"):
        return "continuar" # repetir a pergunta
    elif (op == "2"):
        return "sair" #retorno para o sistema saber que o usuário não quer tentar outra vez
    else:
        print("Opção inválida!")
    return continua() 


# função para tratar erro quando o usuário digitar letras nos lugares que tem que ser números
def retorna_numero(tipoDados):
    tipo = tipoDados
    if(tipo == "quantidade"):
        num = input("Digite a quantidade --> ")
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
def retorna_codigo(estoque, cadastro):
    codigo = input("Digite o código do produto --->  ")

    if cadastro: #Se for na opção de cadastro de produto cai aqui
        if(codigo in estoque):
            print("="*50)
            print("Codigo já existente!")
            cont = continua()
            if(cont == "continuar"):
                return retorna_codigo(estoque, cadastro) # repetir a pergunta
            elif (cont == "sair"):
                return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
            
    else: #Se não for na opção de cadastro de produto cai aqui
        if codigo not in estoque:
            print("="*50)
            print("Codigo não encontrado!")
            cont = continua()
            if(cont == "continuar"):
                return retorna_codigo(estoque, cadastro) # repetir a pergunta
            elif (cont == "sair"):
                return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
    return codigo

#função para adicionar/remover estoque
def adic_remov_estoque(estoque, codigo, quant, adiciona):
    if(adiciona):
        estoque[codigo]["quantidade"] += quant
        if(quant > 0):
            estoque[codigo]["disponivel"] = True
        print("Adicionado com sucesso!")

    else:
        if((estoque[codigo]["quantidade"] - quant) < 0):
            return "sair"
        else:
            estoque[codigo]["quantidade"] -= quant
            if(quant == 0):
                estoque[codigo]["disponivel"] = False
        return "sucesso"


#função para aplicar porcentagem ou valor
def acrescimo_desconto(estoque, tipoOperacao):
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
            return acrescimo_desconto(estoque, tipoOperacao) # repetir a pergunta
        elif (op == "sair"):
            return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código
    novoValor = diferenciaTodos(estoque, sePorcentagem, valor, tipoOperacao)
    return novoValor


#função para escolher todos ou apenas um item da lista
def diferenciaTodos(estoque, sePorcentagem, valor, tipoOperacao):
    print("="*50)
    print("1 - APLICAR POR CODIGO")
    print("2 - APLICAR EM TODOS")
    op = input("OPÇÃO ---> ")
    if(op =="1"):
        todosValores = False
        codigo = retorna_codigo(estoque, False)
    elif(op == "2"):
        codigo = ""
        todosValores = True
    else:
        print("="*50)
        print('Opção inválida!')
        cont = continua()
        if(cont == "continuar"):
            return diferenciaTodos(estoque, tipoOperacao, valor)  # repetir a pergunta
        elif (cont == "sair"):
            return "sair" #retorno para o sistema saber que o usuário não quer tentar outro código

    if(tipoOperacao =="acrescimo"):
        novoValor = novoPreco(estoque, codigo, sePorcentagem, valor, "acrescimo", todosValores)
    else:
        novoValor = novoPreco(estoque, codigo, sePorcentagem, valor, "desconto", todosValores)
    return novoValor


#função para calcular o novo preco de acordo com os parâmetros
def novoPreco(estoque, codigo, sePorcentagem, valor, tipoOperacao, todosValores):
    porcen = ((valor/100)+1)
    if(todosValores):
        for prod in estoque:
            if(tipoOperacao == "acrescimo"):
                if(sePorcentagem):
                    estoque[prod]["preco"] *= porcen
                else:
                    estoque[prod]["preco"] += valor
            else:
                if(sePorcentagem):
                    estoque[prod]["preco"] -= (estoque[prod]["preco"] * (porcen - 1))
                else:
                    estoque[prod]["preco"] -= valor
    else:
        if(tipoOperacao == "acrescimo"):
            if(sePorcentagem):
                estoque[codigo]["preco"] *= porcen
            else:
                estoque[codigo]["preco"] += valor
        else:
            if(sePorcentagem):
                estoque[codigo]["preco"] -= (estoque[codigo]["preco"] * (porcen - 1))
            else:
                estoque[codigo]["preco"] -= valor
    return "sucesso"
