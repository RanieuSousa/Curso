# Solicita ao usuário que insira o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o operador (+, -, *, /)
operador = input("Digite o operador (+, -, *, /): ")

# Solicita ao usuário que insira o segundo número
numero2 = float(input("Digite o segundo número: "))

# Realiza a operação e exibe o resultado
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    if numero2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = numero1 / numero2
else:
    print("Operador inválido. Use +, -, *, ou /.")

if 'resultado' in locals():
    print(f"Resultado: {resultado}")
