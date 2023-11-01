import ASSIS as a

listaNotas = []
op = "1"

while op != "2":
    print("===================== CALCULO DE MEDIA =====================")
    notas = a.retornaNotas(listaNotas)
    media = a.retornaMedia(notas)
    status = a.retornaStatus(media)
    print(f"A média para as notas inseridas é: {media:.2f}\n")
    listaNotas.clear()
    op = a.continuar()
