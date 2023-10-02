import tkinter as tk

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    nome = nome_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    
    if nome and email and telefone:
        cliente = {
            'Nome': nome,
            'Email': email,
            'Telefone': telefone
        }
        clientes.append(cliente)
        status_label.config(text="Cliente cadastrado com sucesso!")
        limpar_campos()
    else:
        status_label.config(text="Preencha todos os campos!")

# Função para imprimir informações de todos os clientes
def imprimir_clientes():
    output_text.config(state=tk.NORMAL)  # Habilita a edição do campo de texto
    output_text.delete(1.0, tk.END)  # Limpa o campo de texto

    for indice, cliente in enumerate(clientes):
        output_text.insert(tk.END, f"Cliente {indice + 1}\n")
        output_text.insert(tk.END, f"Nome: {cliente['Nome']}\n")
        output_text.insert(tk.END, f"Email: {cliente['Email']}\n")
        output_text.insert(tk.END, f"Telefone: {cliente['Telefone']}\n")
        output_text.insert(tk.END, "*********************************************\n")

    output_text.config(state=tk.DISABLED)  # Desabilita a edição do campo de texto

# Função para limpar os campos de entrada
def limpar_campos():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Clientes")

# Entradas de texto
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

telefone_label = tk.Label(root, text="Telefone:")
telefone_label.pack()
telefone_entry = tk.Entry(root)
telefone_entry.pack()

# Botões
cadastrar_button = tk.Button(root, text="Cadastrar Cliente", command=cadastrar_cliente)
cadastrar_button.pack()

imprimir_button = tk.Button(root, text="Imprimir Clientes", command=imprimir_clientes)
imprimir_button.pack()

# Campo de texto para saída
output_text = tk.Text(root, height=20, width=50)
output_text.pack()
output_text.config(state=tk.DISABLED)  # Inicialmente, o campo de texto não pode ser editado

# Label para exibir status
status_label = tk.Label(root, text="", fg="red")
status_label.pack()

# Inicialização da lista de clientes
clientes = []

root.mainloop()
