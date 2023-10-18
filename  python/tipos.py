# Tipos de Dados em Python

# Inteiros
numero_inteiro = 42

# Números de Ponto Flutuante
numero_ponto_flutuante = 3.14

# Texto (String)
texto = "Olá, mundo!"

# Booleanos
verdadeiro = True
falso = False

# Listas
minha_lista = [1, 2, 3, "Python", True]

# Tuplas
minha_tupla = (1, "Python", 3.14)

# Dicionários
meu_dicionario = {"nome": "João", "idade": 30}

# Conjuntos
meu_conjunto = {1, 2, 3, 3, 4}  # Resultará em {1, 2, 3, 4}

# NoneType
valor_nulo = None

# Bytes
dados_binarios = b"exemplo"

# Tipos personalizados (Classe)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Alice", 25)

# Exibindo os valores das variáveis
print("Número Inteiro:", numero_inteiro)
print("Número de Ponto Flutuante:", numero_ponto_flutuante)
print("Texto (String):", texto)
print("Booleano (Verdadeiro):", verdadeiro)
print("Booleano (Falso):", falso)
print("Lista:", minha_lista)
print("Tupla:", minha_tupla)
print("Dicionário:", meu_dicionario)
print("Conjunto:", meu_conjunto)
print("NoneType:", valor_nulo)
print("Bytes:", dados_binarios)
print("Tipo personalizado (Pessoa):", pessoa1.nome, pessoa1.idade)