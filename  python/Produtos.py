# Listas para armazenar os dados dos produtos
nomes_produtos = []
valores_produtos = []
quantidades = []
valor_frete = []
valor_custo = []
valor_final = []

while True:
    print("\nMenu:")
    print("1. Cadastrar Produto")
    print("2. Imprimir Resultados")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        # Cadastrar um produto
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
        
        nomes_produtos.append(nome)
        valores_produtos.append(valor)
        quantidades.append(quantidade)
        valor_frete.append(frete)
        valor_custo.append(custo)
        valor_final.append(venda)
        
        print("Produto cadastrado com sucesso.")
    elif opcao == "2":
        # Imprimir resultados
        if not nomes_produtos:
            print("Nenhum produto cadastrado ainda.")
        else:
            print("\nResultados:")
            for i in range(len(nomes_produtos)):
                print(f"Produto: {nomes_produtos[i]},"
                      f" Custo Total: R${valor_custo[i]:.2f},"
                      f" Valor de Venda: R${valor_final[i]:.2f},"
                      f" Valor de frete: R${valor_frete[i]:.2f},"
                      f" Quantidade: R${ quantidades[i]:.2f},"
                      f" Estoque Final Custo R${valor_custo[i] * quantidades[i]},"
                      f" Estoque Final Venda R${valor_final[i] * quantidades[i]}")
    elif opcao == "3":
        # Sair do programa
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
