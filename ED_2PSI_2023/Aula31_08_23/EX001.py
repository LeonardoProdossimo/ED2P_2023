import json

regs01 = {"Nome":"Fulano","Idade": 10,"Matriculado": True}

regs02 = {"Nome":"Baeltrana","Idade": 12,"Matriculado": False}

dados = {"alunos":[regs01,regs02]}


jason_str = json.dumps(dados)
print(dados)
print(jason_str)


with open('teste.json', 'w') as file_Json:
    json.dump(dados, file_Json) 