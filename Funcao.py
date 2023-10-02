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
        print(f"Cliente {indice +1}")
        print(f"Nome: {cliente['Nome']} ")
        print(f"Email: {cliente['Email']} ")
        print(f"Telefone: {cliente['Telefone']} ")
        print("*********************************************")

def atualizar_cliente(clientes,indice,nome,email,telefone):
    if indice >= len(clientes) and indice < len(clientes):
        clientes[indice]['Nome'] = Nome
        clientes[indice]['Email'] = Email
        clientes[indice]['Telefone'] = Telefone
        print("Informações do cliente atualizadas com sucesso!")
  
clientes = []

while True:
       print("\nMENU")
       print("1. Cadastrar Cliente")
       print("2. Imprimir Cliente")
       print("3. Atualizar Cliente")
       print("4. Sair")
       
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
            print("Saindo....")
            break
    
       else:
           print("Opção invalida")
        