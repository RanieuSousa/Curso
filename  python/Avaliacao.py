# Lista para armazenar as informações dos alunos (nome, notas)
alunos = []

# Função para cadastrar notas dos alunos
def cadastrar_notas():
    nome = input("Digite o nome do aluno: ")
    notas = []
    while True:
        nota = float(input("Digite uma nota do aluno (ou digite -1 para encerrar): "))
        if nota == -1:
            break
        notas.append(nota)
    alunos.append({"nome": nome, "notas": notas})
    print("Notas cadastradas com sucesso!")

# Função para editar notas dos alunos
def editar_notas():
    nome = input("Digite o nome do aluno para editar as notas: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            print(f"Notas atuais do(a) {nome}: {aluno['notas']}")
            notas = []
            while True:
                nota = float(input("Digite uma nova nota do aluno (ou digite -1 para encerrar): "))
                if nota == -1:
                    break
                notas.append(nota)
            aluno["notas"] = notas
            print("Notas editadas com sucesso!")
            return
    print(f"Aluno {nome} não encontrado.")

# Função para deletar notas dos alunos
def deletar_notas():
    nome = input("Digite o nome do aluno para deletar as notas: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            del aluno["notas"]
            print("Notas deletadas com sucesso!")
            return
    print(f"Aluno {nome} não encontrado.")

# Função para imprimir notas dos alunos
def imprimir_notas():
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']}, Notas: {aluno['notas']}")

# Função para calcular a média das notas
def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    return 0

# Função para listar alunos aprovados (Média >= 7)
def alunos_aprovados():
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        if media >= 7:
            print(f"Aluno: {aluno['nome']}, Média: {media}")

# Função para listar alunos reprovados (Média < 7)
def alunos_reprovados():
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        if media < 7:
            print(f"Aluno: {aluno['nome']}, Média: {media}")

while True:
    print("\nMenu:")
    print("1. Cadastrar Notas")
    print("2. Editar Notas")
    print("3. Deletar Notas")
    print("4. Imprimir Notas")
    print("5. Calcular Média")
    print("6. Listar Alunos Aprovados")
    print("7. Listar Alunos Reprovados")
    print("8. Encerrar Cadastro")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_notas()
    elif opcao == "2":
        editar_notas()
    elif opcao == "3":
        deletar_notas()
    elif opcao == "4":
        imprimir_notas()
    elif opcao == "5":
        media = calcular_media([nota for aluno in alunos for nota in aluno["notas"]])
        print(f"Média das notas: {media:.2f}")
    elif opcao == "6":
        alunos_aprovados()
    elif opcao == "7":
        alunos_reprovados()
    elif opcao == "8":
        print("Encerrando o cadastro.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
