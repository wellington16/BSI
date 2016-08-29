import sys

#inicio, lendo o arquivo
arquivo=open(sys.argv[1],"r")
lista= arquivo.readlines()
arquivo.close()

#abrindo arquivo para a escrita
resultado= open(sys.argv[2],"w")
t= int(lista[0])

#restrição
if t<=100 or t>= 1:
    resultado.write('Você ultrapassou a quantidade de numeros de casos.\nTem que ser menor que 100 e maior que 1.\n') 

#função1
a=0
def f(n):
    global a
    if n == 1:
        a+=1
        x= 1
        
    elif n%2 ==0:
        a+=1
        x=f(n/2)
             
    elif n%2 == 1 is n > 1:
        a+=1
        x= f(3*n+1)
    return a

#função2
def g(x,y):
    if x <=1 or x>=y or x>=10**5:
        resultado.write("O primeiro argumento não pode\nser maior que o segundo e maior 100000")  
    else:
        v1=0
        p=0
        for w in range(x,y):
            agora=f(z)
            if agora>v1:
                v1=agora
                p = w
            return v1

#organizador          
for k in range(t):
        separacao= lista[k+1].split(' ')
        x=(int(separacao[0]))
        y=(int(separacao[1]))
        pegar=g(x,y)
        resultado.write("caso %d: %d\n"%((i+1),pegar))
resultado.close()


