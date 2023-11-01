
import ASSIS as a

op = "1"

while op != "2":
    print("===================== GRUPOS =====================")
    numeroAlunos = a.retornaNumero(True, False, "")
    primeiroGrupo = a.retornaNumero(False, False, "")
    a.retornaCombinacoes(numeroAlunos, primeiroGrupo)
    op = a.continuar()



