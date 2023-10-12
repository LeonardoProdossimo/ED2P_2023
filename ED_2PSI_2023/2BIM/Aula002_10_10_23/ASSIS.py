
# função para tratar erro quando o usuário digitar letras nos lugares que tem que ser números
def retornaNumero():
    try:
         num = input("Digite um número para o cálculo ---> ")
         return float(num)
    except ValueError: # formato errado
        print("="*38)
        print('Formato digitado inválido!')
        return retornaNumero()  # repetir a pergunta

def menu():
    print("================ MENU ================")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")
    print("5 - LIMPAR MEMÓRIA")
    print("6 - SAIR DO PROGRAMA")
    return input("OPÇÃO ---> ")

def somaNumero(memoria, num):
    print("================ SOMA ================")
    return memoria + num

def subNumero(memoria, num):
    print("============== SUBTRAÇÃO =============")
    return memoria - num

def multNumero(memoria, num):
    print("============ MULTIPLICAÇÃO ===========")
    return memoria * num

def divNumero(memoria, num):
    return memoria/num

def limpaMemoria():
    print("============ LIMPAR MEMÓRIA ==========")
    return 0

