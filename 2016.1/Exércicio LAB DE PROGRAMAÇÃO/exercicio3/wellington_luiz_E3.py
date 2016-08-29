arquivo=open("E3.in","r+")
lista= arquivo.readlines()
arquivo.close()

Resultado = open('E3.out','w')

t= int(lista[0])


if (t<=1000) and (t>=1):
    for  x in range(t):
        separacao= lista[x+1].split(' ')
        pegar1=int(separacao[0])
        pegar2=int(separacao[1])
        
        if (1 <= pegar1) and (1 <= pegar2) and (pegar1<= 1000) and (pegar2 <= 1000):
            ResultOfficial = (pegar1 - pegar2)
            Resultado.write("Caso %d: %d\n" % ((x+1),ResultOfficial))
            
Resultado.seek(2)
Resultado.write("\n")
Resultado.close
        
