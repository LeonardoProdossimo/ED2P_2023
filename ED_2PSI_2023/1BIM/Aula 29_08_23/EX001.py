estoque = {}

op = 1
while op != 3:
    print('='*10)
    print('===MENU===')
    print('1 - Adicionar')
    print('2 - Consultar')
    print('3 - Sair')
    op = int(input('Digite a opção--> '))
    if (op == 1):
        codigo = input('Código: ')
        nome = input('Nome: ')
        estoque[codigo] = nome
        print('Adicionado com sucesso!')
    elif (op == 2):
        codigo = input('Código desejado: ')
        if codigo not in estoque:
            print('Código inválido!')
        else:
            print(estoque[codigo])
    elif (op == 3):
        print('Saindo..')








        