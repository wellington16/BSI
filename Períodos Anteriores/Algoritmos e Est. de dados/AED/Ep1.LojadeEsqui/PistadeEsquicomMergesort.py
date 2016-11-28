'''
Wellington Luiz Antonio
EP - 1
14/09/2015
Algoritmos e Estrutura de Dados
'''

def mergeSort(L):
    if len(L)>1:
        mid = len(L)//2
        lefthalf = L[:mid]
        righthalf = L[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                L[k]=lefthalf[i]
                i=i+1
            else:
                L[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            L[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            L[k]=righthalf[j]
            j=j+1
            k=k+1

        return(L)


def pista(L):
    p = L[0] #primeiro item da lista
    del(L[0]) 
    L2 = L[:]
    pos = 0

    mergeSort(L)

    for j in range(len(L)-1):#verifica a posição do erro
        if L[j] == L2[j]:
            continue
        else:
            pos = j + 1
            break
        
    #imprime o resultado    
    if  p == 0:
        pass
    elif L == L2 and p != 0:
        print("-1")
    else:
        #print(pos,L)
        #print(type(L[0]))
        g = ''
        for f in L:
            g = g + ' ' + str(f)
        print(pos, g)


entrada = open("E1.txt", "r")
string = entrada.read()
linhas = string.split("\n")
entrada.close()

for x in range(len(linhas)):
    sem_espaco=linhas[x].split(" ")
    for y in range(len(sem_espaco)):
        sem_espaco[y] = int(sem_espaco[y])
    pista(sem_espaco)
