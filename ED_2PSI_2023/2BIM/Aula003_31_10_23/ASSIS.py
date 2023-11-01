import math as m

def retornaNumero(total, retornaNotas, i):
    try:
        if(retornaNotas):
            if( i != ""):
                num = input(f"Digite a {i+1}° nota ---> ")
                return float(num)
            else:
                num = input("Digite o número de notas que deseja calcular a média ---> ")
        else:
            if(total):
                num = input("Digite um número total de alunos ---> ")
            else:
                num = input("Digite um número de alunos no primeiro grupo ---> ")
        return int(num)
    except ValueError:
        print("="*38)
        print('Formato digitado inválido!')
        return retornaNumero(total, retornaNotas, i)
    
def continuar():
    print("Deseja continuar?")
    print("1 - Sim")
    print("2 - Não")
    op = input("OPÇÃO ---> ")
    if(op == "1"):
        return "1"
    elif (op == "2"):
        return "2"
    else:
        print("Opção inválida!")
    return continuar() 

def retornaCombinacoes(numeroAlunos, primeiroGrupo):
    segundoGrupo = numeroAlunos-primeiroGrupo
    comb = m.factorial(numeroAlunos)/(m.factorial(primeiroGrupo) * m.factorial((segundoGrupo)))
    print()
    return print(f"O primeiro grupo ficará com {primeiroGrupo} "+
                    f"alunos e o segundo ficará com {segundoGrupo} alunos.\n"+
                    f"O número de combinações de grupos possiveis para estes números é de {int(comb)}\n")

def retornaNotas(listaNotas):
    num = retornaNumero(False, True, "")
    for i in range(num):
        nota = retornaNumero(False,True, i)
        listaNotas.append(nota)
    return listaNotas

def retornaMedia(listaNotas):
    soma = 0
    for nota in listaNotas:
        soma += nota
    return soma/len(listaNotas)

def retornaStatus(media):
    if(media > 6):
        return print("\nEste aluno está APROVADO\n")
    elif(media >= 4 or media <= 6 ):
        return print("\nEste aluno está em VERIFICAÇÃO SUPLEMENTAR\n")
    else:
        return print("\nEste aluno está em REPROVADO\n")