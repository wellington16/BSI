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

def ordenacaoBBsort(L,E):
    '''ordena a lista L que pista recebe e não ordena a lista E.
       Devolve a lista L(Abcissa = x) ordenada e a lista E(ordenada = y) não ordenada .
    '''
    for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                E[i], E[i + 1] = E[i + 1], E[i]
                for i in range(len(L) - 1):
                    if L[i] > L[i + 1]:
                        L[i], L[i + 1] = L[i + 1], L[i]
                        E[i], E[i + 1] = E[i + 1], E[i]
                    for i in range(len(L) - 1):
                       if L[i] > L[i + 1]:
                           L[i], L[i + 1] = L[i + 1], L[i]
                           E[i], E[i + 1] = E[i + 1], E[i]

def distancia(abcissa1, ordenada1, abcissa2, ordenada2):
    '''Calcula a distancia entre duas cidades
        Devolve a distancia de cada cidade'''

    distancia = float(((abcissa2 - abcissa1)**2 + (ordenada2 - ordenada1)**2)**0.5)
    
    return distancia

#abrir o arquivo e ler, retira o "\n" e fecha o arquivo, é onde o programa faz a leitura do arquivo como string.------------
entrada = open("trembala.dat", "r")

while True:
    '''ler  cada linha do arquivo de entrada e da um break se encontrar 0,
     deopois transforma todas as linhas em inteiros.'''
    N = entrada.readline()
    N = int(N)

    if N == 0:
        break
    x = entrada.readline()
    x = x.split(" ")
    abcissa = [int(i) for i in x]

    y = entrada.readline()
    y = y.split(" ")
    ordenada = [int(i) for i in y]
#----------------------------------------------------------------------------------------------------------------------------
    ordenacaoBBsort(abcissa,ordenada)

    compara_d = (N * 100000)
    menor_dist = [] # Lista de distância entre as cidades
    
    # pega duas cidades e calcula a distância entre elas
    for i in range(N): 
        for j in range(N):
            receb_distancia = distancia(abcissa[i], ordenada[i], abcissa[j], ordenada[j])
            if (abcissa[i], ordenada[i]) == (abcissa[j], ordenada[j]): #compara as distâncias para saber se são iguais
                continue
            elif compara_d > receb_distancia:#compara se "m" é maior que a distancia "d"
                compara_d = receb_distancia # Se for "m" maior então "m" recebe essa distancia "d" 
            #-cidade1(x1,y2)---------------------------------------
                abcissa1 = abcissa[i] 
                ordenada1 = ordenada[i]
            #-cidade2(x2,y2)---------------------------------------
                abcissa2 = abcissa[j]
                ordenada2 = ordenada[j]
   
            menor_dist.append(receb_distancia) # adiciona a distância na lista. 
            ordenacaoMSort(menor_dist) # organização a Lista de distância entre cidades

    #imprime o resultado
    print("Distância entre as cidades %d, %d e %d, %d : %.2f" % (abcissa1,ordenada1,abcissa2,ordenada2,menor_dist[1]))#cidade1(x1,y2),cidade2(x2,y2) e menor distância entre as cidades.


entrada.close()
