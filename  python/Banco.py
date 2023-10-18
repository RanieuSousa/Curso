import mysql.connector

def conectar_ao_banco():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="cursosenac"
    )

def menu():
    print("Menu:")
    print("1. Inserir cliente")
    print("2. Atualizar cliente")
    print("3. Imprimir clientes")
    print("4. Deletar cliente")
    print("0. Sair")

def main():
    conn = conectar_ao_banco()
    cursor = conn.cursor()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do cliente: ")
            email = input("E-mail do cliente: ")
            telefone = input("Telefone do cliente: ")
            tipo = int(input("Tipo do cliente (inteiro): "))
           
        elif escolha == "2":
            nome = input("Nome do cliente a ser atualizado: ")
            novo_email = input("Novo e-mail: ")
            novo_telefone = input("Novo telefone: ")
            novo_tipo = int(input("Novo tipo (inteiro): "))
           
        elif escolha == "3":
            imprimir_clientes()
        elif escolha == "4":
            nome = input("Nome do cliente a ser excluído: ")
            deletar_cliente(nome)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()
    print("Programa encerrado.")

if __name__ == "__main__":
    main()
import mysql.connector

def conectar_ao_banco():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="cursosenac"
    )

def inserir_cliente(nome, email, telefone, tipo):
    conn = conectar_ao_banco()
    cursor = conn.cursor()
    sql = "INSERT INTO Cliente (nome, email, telefone, tipo) VALUES (%s, %s, %s, %s)"
    values = (nome, email, telefone, tipo)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Cliente inserido com sucesso!")

def atualizar_cliente(nome, novo_email, novo_telefone, novo_tipo):
    conn = conectar_ao_banco()
    cursor = conn.cursor()
    sql = "UPDATE Cliente SET email = %s, telefone = %s, tipo = %s WHERE nome = %s"
    values = (novo_email, novo_telefone, novo_tipo, nome)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Cliente atualizado com sucesso!")

def imprimir_clientes():
    conn = conectar_ao_banco()
    cursor = conn.cursor()
    sql = "SELECT * FROM Cliente"
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    for row in result:
        print(row)

def deletar_cliente(nome):
    conn = conectar_ao_banco()
    cursor = conn.cursor()
    sql = "DELETE FROM Cliente WHERE nome = %s"
    values = (nome,)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Cliente excluído com sucesso!")

def menu():
    print("Menu:")
    print("1. Inserir cliente")
    print("2. Atualizar cliente")
    print("3. Imprimir clientes")
    print("4. Deletar cliente")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do cliente: ")
            email = input("E-mail do cliente: ")
            telefone = input("Telefone do cliente: ")
            tipo = int(input("Tipo do cliente (inteiro): "))
            inserir_cliente(nome, email, telefone, tipo)
        elif escolha == "2":
            nome = input("Nome do cliente a ser atualizado: ")
            novo_email = input("Novo e-mail: ")
            novo_telefone = input("Novo telefone: ")
            novo_tipo = int(input("Novo tipo (inteiro): "))
            atualizar_cliente(nome, novo_email, novo_telefone, novo_tipo)
        elif escolha == "3":
            imprimir_clientes()
        elif escolha == "4":
            nome = input("Nome do cliente a ser excluído: ")
            deletar_cliente(nome)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")

if __name__ == "__main__":
    main()
