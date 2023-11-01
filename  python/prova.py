#vitotoso
import csv
import datetime

livros = []
pessoas = []
emprestimos = []

def cadastrar_livro(livros):
    livro=input("Digite o nome do livro:  ")
    editora=input("Digite o nome da editora:  ")
    autor=input("Digite o nome do autor:  ")

    livro={
        'Titulo':livro,
        'Editora':editora,
        'Autor':autor  
    }
    livros.append(livro)
    criar_livro_csv()
    print("LIVRO CADASTRADO COM SUCESSO!!")
    print("====================================")
    
def cadastrar_pessoa(pessoas):
    nome=input("Digite o nome da Pessoa:  ")
    telefone=input("Digite o telefone da pessoa:  ")
    email=input("Digite o email da pessoa:  ")
    
    pessoa={
        'Nome':nome,
        'Telefone':telefone,
        'Email':email
    }
    pessoas.append(pessoa)
    criar_pessoa_csv()
    print("PESSOA CADASTRADA COM SUCESSO!!!")
    print("=====================================")

def Cadastrar_emprestimos(emprestimos):
    
    procurar_livro=input("Qual o nome do livro que vc deseja fazer o emprestimo:  ")
    procurar_pessoa=input("Qual o email da pessoa que vai pegar o livro:  ")
    dia=int(input("Dia do mes de vencimento:  "))
    mes=int(input("Mes de vencimento:  "))
    ano=int(input("Ano de vencimento:  "))
    
    for livro in livros:
        if procurar_livro == livro['Titulo']:
            
            procurar_livro=livro['Nomelvr']
        else:
            print("Esse Livro nao existe.")
            
    for pessoa in pessoas:
        if procurar_pessoa == pessoa['Email']:
            
            procurar_pessoa=pessoa['Email']
        
        else:
            
            print("Essa pessoa nao existe.")
            
    emprestimo={
        
        'Pessoa':procurar_pessoa,
        'Livro':procurar_livro,
        'Data':datetime(ano,mes,dia) 
    }
    emprestimos.append(emprestimo)
    criar_emprestimo_csv()
    print("Emprestimo cadastrado com sucesso.")
    
def main():
    
    livros = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    pessoas = csv.DictReader(open('arquivo_pessoas.csv', mode="r"))
    emprestimos = csv.DictReader(open('arquivo_emprestimos.csv', mode="r"))
#DaNasser
def criar_livro_csv():
    gravador = csv.writer(open('arquivo_livros.csv', mode="w", newline='')) 
    gravador.writerow(["livro","Editora","Autor"])
    
    for livro in livros:
            
            gravador.writerow([livro['Titulo'],livro['Editora'],livro['Autor'],])
    
def criar_pessoa_csv():
      gravador1 = csv.writer(open('arquivo_pessoas.csv', mode="w", newline=''))
      gravador1.writerrow(["Nome","Telefone","Email"])

      for pessoa in pessoas:

        gravador1.writerrow([pessoa['Nome'],pessoa['Telefone'],pessoa['Email']])

def criar_emprestimo_csv():
    gravador2 = csv.writer(open('arquivo_emprestimos.csv', mode="w", newline=''))
    gravador2.writerrol(["Pessoa","Livro","Data"])

    for emprestimo in emprestimos:
          
        gravador2.writerrow(emprestimo['Pessoa'],emprestimo['Livro'],emprestimo['Entega'])


def deletar_livro(livros):
    pesquisa = input("digite o nome do livro: ")
    for livro in livros:
        if livro['livro'] == pesquisa:
            livros.remove(livro)
        else:
                print("Livro não encontrado!")
    criar_livro_csv()

def deletar_pessoa(pessoas):
    pesquisa1 = input("Digite o seu email: ")
    for pessoa in pessoas:
        if pessoa['Email'] == pesquisa1:
              pessoas.remove(pessoa)
        else:
             print("Pessoa não encontrada!")
    criar_pessoa_csv()
        
def deletar_emprestimo(emprestimos):
    pesquisa2 = input("Digite o nome do livro: ")
    for emprestimo in emprestimos:
        if emprestimo['Livro'] == pesquisa2:
            emprestimos.remove[emprestimo]
        else:
             print("Emprestimo não encontrado!")
    criar_emprestimo_csv()

#Githug-o
def editar_livros():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editlivro = input("Digite o nome do livro que deseja editar: ")

    for livro in leitor:
        if livro['Titulo'] == editlivro:
            livro['Titulo'] = input("Título: ")
            livro['Editora'] = input("Editora: ")
            livro['Autor'] = input("Autor: ")
        else:
            print("Livro não encontrado.")
    livros = leitor
    criar_livro_csv()

def editar_contatos():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editcontato = input("Digite o email do contato que deseja editar: ")

    for contato in leitor:
        if contato['Email'] == editcontato:
            contato['Nome'] = input("Nome: ")
            contato['Telefone'] = input("Telefone: ")
            contato['Email'] = input("Email: ")
        else:
            print("Livro não encontrado.")
    contatos = leitor
    criar_contato_csv()

