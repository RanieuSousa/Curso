# Inicialize uma lista vazia para armazenar os detalhes dos produtos
produtos = []

def calcular_preco_custo(valor_compra, frete_total, quantidade_compra, imposto1, imposto2, imposto3):
    frete_por_unidade = frete_total / quantidade_compra
    preco_custo = valor_compra + frete_por_unidade
    preco_custo += preco_custo * (imposto1 + imposto2 + imposto3)
    return preco_custo

def calcular_preco_venda(preco_custo):
    return preco_custo * 1.6  # 60% de lucro
imposto1 = 0.12
imposto2 = 0.06
imposto3 = 0.03

while True:
    print("\n===== Menu =====")
    print("1. Inserir informações do produto")
    print("2. Atualizar informações do produto")
    print("3. Deletar produto")
    print("4. Imprimir detalhes do produto atual")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1/2/3/4/5): ")
    
    if opcao == '1':
        # Solicitar informações sobre o produto
        nome_produto = input("Nome do produto: ")
        valor_compra = float(input("Valor da compra: "))
        quantidade_compra = int(input("Quantidade de compra: "))
        frete_total = float(input("Frete total da quantidade comprada: "))
        
        # Calcular o preço de custo
        preco_custo = calcular_preco_custo(valor_compra, frete_total, quantidade_compra, imposto1, imposto2, imposto3)
        
        # Calcular o preço de venda com base na porcentagem de lucro
        preco_venda = calcular_preco_venda(preco_custo)
        
        # Criar um dicionário com os detalhes do produto
        detalhes_produto = {
            "Nome do Produto": nome_produto,
            "Valor da Compra": valor_compra,
            "Quantidade de Compra": quantidade_compra,
            "Frete Total": frete_total,
            "Preço de Custo": preco_custo,
            "Preço de Venda": preco_venda
        }
        
        # Adicionar os detalhes do produto à lista de produtos
        produtos.append(detalhes_produto)
        print("Detalhes do produto foram salvos com sucesso.")
    
    elif opcao == '2':
        # Atualizar informações do produto
        if len(produtos) == 0:
            print("Nenhum produto foi inserido ainda.")
        else:
            print("Lista de produtos:")
            for i, produto in enumerate(produtos):
                print(f"{i + 1}. {produto['Nome do Produto']}")
            
            escolha = int(input("Escolha o número do produto que deseja atualizar: "))
            if 1 <= escolha <= len(produtos):
                produto_atualizar = produtos[escolha - 1]
                
                # Solicitar informações atualizadas
                valor_compra = float(input("Novo valor da compra: "))
                quantidade_compra = int(input("Nova quantidade de compra: "))
                frete_total = float(input("Novo frete total da quantidade comprada: "))
                
                # Atualizar os detalhes do produto
                produto_atualizar["Valor da Compra"] = valor_compra
                produto_atualizar["Quantidade de Compra"] = quantidade_compra
                produto_atualizar["Frete Total"] = frete_total
                
                # Recalcular preço de custo e preço de venda
                produto_atualizar["Preço de Custo"] = calcular_preco_custo(valor_compra, frete_total, quantidade_compra, imposto1, imposto2, imposto3)
                produto_atualizar["Preço de Venda"] = calcular_preco_venda(produto_atualizar["Preço de Custo"])
                
                print("Detalhes do produto atualizados com sucesso.")
            else:
                print("Escolha inválida.")
    
    elif opcao == '3':
        # Deletar produto
        if len(produtos) == 0:
            print("Nenhum produto foi inserido ainda.")
        else:
            print("Lista de produtos:")
            for i, produto in enumerate(produtos):
                print(f"{i + 1}. {produto['Nome do Produto']}")
            
            escolha = int(input("Escolha o número do produto que deseja deletar: "))
            if 1 <= escolha <= len(produtos):
                produto_deletar = produtos.pop(escolha - 1)
                print(f"O produto '{produto_deletar['Nome do Produto']}' foi deletado com sucesso.")
            else:
                print("Escolha inválida.")
    
    elif opcao == '4':
        # Imprimir detalhes do produto atual
        if len(produtos) == 0:
            print("Nenhum produto foi inserido ainda.")
        else:
            produto_atual = produtos[-1]
            print("\n===== Detalhes do Produto Atual =====")
            for chave, valor in produto_atual.items():
                print(f"{chave}: {valor}")
    
    elif opcao == '5':
        # Sair do programa
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5).")
