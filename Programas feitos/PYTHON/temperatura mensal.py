"""#exercios 
media_mensal=[]

media_anual=[]
for i in range(12):
    t= float (input("t: "))
    media_mensal.append(t)
for e in media_mensal:
    media_anual += e
media = media_anual/12
print("A media anual e: %2f" % media)
for i,e in enumerate (media_mensal):
    if e > media:
        print ("No mês %s, a temp. foi: %.2f"%(meses[i], e)) """
"""#multiplicar um numero:
continuar=("S")
while continuar == "S":
    i=1
    num=int(input("Digite um numero:"))
    while i < 11:
        r = num * i
        print('%d x %d = %d' % (num,i,r))
        i+=1
    continuar = input("deseja continuar ?(S/N)")
    continuar=continuar.upper()
    if continuar != "N" or "S":
        print ("Erro! Deve-se digitar apenas S ou N!")
l=input("diegite a coluna:")
a=input("diegite a linha:")
matriz1= [0]*a
matriz2= a*l

matriz= matriz1[:]
for i in range(l):
    for j in range (a):
        num1=randit(1,10)
        num= randit (1,10)
        matriz [i][j]=num1
        matriz [i][j]=num2"""

'''altura= float(input("altura:"))
idade  =  float (input("idade:"))
contador=0
c=1
while altura !=0:
        if idade > 13 and altura < 1.5:
            c=contador + 1
        print (c)
     break'''
a =1
n=1
e=1
for i in range(1,20):
    n= n*i
    e=a**i/n
    print (e)

        
       
