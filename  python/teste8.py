produto=[0,"bolacha","leite","refri","carvao"]
preco_produto=[0,5.50,4.00,7.50,18.50]
frete=40

for i in range(1,len(produto)):
    
    print(produto[i] , preco_produto[i])

pd=int(input("qual produto vc deseja? digite a posição dele:"))

quantidade=int(input("quantos produtos voce deseja levar?: "))

valor=preco_produto[pd]*quantidade

frete=-(-frete/quantidade)

imposto1=valor*0.12
imposto2=valor*0.06
imposto3=valor*0.03

valor_de_custo=(valor+frete+imposto1+imposto2+imposto3)
taxa=valor_de_custo*0.60
valor_de_venda=valor_de_custo+taxa
valor_de_venda=round(valor_de_venda,2)

print("o valor final é: ",valor_de_venda)