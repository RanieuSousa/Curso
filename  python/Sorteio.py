import random

# Crie uma lista de números de 1 a 10
numeros = list(range(1, 11))

# Embaralhe a lista de números
random.shuffle(numeros)

# Divida a lista embaralhada em duas listas de 5 elementos cada
lista1 = numeros[:5]
lista2 = numeros[5:]

# Imprima as duas listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
