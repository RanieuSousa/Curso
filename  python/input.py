numeros=[]
PAR = []
IMPAR = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
    if numero % 2 == 0:
        PAR.append(numero)
    else:
        IMPAR.append(numero)

print("Números digitados:",numeros)
print("Vetor PAR:", PAR)
print("Vetor IMPAR:", IMPAR)
