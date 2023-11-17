def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0) # posicionando cursor no inicio
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor =  float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("ED_2PSI_2023\\2BIM\\Aula004_14_10_23\\programa\\entrada.txt")
    return sum(valores)

# EXERCICIOS 16/11/2023 
def maior_valor_arquivo():
    maior = leitura("ED_2PSI_2023\\2BIM\\Aula004_14_10_23\\programa\\entrada.txt")
    return max(maior)
    
def multiplica_valores_arquivo():
    maior = leitura("ED_2PSI_2023\\2BIM\\Aula004_14_10_23\\programa\\entrada.txt")
    mult = 1
    for valor in maior:
        mult *= valor
    return mult

if __name__ == '__main__':
    resultado = soma_valores_arquivo()
    maior = maior_valor_arquivo()
    mult = multiplica_valores_arquivo()
    print("="*50)
    print("SOMA")
    print(resultado)
    print("="*50)
    print("MAIOR DA LISTA")
    print(maior)
    print("="*50)
    print("MULTIPLICAÇÃO")
    print(mult)
