entrada=open('E3.in', 'r')
transf=entrada.read()
quebrar=transf.split('\n')
entrada.close()
saida=open('E3.out', 'w')

T=int(linhas[0])

if (T >=1) and (T<=1000):
    for i in range (T):
        AeB=linhas[i+1].split(' ')
        A=int(AeB[0])
        B=int(AeB[1])
        #implementar restrição 1 <= A,B <= 1000
        C=A-B
        saida.write('Caso %d: %d\n' % ((i+1),C))

saida.close()
