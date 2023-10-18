# Inicialização das listas para armazenar nomes e telefones
nomes = []
telefones = []

# Loop principal do programa
while True:
    # Exibe o menu e obtém a escolha do usuário
    menu = float(input(
        "Escolha uma opção para o menu:\n"
        "1 - Inserir\n"
        "2 - Atualizar\n"
        "3 - Imprimir\n"
        "4 - Deletar\n"
        "5 - Sair\n"
    ))

    if menu == 1:
        # Opção 1: Inserir um novo contato
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        nomes.append(nome)
        telefones.append(telefone)
        print("Nome e telefone inseridos com sucesso.")
    elif menu == 2:
        # Opção 2: Atualizar um contato existente
        nome_para_atualizar = input("Digite o nome a ser atualizado: ")
        if nome_para_atualizar in nomes:
            indice = nomes.index(nome_para_atualizar)
            novo_telefone = input("Digite o novo telefone: ")
            telefones[indice] = novo_telefone
            print("Telefone atualizado com sucesso.")
        else:
            print("Nome não encontrado.")
    elif menu ==3:
        # Opção 3: Imprimir a lista de contatos
        print("Lista de Contatos:")
        for i in range(len(nomes)):
            print(f"{nomes[i]}: {telefones[i]}")
    elif menu == 4:
        # Opção 4: Deletar um contato
        nome_para_deletar = input("Digite o nome a ser deletado: ")
        if nome_para_deletar in nomes:
            indice = nomes.index(nome_para_deletar)
            del nomes[indice]
            del telefones[indice]
            print("Contato deletado com sucesso.")
        else:
            print("Nome não encontrado.")
    elif menu == 5:
        # Opção 5: Sair do programa
        print("Saindo do programa.")
        break
    else:
        # Trata opções inválidas
        print("Opção inválida. Por favor, escolha uma opção válida.")
