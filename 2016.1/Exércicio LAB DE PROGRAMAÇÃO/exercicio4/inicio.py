entrada=open('E4.in', 'r')
string=entrada.read()
string2=string.split('\n')
entrada.close()
saida=open('E4.out', 'w')
N=int(string2[0])

#soma das linhas
if ( N<=10) and (N>=2):
    linhax=[]
    for j in range (N):
        soma=0
        for i in range (N):
            linha=string2[j+1].split(' ')
            linhax.append(int(linha[i]))
            soma+=int(linha[i])
            print(i)
            print('-----',soma)

#soma das colunas


'''if (N <=10) and (N>=2):
    coluna=[]
    for j in range (N):
        i=0
        while i < (N):
            index=string2[j+1].split(' ')
            coluna.append(int(index[j][i]))
            print (coluna)
            i+=1
    j=j+1
            
           
            # for x in range(N):
           #     linha2=string2[j+1]
            #    print(linha2)
            
    print(coluna)
            #print(j)
            #print('-----',soma)
    
print(coluna)'''

#soma das diagonas
