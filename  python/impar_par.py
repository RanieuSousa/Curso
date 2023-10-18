primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o primeiro segundo: "))
soma =0
if primeiro %2 == 0:
    for i in range(primeiro,segundo,2):
        soma = soma + i
        print(soma)
else:
     for i in range(primeiro,segundo,2):
            soma = soma + i
            print(soma)