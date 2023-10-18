def cadastrar_cliente(clientes, nome , email, telefone):
    cliente ={
        'Nome': nome,
        'Email':email,
        'Telefone': telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!" )
    print("*********************************************")
    
def imprimir_clientes(clientes):
    for indice,cliente in enumerate(clientes):
        print(f"Cliente {indice}")
        print(f"Nome: {cliente['Nome']} ")
        print(f"Email: {cliente['Email']} ")
        print(f"Telefone: {cliente['Telefone']} ")
        print("*********************************************")

def atualizar_cliente(clientes, indice, nome, email, telefone):
    if 0 <= indice < len(clientes):
        clientes[indice]['Nome'] = nome
        clientes[indice]['Email'] = email
        clientes[indice]['Telefone'] = telefone
        print("Informações do cliente atualizadas com sucesso!")
    else:
        print("Índice inválido. Cliente não encontrado.")
def deletar_cliente(clientes,indice):
    if 0 <= indice < len(clientes):
        del clientes[indice]
        print("Informações do cliente deletadas com sucesso!")
    else:
        print("Índice inválido. Cliente não encontrado.")
    
clientes = []

while True:
       print("\nMENU")
       print("1. Cadastrar Cliente")
       print("2. Imprimir Cliente")
       print("3. Atualizar Cliente")
       print("4. deletar Cliente")
       print("5. Sair")
       
       opcao = int(input("Escolhar uma opção: "))
       
       if opcao == 1:
            nome  = input("Nome do cliente: ")
            email  = input("Email do cliente: ")
            telefone  = input("telefone do cliente: ")
            cadastrar_cliente(clientes, nome,email, telefone)
       elif opcao == 2:
            imprimir_clientes(clientes)
       elif opcao  == 3:
           indice = int(input("Digite o número do cliente"))
           nome = input("Nome do cliente: ")
           email = input("Email do cliente: ")
           telefone = input("telefone do cliente: ")
           atualizar_cliente(clientes,indice,nome,email,telefone)
       elif opcao  == 4:
           indice = int(input("Digite o número do cliente"))
           deletar_cliente(clientes,indice)
             
       elif opcao  == 5:
            print("Saindo....")
            break
    
       else:
           print("Opção invalida")
        