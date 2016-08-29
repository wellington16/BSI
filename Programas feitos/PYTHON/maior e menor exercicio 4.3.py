primeiro=int(input("Digite o primero :"))
segundo=int(input("Digite o segundo:"))
terceiro=int(input("Digite o terceiro:"))
if primeiro>segundo>terceiro:
     print ("primeiro é o maior e terceiro é menor")
     
if terceiro>segundo>primeiro:
     print ("terceiro é o maior e primeiro é menor")
     
if segundo>terceiro>primeiro:
    print ("segundo é o maior e primeiro é menor")
    
if segundo<primeiro<terceiro:
     print ("terceiro é o maior e segundo é menor")
while primeiro==segundo:
     print ("Mensagem de ERRO, NUMEROS IGUAIS")
     break
while segundo==terceiro:
     print ("Mensagem de ERRO, NUMEROS IGUAIS")
     break
while primeiro==terceiro:
     print ("Mensagem de ERRO, NUMEROS IGUAIS")
     break

