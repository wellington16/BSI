nota1= float(input ('Digite a primeira nota: '))
while nota1<0 or nota1>10:
    nota1=float(input ("Digite a primeira nota corretamente:"))
nota2= float(input ('Digite a segunda nota : '))
while nota1<0 or nota1>10:
    nota2=float(input ("Digite a segunda nota corretamente:"))
nota3= float(input ('Digite a terceira nota : '))
while nota1<0 or nota1>10:
    nota2=float(input ("Digite a segunda nota corretamente:"))
media = ( nota1 + nota2+ nota3 )/3
if media == 10:
    print (media,"Você tirou a nota maxima")
elif media >=7:
    print ( media,"Aprovado por média")
elif media >= 5 and media <7:
    print (media,"Você está na final")
else :
    print (media,"Você foi reprovado")
