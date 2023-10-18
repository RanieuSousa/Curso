import csv


def cadastra_usuario(usuarios, nome, telefone, email):
    usuario = {
        'Nome': nome,
        'Telefone': telefone,
        'Email': email,
    }
    usuarios.append(usuario)

def salvar_usuarios(usuarios):
    with open('arquivos.csv', mode='w', newline='') as arquivos_csv:
        writer = csv.writer(arquivos_csv)
        writer.writerow(["Nome", "Email", "Telefone"])  # Escreve o cabeçalho no arquivo CSV
        for usuario in usuarios:
            writer.writerow([usuario['Nome'], usuario['Email'], usuario['Telefone']])

def main():
    usuarios = []

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar usuário")
        print("2. Imprimir usuários")
        print("3. Sair")

        escolha = input("Opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            cadastra_usuario(usuarios, nome, telefone, email)
            print("Usuário cadastrado com sucesso.")
        elif escolha == '2':
            for usuario in usuarios:
                print(f"Nome: {usuario['Nome']} | Telefone: {usuario['Telefone']} | E-mail: {usuario['Email']}")
        elif escolha == '3':
            salvar_usuarios(usuarios)
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
