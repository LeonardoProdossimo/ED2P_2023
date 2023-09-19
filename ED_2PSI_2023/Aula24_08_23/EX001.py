opcao = 1
bd_estoque = [] 
while opcao != 4:
    print('='*10)
    print("1- Adicionar")
    print('2- Consultar estoque')
    print('3- Consultar Valor Total do Estoque')
    print('4- Sair')
    opcao = int(input('Opcao >>>> '))
    if opcao == 1:
        print('-----Adicionar produto-----')
        codigo = int(input('Codigo: '))
        nome = input('Nome: ')
        descricao = input('Descricao: ')
        qtd = int(input("Quantidade: "))
        preco = float(input('Preco: R$ '))
        produto = [codigo, nome, descricao, preco, qtd]
        bd_estoque.append(produto)
        print('-----Adicionado com sucesso-----')
    elif opcao == 2:
        print('-----Estoque-----')
        print('Codigo\tNome\tDescricao\tQuant\tPreco')
        for prod in bd_estoque:
            print(prod[0],end='\t')
            print(prod[1],end='\t')
            print(prod[2],end='\t')
            print(prod[4],end='\t')
            print(prod[3])
        print('-----Fim estoque-----')
    elif opcao == 3:
        soma = 0
        for prod in bd_estoque:
            soma += (prod[3] * prod [4])
        print(f"O valor total do estoque é R$ {soma:.2f}")
    elif opcao == 4:
        print('saindo....')
    else:
        print('opcao incorreta')