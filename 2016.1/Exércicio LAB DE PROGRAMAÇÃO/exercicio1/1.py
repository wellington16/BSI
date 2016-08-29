entrada=open('L0Q1.in', 'r')
string=entrada.read()
linhas=string.split('\n')
entrada.close()

saida=open('L0Q1.out', 'w')

T=int(linhas[0])

for i in range (T):
    AeC=linhas[i+1].split(' ')
    A=int(AeC[0])
    C=int(AeC[1])
    B=0

    for b in range(0,C):
        if ((A * b)%C)==1:
            B=b

    if B==0:
        saida.write('Caso %d: muito difícil\n' %(i+1))
    elif B!=0:
        saida.write('Caso %d: %d\n' % (i+1, B))

saida.close()
