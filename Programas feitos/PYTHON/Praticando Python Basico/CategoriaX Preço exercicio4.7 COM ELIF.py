categoria=int(input("Digite a categoria do produto:"))
if categoria ==1:
  preço= 10
elif categoria==2:
   preço=18
elif categoria==3:
  preço=23
elif categoria==4:
  preço=26
elif categoria==5:
  preço=31
else:
    print("categoria invalida,digite um valor entre 1 e 5")
    preço=0
print ("O preço do produto é:R$%6.2f" %preço)

