arquivo=open("L0Q1.in","r+")
lista= arquivo.readlines()
arquivo.close()
print (lista)
T= int(lista[0])

resultado= open('L0Q1.out','r+')
x=0
while x <=(int(T)):
    separacao= lista[x+1].split('\n')
    pegar1=(separacao[0])
    pegar2=(separacao[1])
    y=0

    resultado.flush()
    while b < c:
        inverso= ((a * b) % c)
        if inverso==1:
            print("b=",inverso)
        b += 1
   
        resulatdo.flush()

    if inverso == 0:
        print('Caso',(x+1),": Muito difícil")
    else :    
       print('Caso',(x+1),":" ,inverso)

resultado.close()    
