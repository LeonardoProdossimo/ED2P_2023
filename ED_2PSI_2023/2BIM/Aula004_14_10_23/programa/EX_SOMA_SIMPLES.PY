from funcoes import retornaNumero as r
from funcoes import somaSimples as s

try:
    with open('ED_2PSI_2023\\2BIM\\Aula004_14_10_23\\programa\\arquivoTxt\\entrada.txt', 'w') as txtFile:
        num1 = r()
        num2 = r()
        res = s(num1, num2)
        print(res)
        txtFile.write(f"\nEntrada: \n {str(num1)}\n {str(num2)}\n\n{str(res)}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