def editar_emprestimos():
    leitor = csv.DictReader(open('arquivo_livros.csv', mode="r"))
    editemprestimo = input("Digite o nome do livro emprestado que deseja alterar: ")
    opc1 = int(input("Qual informação deseja alterar?\n1 - Pessoa;\n2 - Livro;\n3 - Entrega;\n4 - Todas.\n")) 

    for emprestimo in leitor:
        if emprestimo['Livro'] == editemprestimo:
            if opc1 == 1:
                emprestimo['Nome'] = input("Nome: ")
            elif opc1 == 2:
                emprestimo['Livro'] = input("Livro: ") 
            elif opc1 == 3: 
                dia = int(input("Digite o dia a previsão de devolução (dd): "))
                mes = int(input("Digite o mês a previsão de devolução (mm): "))
                ano = int(input("Digite o ano a previsão de devolução (aaaa): "))

                emprestimo['Data'] = datetime(ano,mes,dia)
            elif opc1 == 4:             
                emprestimo['Nome'] = input("Nome: ")
                emprestimo['Telefone'] = input("Telefone: ")
                emprestimo['Email'] = datetime(ano,mes,dia)
            else:
                print("Opção inválida!")
        else:
            print("Livro não encontrado.")
    emprestimos = leitor
    criar_emprestimo_csv()
#BernardoGuerino

def imprimir_livros(livros):
    pesquisa= input("Digite o nome do livro !")
    for livro in livros :
        if livro['Titulo'] == pesquisa: #????
            print(f"   Título  |   Editora   |      Autor(a)  ")    
            print(f"   {livro['Titulo']}  |   {livro['Editora']}   |   {livro['Autora']}")
        
def imprimir_pessoas(pessoas):
    pesquisa= input("Digite o seu email !")
    for pessoa in pessoas :
        if pessoa['Email'] == pesquisa: #????
            print(f"   |   Nome  |   Telefone   |   E-mail ")       
            print(f"  |   {pessoa['Nome']}  |   {pessoa['Telefone']}   |   {pessoa['Email']}")
        
def imprimir_emprestimos(emprestimos):
    print(f"Email  |   Status  |   Livro  |   Detentor   |   Data emprestimo")
    for emprestimo in emprestimos:
        if emprestimos['Devolucao'] < datetime.now():
            status = "Atrasado"
        else:
            status = "No prazo"
        print(f"{emprestimo['Email']}  |    {status}  |   {emprestimo['Livro']}  |   {emprestimo['Pessoa']}   |   {emprestimo['Data']}")

while True:
    print("Bem-vinda!")
    print("Escolha uma categoria:")
    print("1 - Cadastro de livros")
    print("2 - Cadastro de contatos")
    print("3 - Gestão de empréstimos")
    
    opc1 = int(input(""))
    print("")

    if opc1 == 1:
        print("-------------------")
        print("O que deseja fazer:")
        print("1 - Cadastrar um novo livro")
        print("2 - Editar o cadastro de um livro")
        print("3 - Exibir a lista de livros cadastrados")
        print("4 - Excluir um livro dos registros")
        print("")
        opc2 = int(input(""))
        
        if   opc2 == 1:
            cadastrar_livro(livros)
        elif opc2 == 2:
            editar_livros()
        elif opc2 == 3:
            imprimir_livros(livros)
        elif opc2 == 4:
            deletar_livro(livros)
        else:
            print("Opção inválida, tente novamente.")
            print("")

    elif opc1 == 2:
        print("-------------------")
        print("O que deseja fazer:")
        print("1 - Cadastrar um novo contato")
        print("2 - Editar o cadastro de um contato")
        print("3 - Exibir a lista de contatos cadastrados")
        print("4 - Excluir um contato dos registros")
        print("")
        if   opc2 == 11:
            cadastrar_pessoa(pessoas)
        elif opc2 == 2:
            editar_contatos()
        elif opc2 == 3:
            imprimir_pessoas(pessoas)
        elif opc2 == 4:
            deletar_pessoa(pessoas)
        else:
            print("Opção inválida, tente novamente.")
            print("")

    elif opc1 == 3:
        print("-------------------")
        print("O que deseja fazer:")
        print("1 - Registrar um novo empréstimo")
        print("2 - Editar o registro de um empréstimo")
        print("3 - Exibir a lista de empréstimos")
        print("4 - Excluir um empréstimo dos registros")
        print("")
        opc2 = int(input(""))
        if   opc2 == 1:
            Cadastrar_emprestimos(emprestimos)
        elif opc2 == 2:
            editar_contatos()
        elif opc2 == 3:
            imprimir_emprestimos(emprestimos)
        elif opc2 == 4:
            deletar_emprestimo(emprestimos)
        else:
            print("Opção inválida, tente novamente.")
            print("")