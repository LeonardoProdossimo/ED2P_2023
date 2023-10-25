"""
Presumi que a memória sempre sofrerá ação, por isso não criei opções de trocar o divisor ou subtração (memoria/num ou num/memoria)
"""
import ASSIS as a

memoria = 0
op = 0

if __name__ == '__main__':
    while op != 6:

        op = a.menu()
        if(op == "6"):
            print("SAINDO... ")
            break
        if(op != "5"):
            print("="*38)
            print(f"O estado atual da memória é {memoria}")
            print("="*38)
            num = a.retornaNumero()
            print(f"O número informado é {num}")
        
        if op == "1":
            operacao = a.somaNumero(memoria, num)

        elif op == "2":
            operacao = a.subNumero(memoria, num)

        elif op == "3":
            operacao = a.multNumero(memoria, num)

        elif op == "4":
            print("=============== DIVISÃO ==============")
            if(num == 0):
                print("Não é possivel dividir por 0")
                continue
            operacao = a.divNumero(memoria, num)

        elif op == "5":
            operacao = a.limpaMemoria()
            print(f"O estado atual da memória é 0")
            continue
        else:
            print("OPÇÃO INVÁLIDA! ")
            
        print(f"O resultado da operação: {operacao}")
        memoria = operacao