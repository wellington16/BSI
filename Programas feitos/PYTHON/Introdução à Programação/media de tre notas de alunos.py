n1=int(input("Digite a primeira nota:"))
n2=int(input("Digite a segunda nota:"))
n3=int(input("Digite a terceira nota:"))
media= (n1+n2+n3)/3
if media ==10:
    print("Aprovado com a nota maxima")
elif media >=7:
    print ("Aprovado por media")
elif 5<=media<7:
    print ("Você está na final")
else:
    print ("Você foi reprovado")
