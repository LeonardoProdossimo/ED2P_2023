notas = []
soma = 0
for i in range(10):
    i+=1
    print("Escreva 10 notas")
    nota = float(input(f"Digite a nota número {i}: "))
    notas.append(nota)
    soma += nota
media = soma / len(notas)
print(media)