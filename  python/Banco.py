import mysql.connector

# Conectar ao banco de dados
config = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="nova_senha",
    database="cursosenac"
)

# Criar um cursor para executar comandos SQL
cursor = config.cursor()

def criar_cliente(nome, email, telefone, tipo, id_endereco):
    sql = "INSERT INTO cliente (nome, email, telefone, tipo, id_endereco)
    VALUES (%s, %s,%s, %s, %s)"
    val = (nome, email, telefone, tipo, id_endereco)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente inserido com sucesso!")

def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

def atualizar_cliente(idcliente, nome, email, telefone, tipo, id_endereco):
    sql = "UPDATE cliente SET nome = %s, email = %s,
    telefone = %s, tipo = %s,id_endereco = %s 
    WHERE idcliente = %s"
    val = (nome, email, telefone, tipo, id_endereco, idcliente)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente atualizado com sucesso!")

def deletar_cliente(idcliente):
    sql = "DELETE FROM cliente WHERE idcliente = %s"
    val = (idcliente,)
    cursor.execute(sql, val)
    config.commit()
    print("Cliente excluído com sucesso!")

def menu():
    while True:
        print("\nMenu:")
        print("1. Criar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Sair")

        escolha = input("Escolha a opção (1/2/3/4/5): ")

        if escolha == "1":
            nome = input("Nome do Cliente: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            tipo = input("Tipo: ")
            id_endereco = input("ID do Endereço: ")
            criar_cliente(nome, email, telefone, tipo, id_endereco)
            print("Cliente inserido com sucesso!")
        elif escolha == "2":
            print("\nLista de Clientes:")
            listar_clientes()
        elif escolha == "3":
            idcliente = input("ID do Cliente a ser atualizado: ")
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            telefone = input("Novo Telefone: ")
            tipo = input("Novo Tipo: ")
            id_endereco = input("Novo ID do Endereço: ")
            atualizar_cliente(idcliente, nome, email, telefone, tipo, id_endereco)
            print("Cliente atualizado com sucesso!")
        elif escolha == "4":
            idcliente = input("ID do Cliente a ser deletado: ")
            deletar_cliente(idcliente)
            print("Cliente excluído com sucesso!")
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Escolha uma opção válida.")

if __name__ == "__main__":
    menu()

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    config.close()
