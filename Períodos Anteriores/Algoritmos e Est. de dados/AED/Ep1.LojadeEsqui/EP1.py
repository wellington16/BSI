'''
Wellington Luiz Antonio
EP - 1
14/09/2015
Algoritmos e Estrutura de Dados
'''

def ordenacaoMSort(L):
    
    '''ordena a lista que pista recebe em grau Teta(n log 2n) no pior caso. "dividir e conquista!" 
       Devolve a lista ordenada para pista.
    '''
    
    if len(L) > 1: # Divide L em duas listas 
        medio = len(L)//2
        metadeEsq = L[:medio]
        metadeDir = L[medio:]
        ordenacaoMSort(metadeEsq)#chama varias vezes metade esquerda de L na função ordenacaoMSort até ela devolver Nulo.
        ordenacaoMSort(metadeDir)#chama varias vezes metade direita de L na função ordenacaoMSort até ela devolver Nulo.

        x = y = z = 0
        
        while x < len(metadeEsq) and y < len(metadeDir):#Verifica se esta ordenada, se não, a ordena. 
            if metadeEsq[x] < metadeDir[y]:
                L[z] = metadeEsq[x]
                x = x + 1
            else:
                L[z] = metadeDir[y]
                y = y + 1
            z = z + 1

        while x < len(metadeEsq):
            L[z] = metadeEsq[x]
            x = x + 1
            z = z + 1

        while y < len(metadeDir):
            L[z] = metadeDir[y]
            y = y + 1
            z = z + 1

        return(L)

def pista(L):
    
    '''Recebe uma lista de inteiros e
    Devolve a posição da pista onde começa o
    trecho atingido pela avalanche'''
    
    p = L[0] #primeiro item da lista
    del(L[0])
    L2 = L[:]
    pos = 0

    ordenacaoMSort(L)
    
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
        print(pos, vazio)# imprime a posição e o trecho atingido pela avalanche já ordenado.

  
#abri o arquivo e ler, retira o "\n" e fecha o arquivo
entrada = open("esqui.dat", "r") 
string = entrada.read()
linhas = string.split("\n")
entrada.close()

for x in range(len(linhas)):#transforma uma lista de strings em uma lista de inteiros
    sem_espaco = linhas[x].split(" ")
    for y in range(len(sem_espaco)):
        sem_espaco[y] = int(sem_espaco[y])
    pista(sem_espaco)
