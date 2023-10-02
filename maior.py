primeiro_numero = float(input("Digite o 1º número: "))
maior_numero = primeiro_numero
for i in range(2, 6):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > maior_numero:
        maior_numero = numero
print(f"O maior número é: {maior_numero}")
