#Determinar se o usuário é menor ou maior de idade:

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
#---------------------------------------------------------------------------------------
     #Encontrar o maior entre dois números:
    
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro número é maior.")
elif numero2 > numero1:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")
        
#---------------------------------------------------------------------------------------
  #Verificar se um número é positivo, negativo ou zero:
  
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    
#---------------------------------------------------------------------------------------
  #Determinar se um número é par ou ímpar:
    
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#---------------------------------------------------------------------------------------
 #Calcular a média de quatro notas e decidir se o aluno está aprovado ou reprovado:
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))
nota4 = float(input("Digite a quarta nota (0 a 10): "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")