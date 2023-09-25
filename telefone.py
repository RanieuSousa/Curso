# Criar listas de nomes e números de telefone
nomes = ["João", "Maria", "Pedro", "Ana", "Luiza"]
telefones = ["123-456-7890", "987-654-3210", "555-123-4567", "999-888-7777", "333-222-1111"]

# Usar um loop para imprimir nome e número da mesma posição
for i in range(len(nomes)):
    nome = nomes[i]
    telefone = telefones[i]
    print(f"Nome: {nome}, Telefone: {telefone}")