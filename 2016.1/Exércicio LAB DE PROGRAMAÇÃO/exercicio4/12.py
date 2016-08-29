entrada=open('E4.in', 'r')
string=entrada.read()
string2=string.split('\n')
entrada.close()
saida=open('E4.out', 'w')
N=int(string2[0])
somas=[]

#soma das linhas
if (N >=2) and (N<=10):
    for i in range (N):
        linhas=0
        for j in range (N):
            linha=string2[i+1].split(' ')
            linhas+=int(linha[j])
        somas.append(linhas)
        print('---',linhas)

#soma das colunas
for x in range (N+(N-1)):
    colunas=0
    for y in range(N):
        if (string2[y+1][x])!=' ':
            colunas+=int(string2[y+1][x])
    if colunas!=0:
        somas.append(colunas)
        print('|||',colunas)

#soma das diagonais
for c in range ((N+(N-1))-2):
    diagonais=0
    z=0
    while z<(N+(N-1)):
        if (string2[c+1][z])!=' ':
            diagonais+=int(string2[c+1][z])
            z+=2
    if diagonais!=0:
        somas.append(diagonais)
        print('///',diagonais)

#verificação
quadrado_magico=True
for v in range(len(somas)-1):
    if somas[v]==somas[0]:
        pass
    else:
        quadrado_magico=False

if quadrado_magico:
    saida.write(str(somas[0]))
else:
    saida.write('-1')
