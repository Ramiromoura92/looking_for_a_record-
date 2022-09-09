import json
from tokenize import String

def busca_nome():

    with open("cadastro.txt",'rb') as f:
        content = f.read()
    
    dict = json.loads(content)
    
    alunos = dict["aluno"]
    while True:

        nome = str(input("Informe o nome: "))

        for cadastro in alunos:        
            if cadastro['nome'] == nome:
                print(cadastro)

busca_nome()