import csv

clientes = [
    {"nome": "João", "email": "joao@example.com", "telefone": "123-456-7890"},
    {"nome": "Maria", "email": "maria@example.com", "telefone": "987-654-3210"},
    {"nome": "Pedro", "email": "pedro@example.com", "telefone": "555-555-5555"},
]


def gravar()
with open('arquivo_csv', mode="w", newline="") as arquivo_csv:
   
    writer = csv.writer(arquivo_csv)

    writer.writerow(["Nome", "Email", "Telefone"])

    
    for cliente in clientes:
        writer.writerow([cliente["nome"], cliente["email"], cliente["telefone"]])

print("Os dados dos clientes foram salvos no arquivo ")
