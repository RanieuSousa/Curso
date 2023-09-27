while True:
     nota = float(input("Digite a uma nota"))
     
     if nota >= 0 and  nota<= 10:
         print ("Nota valida", nota)
         break
     else:
         print(" Nota invalida.") 