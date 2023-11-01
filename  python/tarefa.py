from datetime import datetime
import csv

dataatual = datetime.now()
dataatrassada = []
tarefas = []

# CRIAR TAREFA

def criar_tarefa(tarefas):
    print("-------CADASTRA TAREFA--------")
    nome = input("Digite o nome da tarefa: ")
    tipo = input("Insira o tipo de tarefa: ")
    obs = input("Informe a observação da tarefa: ")
    data = input("Insira a data da tarefa (AAAA-MM-DD): ")
    data = datetime.strptime(data, "%Y-%m-%d")
    
    tarefa = {
        'Nome': nome,
        'Tipo': tipo,
        'Observacao': obs,
        'Data de entrega': data
    }


    if data < dataatual:
        dataatrassada.append(tarefa)
    tarefas.append(tarefa)
    criar_csv()
    print("\nTarefa cadastrada com sucesso!\n")




# CRIAR CSV
def criar_csv():

   
    with open('arquivo_tarefa.csv', mode="w", newline='')
    as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Tipo", "Observacao", "Data de entrega"])
        for tarefa in tarefas:
            writer.writerow([tarefa['Nome'],tarefa['Tipo']
                             ,tarefa['Observacao'],
                             tarefa['Data de entrega']])




# IMPRIMIR TAREFAS EM ATRASO
def imprimir_atrassada():


    print("\nTarefas em atraso:")
    for tarefa in dataatrassada:
        print("-------------------------------")
        print("Nome:", tarefa['Nome'])
        print("Tipo:", tarefa['Tipo'])
        print("Observação:", tarefa['Observacao'])
        print("Data de entrega:", tarefa['Data de entrega'].
              strftime("%Y-%m-%d"))
        print()

def atualizar_tarefa(tarefas):
    nome_tarefa = input("Digite o nome da tarefa que deseja atualizar: ")
    
    tarefa_encontrada = None
    for tarefa in tarefas:
        if tarefa['Nome'] == nome_tarefa:
            tarefa_encontrada = tarefa
            break

    if tarefa_encontrada:
        # Exibir os detalhes da tarefa
        print("\nDetalhes da tarefa a ser atualizada:")
        print("Nome:", tarefa_encontrada['Nome'])
        print("Tipo:", tarefa_encontrada['Tipo'])
        print("Observacao:", tarefa_encontrada['Observacao'])
        print("Data de entrega:", tarefa_encontrada['Data de entrega'])

        # Solicitar as novas informações da tarefa
        tarefa_atualizada = {
            'Nome': input("Digite o novo nome da tarefa: "),
            'Tipo': input("Insira o novo tipo de tarefa: "),
            'Observacao': input("Informe a nova observação da tarefa:"),
            'Data de entrega': input("Insira a nova data da tarefa (AAAA-MM-DD): "),
        }

        # Atualizar a tarefa na lista
        tarefa_encontrada.update(tarefa_atualizada)
        criar_csv()
        print("\nTarefa atualizada com sucesso!\n")
    else:
        print("\nTarefa nao encontrada!\n")


# LER E IMPRIMIR CSV
def ler_e_imprimir_csv():


    with open('arquivo_tarefa.csv', 'r', newline='') as arquivo_tarefa:
        linhas = csv.reader(arquivo_tarefa)
        for linha in linhas:
            print(linha[0], linha[1], linha[2], linha[3])

#DELETAR TAREFA
def deletar_tarefa(): 
    pesquisa = input("Digite o nome da tarefa que deseja excluir: ")
    for tarefa in tarefas:
        if tarefa['Nome'] == pesquisa:
            tarefas.remove(tarefa)
            print("Tarefa deletada com sucesso!")
        else:
            print("Nome de tarefa não encontrado na lista!")            
    criar_csv()





# LOOP PRINCIPAL
while True:
    print("------- AGENDA -------")
    print("1. Cadastrar tarefa.")
    print("2. imprimir todas as tarefas")
    print('3. Imprimir tarefas em aberto.')
    print("4. Atualizar tarefas.")
    print("5. Deletar tarefa.")
    print("6. Sair.")
    print("----------------------")
    print("\n")
    op = int(input("Escolha uma opção: "))


   
   
   
    if op == 1:

        criar_tarefa(tarefas)

   
   
    elif op == 2:
        ler_e_imprimir_csv()
    
    
    
    
    elif op == 3:
        imprimir_atrassada()
   
   
   
    elif op == 4:
        atualizar_tarefa(tarefas)
    
    

    elif op == 5:
        deletar_tarefa()
    elif op == 6:

        break
   
   
    else:
        print("-------------------")
        print("  OPÇÃO INVÁLIDA   ")
        print('-------------------')