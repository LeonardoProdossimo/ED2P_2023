"""
Vamos supor que precisamos criar um programa para cadastrar alunos em uma escola, armazenando informações como nome, idade e nota. Podemos utilizar um dicionário para representar cada aluno, onde a chave será o número de matrícula e o valor será outro dicionário contendo as informações do aluno.

"""

alunos = {}

op = 1
while op != 3:
    print('='*10)
    print('===MENU===')
    print('1 - Adicionar Aluno')
    print('2 - Consultar Aluno')
    print('3 - Sair')
    op = int(input('Digite a opção--> '))
    if (op == 1):
        codigoMatricula = input('Número da matricula: ')
        nome = input('Nome do aluno: ')
        idade = int(input('Idade do aluno: '))
        nota = float(input('Nota do aluno: '))
        aluno = {'Nome': nome, 'Idade': idade, 'Nota': nota}
        alunos [codigoMatricula] = aluno
    elif (op == 2):
        codigo = input('Código do aluno: ')
        if codigo not in alunos:
            print('='*10)
            print('Código inválido!')
        else:
            print('='*10)
            print(alunos[codigo])
    elif (op == 3):
        print('Saindo..')
    else:
        print('Opção inválida!')