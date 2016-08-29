arquivo=open("L0Q1.in","r+")
lista= arquivo.readlines()
arquivo.close()
print (lista)

resultado= open('L0Q1.out','r+')

t= int(lista[0])
x=0
for  x in range(t):
    separacao= lista[x+1].split(' ')
    pegar1=(separacao[0])
    pegar2=(separacao[1])
    y=0

    resultado.flush()
    inverso=0    
    queroaxar=0
    while queroaxar < int(pegar2):
        calcularinv= ((int( pegar1) * int(queroaxar)) % int(pegar2))
        if calcularinv == 1:
            inverso = queroaxar
        queroaxar += 1

    if inverso == 0:
        resultado.write('Caso %d: Muito difícil\n')
    else :
        resultado.write('Caso %d: %s\n' % ((x+1),inverso))
       
resultado.close()    
