def retornaNumero():
    try:
        num = input(f"Digite um número para soma ---> ")
        return float(num)
    except ValueError:
        print("="*38)
        print('Formato digitado inválido!')
        return retornaNumero()
    
def somaSimples(num1:float, num2:float):
    return F"Saida:\n SOMA = {num1+num2}"