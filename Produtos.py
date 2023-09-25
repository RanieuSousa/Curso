
nomes_produtos = ["Produto A", "Produto B", "Produto C"]
valores_produtos = [100.0, 200.0, 150.0]
quantidades = [100, 100, 100]


taxa_imposto1 = 0.12
taxa_imposto2 = 0.06
taxa_imposto3 = 0.03
valor_frete = 50.0
custos_individuais = []

for i in range(len(valores_produtos)):
    valor_produto = valores_produtos[i]
    quantidade = quantidades[i]
    imposto1 = valor_produto * taxa_imposto1
    imposto2 = valor_produto * taxa_imposto2
    imposto3 = valor_produto * taxa_imposto3
    custo_individual = (valor_produto + imposto1 + imposto2 + imposto3) + (valor_frete / quantidade)
    custos_individuais.append(custo_individual)

valores_venda = [custo + (custo * 0.6) for custo in custos_individuais]

for i in range(len(nomes_produtos)):
    print(f"Produto: {nomes_produtos[i]}, Custo Total: R${custos_individuais[i]:.2f}, Valor de Venda: R${valores_venda[i]:.2f}")
