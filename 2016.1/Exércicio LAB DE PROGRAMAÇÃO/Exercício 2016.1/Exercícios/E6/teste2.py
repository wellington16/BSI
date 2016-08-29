l=['..#.#','#...,','...#.','.##..','...#.']

def buscL(ab,listaM):
        for h in range(len(listaM)):
            for i in listaM:
                print('é h:',)
                if i[0] == ab :
                    print(i[0])
            listaM[h].append(ab)
listaM=[]
def antVert(j,i, g):
    x= j - i
    if x =='#':
        print(g[x])
        return(x)

for i in l:
    for j in range(len(i)):
        listad = []
        if i[j] == '#':
            listad.append(i[j])
            print('aqui: ',j)
            if j == 0:
                print('É igual a',j)
            elif j!= 0:
                ant(ab, listaM)
        #antVert(j, len(i), i)
        listaM.append(listad)
print(listaM)
