inicio=open('E4.in', 'r')
string=inicio.read()
arrumar=string.split('\n')
inicio.close()

resultado=open('E4.out', 'w')
N=int(arrumar[0])

#funçao adicionar na lista
def Add(self):
    linhax.append(self)

#soma da linha
linhax=[]
if (N<=10) and (N>=2):
    for j in range (N):
        somalin=0
        for i in range (N):
            linha=arrumar[j+1].split(' ')
            somalin+=int(linha[i])
        Add(somalin)

#soma da coluna
for z  in range(N+(N-1)):
        somacol=0
        for x in range (N):
            if (arrumar[x+1][z])!=" ":
                somacol+=int(arrumar[x+1][z])
        if somacol != 0:
            Add(somacol)
   
#soma da diagona
for v in range((N+(N-1))-2):
            somadiag=0
            cont=0
            while cont < (N+(N-1)):
                if (arrumar[v+1][cont])!=" ":
                    somadiag= somadiag +(int(arrumar[v+1][cont]))
                    cont+=2
            if somadiag != 0:
                Add(somadiag)
#função cancelar o True
def cancelartrue():
    qaudradox=False
    pass
                                             
#status
quadradox=True
for b in range(len(linhax)-1):
    if linhax[b]==linhax[0]:
        pass
    else:
        quadradox=False

if quadradox:
        resultado.write(str(linhax[0]))
        resultado.write('\n')
else:
    resultado.write('ERRO\n')                         
resultado.close()
