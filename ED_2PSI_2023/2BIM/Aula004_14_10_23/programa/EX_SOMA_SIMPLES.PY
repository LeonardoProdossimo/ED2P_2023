from funcoes import retornaNumero
from funcoes import somaSimples

try:
    with open('2BIM\\Aula004_14_10_23\\programa\\arquivoTxt\\entrada.txt', 'w') as txtFile:
        num1 = retornaNumero()
        num2 = retornaNumero()
        res = somaSimples(num1, num2)
        print(res)
        txtFile.write(f"\nEntrada: \n {str(num1)}\n {str(num2)}\n\n{str(res)}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

