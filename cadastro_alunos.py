import json

def cadastrar_alunos():

    dict = {}
    contador = 3
    for cont in range(contador):
        #print(cont)
        
        nome = input("Informe o nome: ")
        email = input("Informe seu melhor email: ")
        curso = input("Informe o curso desejado: ")
        if cont == 0:
            dict["aluno"] = [{"nome": nome, "email": email, "curso": curso}]
        else:
            dict["aluno"].append({"nome": nome, "email": email, "curso": curso})
    print(dict)
    arquivo = open("cadastro.txt","w")
    arquivo.write(json.dumps(dict))
    arquivo.close()

cadastrar_alunos()

