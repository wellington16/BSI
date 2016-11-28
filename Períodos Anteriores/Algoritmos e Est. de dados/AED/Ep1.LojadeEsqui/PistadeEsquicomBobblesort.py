'''
Wellington Luiz Antonio
EP - 1
14/09/2015
Algoritmos e Estrutura de Dados
'''

def ordenacaoBBsort(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            L[i], L[i + 1] = L[i + 1], L[i]
            for i in range(len(L) - 1):
                if L[i] > L[i + 1]:
                    L[i], L[i + 1] = L[i + 1], L[i]
                for i in range(len(L) - 1):
                    if L[i] > L[i + 1]:
                        L[i], L[i + 1] = L[i + 1], L[i]
    return(L)

def pista(L):
    
    '''Recebe uma lista de inteiros e
    Devolve a posição da pista onde começa o
    trecho atingido pela avalanche'''
    
    p = L[0] #primeiro item da lista
    del(L[0])
    L2 = L[:]
    pos = 0

    ordenacaoBBsort(L)
    
    for j in range(len(L) - 1):#verifica a posição e o trecho afetado
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
        vazio = ''
        for f in L: # Transforma a lista de Inteiros em uma lista strings  
            vazio = vazio + ' ' + str(f)
        print(pos, vazio)# imprime a posição e o trecho atingido pela avalanche
  
#abri o arquivo e ler, retira o "\n" e fecha o arquivo
entrada = open("E1.txt", "r") 
string = entrada.read()
linhas = string.split("\n")
entrada.close()

for x in range(len(linhas)):#transforma uma lista de strings em uma lista de inteiros
    sem_espaco = linhas[x].split(" ")
    for y in range(len( sem_espaco)):
        sem_espaco[y] = int( sem_espaco[y])
    pista( sem_espaco)
