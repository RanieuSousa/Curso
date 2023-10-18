import mysql.connector

class ClienteEndereco:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='nova_senha',
            host='127.0.0.1',
            database='cursosenac'
        )
        self.cursor = self.conn.cursor()

    def inserir_cliente(self, nome, email, telefone, tipo, id_endereco):
        query = "INSERT INTO cliente (nome, email, telefone, tipo, id_endereco) VALUES (%s, %s, %s, %s, %s)"
        values = (nome, email, telefone, tipo, id_endereco)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def inserir_endereco(self, cep, uf, cidade, bairro, rua, numero, complemento):
        query = "INSERT INTO endereco (cep, uf, cidade, bairro, rua, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (cep, uf, cidade, bairro, rua, numero, complemento)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def atualizar_cliente(self, id_cliente, nome, email, telefone, tipo, id_endereco):
        query = "UPDATE cliente SET nome=%s, email=%s, telefone=%s, tipo=%s, id_endereco=%s WHERE idcliente=%s"
        values = (nome, email, telefone, tipo, id_endereco, id_cliente)
        self.cursor.execute(query, values)
        self.conn.commit()

    def atualizar_endereco(self, id_endereco, cep, uf, cidade, bairro, rua, numero, complemento):
        query = "UPDATE endereco SET cep=%s, uf=%s, cidade=%s, bairro=%s, rua=%s, numero=%s, complemento=%s WHERE idendereco=%s"
        values = (cep, uf, cidade, bairro, rua, numero, complemento, id_endereco)
        self.cursor.execute(query, values)
        self.conn.commit()

    def imprimir_clientes(self):
        query = "SELECT * FROM cliente"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)

    def imprimir_enderecos(self):
        query = "SELECT * FROM endereco"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(row)

    def deletar_cliente(self, id_cliente):
        query = "DELETE FROM cliente WHERE idcliente=%s"
        self.cursor.execute(query, (id_cliente,))
        self.conn.commit()

    def deletar_endereco(self, id_endereco):
        query = "DELETE FROM endereco WHERE idendereco=%s"
        self.cursor.execute(query, (id_endereco,))
        self.conn.commit()

    def close(self):
        self.conn.close()

def exibir_menu():
    print("1. Inserir Cliente")
    print("2. Inserir Endereço")
    print("3. Atualizar Cliente")
    print("4. Listar Clientes")
    print("5. Sair")

def main():
    ce = ClienteEndereco()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Cliente: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            tipo = input("Tipo (Pessoa Física ou Jurídica): ")
            id_endereco = int(input("ID do Endereço: "))
            ce.inserir_cliente(nome, email, telefone, tipo, id_endereco)
            print("Cliente inserido com sucesso!")

        elif escolha == "2":
            cep = input("CEP: ")
            uf = input("UF: ")
            cidade = input("Cidade: ")
            bairro = input("Bairro: ")
            rua = input("Rua: ")
            numero = input("Número: ")
            complemento = input("Complemento: ")
            ce.inserir_endereco(cep, uf, cidade, bairro, rua, numero, complemento)
            print("Endereço inserido com sucesso!")

        elif escolha == "3":
            cliente_id = int(input("ID do Cliente a ser atualizado: "))
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            telefone = input("Novo Telefone: ")
            tipo = input("Novo Tipo (Pessoa Física ou Jurídica): ")
            id_endereco = int(input("Novo ID do Endereço: "))
            ce.atualizar_cliente(cliente_id, nome, email, telefone, tipo, id_endereco)
            print(f"Cliente com ID {cliente_id} atualizado com sucesso!")

        elif escolha == "4":
            print("Lista de Clientes:")
            ce.imprimir_clientes()

        elif escolha == "5":
            ce.close()
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
