import random as rnd
def calcula_media(v): # v é uma variavel local - só existe dentro da funçao 
    if len(v) > 0:
        return sum(v)/len(v)
    else:
        return 0
    
def inicializa_list(quantidade=5):
    lista = []
    for _ in range(quantidade):
        valor = rnd.randint(0,100)
        lista.append(valor)
    return lista

def menu():
    print('='*20)
    print("=====MENU=====")
    print('1- INICIAR LISTA ALEATÓRIA')
    print('2- CALCULAR MÉDIA')
    print('3- PESQUISAR VALOR')
    print('4- SAIR')
    return int(input('Digite sua opção-->  '))

def verificaValor(valor):
    if(valor in v):
        return print(f"O valor {valor} existe dentro da lista!")
    else:
        return print(f"O valor {valor} não existe dentro da lista!")
    
#main
if __name__ == '__main__':
    v= []
    op = 0
    while op != 4:
        op = menu()
        if op == 1:
            v =inicializa_list(8)
            print(v)
        elif op == 2:
            media = calcula_media(v)
            print(f'A média é: {media:.2f}')
        elif op == 3:
            valor = int(input("Digite o valor que deseja verificar---> "))
            verificaValor(valor)
    else:
        print('SAINDO...')
