import sys
import os # Biblioteca de funções do sistema operacional

# Limpar o video
if  sys.platform.startswith("Win32"): 
    os.system("cls") # No windows
elif  sys.platform.startswith('Linux'): 
    os.system("clear") # No linux ou mac os

#Autor : Wellington Luiz 

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 3 - Laboratório de Programação
    titulo: Batalha Naval com Juvenal. Olha só rimou. Kkkkk
    Executado em python 3.4
'''
try:
    #funcao recursiva
    def busca(x,y):
        
        #deleta x,y da lista de tiros
        listdTiros.remove([x,y])
        
        #variavel de retorno
        afundou = True
        
        #olhando para meus vizinhos
        #casos base da recursao
        if x + 1 <= n - 1:
            if tabuleiro[x+1][y] == "#":
                afundou = False

        if y + 1 <= m - 1:
            if tabuleiro[x][y + 1] == "#":
                afundou = False
                
        if x - 1 >= 0:
            if tabuleiro[x - 1][y] == "#":
                afundou = False
                
        if y - 1 >= 0:
            if tabuleiro[x][y - 1] == "#":
                afundou = False
                
        #Entro na recursividade ou não?
        if x + 1 <= n - 1 and afundou == True:
            if tabuleiro[x + 1][y] == "*" and [x + 1, y] in listdTiros:
                #recursao aqui
                afundou = busca(x + 1, y)
                
        elif x - 1 >= 0 and afundou == True:
            if tabuleiro[x - 1][y] == "*" and [x - 1, y] in listdTiros:
                #recussao aqui
                afundou = busca(x - 1, y)
                
        elif y + 1 <= m - 1 and afundou == True:
            if tabuleiro[x][y + 1] == "*" and [x, y + 1] in listdTiros:
                #recursao aqui
                afundou = busca(x, y + 1)
                
        elif y - 1 >= 0 and afundou == True:
            if tabuleiro[x][y - 1] == "*" and [x, y - 1] in listdTiros:
                #recursao aqui
                afundou = busca(x, y - 1)
                
        #retorna afundou
        return (afundou)


    #inico do corpo principal

    #leitura do arquivo sem HARDCODE
    #arqent = open(sys.argv[1], 'r')
    #arqsaida = open(sys.argv[2], 'w')

    #leitura do arquivo com HARDCODE
    arqent = open('input.txt',"r")
    arqsaida = open('output.txt',"w")

    n, m = arqent.readline().strip().split(" ")
    n, m = int(n), int(m)
    #print(n,m)

    #Construindo o campo de jogo
    tabuleiro=[]
    for c in range(n):
        lista = []
        string = arqent.readline().strip()
        for d in range(m):
            lista.append(string[d])
            #print(lista)
        tabuleiro.append(lista)

    NumVisitas = 0
    QNavios = 0

    tiros = arqent.readline().strip()
    tiros = int(tiros)
    listdTiros=[]

    #carrega um tiro do arquivo e processando-o
    for cont in range(tiros):
        tirox, tiroy = arqent.readline().strip().split(" ")
        tirox = int(tirox)-1
        tiroy = int(tiroy)-1
        #so processa o tiro se ele nao for na agua
        if tabuleiro[tirox][tiroy] == "#":
            NumVisitas += 1
            #guarda tiro
            listdTiros.append([tirox, tiroy])
            tabuleiro[tirox][tiroy] = "*"

    while True:
        #tiros que acertaram o alvo...
        if len(listdTiros) == 0:
            #lista de tiros já foi processada
            break
        #pega primeiro elemento da lista de tiros
        tirox, tiroy = listdTiros[0]

        #inicia procura recursiva
        afundou = busca(tirox,tiroy)
        if afundou == True:
            QNavios += 1

    print ("Navios afundados: %d" %(QNavios))
    arqsaida.write(str(QNavios)+"\n")

#tratando erro de entrada
except IndexError as e:
    arqsaida.write("Reveja o código")

#fechando o arquivo
arqent.close()
arqsaida.close()
#fim do programa  

