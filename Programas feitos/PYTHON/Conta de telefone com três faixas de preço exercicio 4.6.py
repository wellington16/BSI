minutos=int (input("Quantos minutos você utlizou este mês:"))
if minutos <200:
    preço=0.20
else:
    if minutos<400:
        preço=0.18
    else:
        preço=0.15
    print ("Você vai pagar este mês :R$%6.2f"%(minutos*preço))
