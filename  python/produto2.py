def cadastrar_produto(produtos, nome , valor, frete, ganho, imp1, imp2, imp3, quantidade,custo,venda):
    produto ={
        'Nome': nome,
        'Valor':valor,
        'Frete': frete,
        'Ganho':ganho,
        'Imp1':imp1,
        'Imp2':imp2,
        'Imp3':imp3,
        'Quantidade':quantidade,
        'Custo':custo,
        'Venda':venda
          
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!" )
    print("*********************************************")
    
def imprimir_produto(produtos):
    for indice,produto in enumerate(produtos):
        print(f"Produto {indice +1}")
        print(f"Nome: {produto['Nome']} ")
        print(f"Valor: {produto['Valor']} ")
        print(f"Frete: {produto['Frete']} ")
        print(f"Ganho: {produto['Ganho']} ")
        print(f"Imposto 1: {produto['Imp1']} ")
        print(f"Imposto 2: {produto['Imp2']} ")
        print(f"Imposto 3: {produto['Imp3']} ")
        print(f"Quantidade: {produto['Quantidade']} ")
        print(f"Custo: {produto['Custo']:.2f}")
        print(f"Venda: {produto['Venda']:.2f} ")
            
        print("*********************************************")

def atualizar_produtos(produtos,indice, nome , valor, frete, ganho, imp1, imp2, imp3, quantidade,custo,venda):
    if indice >= len(clientes) and indice < len(clientes):
        produtos[indice]['Nome'] = nome
        produtos[indice]['Valor'] = valor
        produtos[indice]['Frete'] = frete
        produtos[indice]['Ganho'] = ganho
        produtos[indice]['Imp1'] = imp1
        produtos[indice]['Imp2'] = imp2
        produtos[indice]['Imp3'] = imp3
        produtos[indice]['Quantidade'] = quantidade
        produtos[indice]['Custo'] = custo
        produtos[indice]['Venda'] = venda
        print("Informações do cliente atualizadas com sucesso!")
  
produtos = []

while True:
       print("\nMENU")
       print("1. Cadastrar Produto")
       print("2. Imprimir Produto")
       print("3. Atualizar Produto")
       print("4. Sair")
       
       opcao = int(input("Escolhar uma opção: "))
       
       if opcao == 1:
            nome = input("Digite o nome do produto: ")
            valor = float(input("Digite o valor do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            frete = float(input("Digite o valor do frete para o produto: "))
            imposto1 = float(input("Digite a taxa de imposto 1  "))
            imposto2 = float(input("Digite a taxa de imposto 2  "))
            imposto3 = float(input("Digite a taxa de imposto 3 "))
            ganho = float(input("Digite a margem de lucro "))
        
            imposto1 = (valor * imposto1) / 100
            imposto2 = (valor * imposto2) / 100
            imposto3 = (valor * imposto3) / 100
            frete = frete / quantidade
            custo = valor + imposto1 + imposto2 + imposto3 + frete
            venda = custo + (custo * (ganho / 100))
            cadastrar_produto(produtos, nome,valor, frete, ganho, imposto1, imposto1,imposto3, quantidade,custo,venda)
       elif opcao == 2:
            imprimir_produto(produtos)
       elif opcao  == 3:
           indice = int(input("Digite o número do cliente"))
           nome = input("Digite o nome do produto: ")
           valor = float(input("Digite o valor do produto: "))
           quantidade = int(input("Digite a quantidade do produto: "))
           frete = float(input("Digite o valor do frete para o produto: "))
           imposto1 = float(input("Digite a taxa de imposto 1  "))
           imposto2 = float(input("Digite a taxa de imposto 2  "))
           imposto3 = float(input("Digite a taxa de imposto 3 "))
           ganho = float(input("Digite a margem de lucro "))
        
           imposto1 = (valor * imposto1) / 100
           imposto2 = (valor * imposto2) / 100
           imposto3 = (valor * imposto3) / 100
           frete = frete / quantidade
           custo = valor + imposto1 + imposto2 + imposto3 + frete
           venda = custo + (custo * (ganho / 100))
           cadastrar_produto(produtos, nome,valor, frete, ganho, imposto1, imposto1,imposto3, quantidade,custo,venda)
           
       elif opcao  == 4:
            print("Saindo....")
            break
    
       else:
           print("Opção invalida")
        