
#
arquivo=open("L0Q1.in","r+")
arquivo.seek(0,0)
lista= arquivo.readlines()
arquivo.close()

#--------------------------------------#
resultado= open('L0Q1.out','w')
t= int(lista[0])

if t >=1000 or t<=1 :
       resultado.write('Você ultrapassou a quantidade de numeros de casos.\nTem que ser menor que 1000 e maior que 1.\n')
resultado.flush()

x=0
resultado.flush()
for  x in range(t):
    separacao= lista[x+1].split(' ')
    pegar1=(separacao[0])
    pegar2=(separacao[1])
#--------------------------------------#    
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
        resultado.write('Caso %d: Muito difícil\n' %(x+1))
        resultado.seek(2)
    else:
        resultado.write('Caso %d: %s\n' % ((x+1),inverso))
        resultado.seek(2)
#---------------------------------------#
if int(pegar1) >=10000 or int(pegar1)<=1:
    resultado.write('Você ultrapassou o numero maximo do A. \nTem que ser menor 10000 e maior que 1.\n')
if int(pegar2)>=100 or int(pegar2)<=1:
    resultado.write('Você ultrapassou o numero maximo do B. \nTem que ser menor 10000 e maior que 1.\n')
    
resultado.seek(2)
resultado.close()


