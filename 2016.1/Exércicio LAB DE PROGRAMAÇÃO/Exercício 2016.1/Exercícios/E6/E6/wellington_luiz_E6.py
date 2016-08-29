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
    def Busca(x,y):
        
        #deleta x,y da lista de tiros
        listdTiros.remove([x,y])
        
        #variavel de retorno
        afund = True
        
        #olhando pros vizinhos
        #casos base da recursao
        if x + 1 <= a - 1:
            if tabuleiro[x + 1][y] == "#":
                afund = False
                
        if x - 1 >= 0:
            if tabuleiro[x - 1][y] == "#":
                afund = False
                
        if y + 1 <= b - 1:
            if tabuleiro[x][y + 1] == "#":
                afund = False
                
        if y - 1 >= 0:
            if tabuleiro[x][y - 1] == "#":
                afund = False
                
        #Entro na recursividade ou não?
        if x + 1 <= a - 1 and afund == True:
            if tabuleiro[x + 1][y] == "*" and [x + 1, y] in listdTiros:
                #recursao aqui
                afund = Busca(x + 1, y)
                
        if x - 1 >= 0 and afund == True:
            if tabuleiro[x - 1][y] == "*" and [x - 1, y] in listdTiros:
                #recussao aqui
                afund = Busca(x - 1, y)
                
        if y + 1 <= b - 1 and afund == True:
            if tabuleiro[x][y + 1] == "*" and [x, y + 1] in listdTiros:
                #recursao aqui
                afund = Busca(x,y+1)
                
        if y - 1 >= 0 and afund == True:
            if tabuleiro[x][y - 1] == "*" and [x, y - 1] in listdTiros:
                #recursao aqui
                afund = Busca(x, y - 1)

        #retorna afundou
        return (afund)

    # Núcleo do programa
    #leitura do arquivo sem HARDCODE
    arqent = open(sys.argv[1], 'r')
    arqsaida = open(sys.argv[2], 'w')

    #leitura do arquivo com HARDCODE
    #arqent = open('entrada.txt',"r")
    #arqsaida = open('saida.txt',"w")

    a, b = arqent.readline().strip().split(" ")
    a, b = int(a),int(b)
    #print (a,b)

    #Construindo o campo de jogo
    tabuleiro=[]
    for c in range(a):
        lista = []
        string = arqent.readline().strip()
        for d in range(b):
            lista.append(string[d])
        tabuleiro.append(lista)

    NumVisitas = 0
    QNaviosAfundados = 0

    tiros = arqent.readline().strip()
    tiros = int(tiros)
    listdTiros = []

    #carrega um tiro do arquivo e processando-o
    for cont in range(tiros):
        tirox, tiroy = arqent.readline().strip().split(" ")
        tirox = int(tirox)-1
        tiroy = int(tiroy)-1
        #print tirox, tiroy
        #so processa o tiro se ele nao for na agua
        if tabuleiro[tirox][tiroy] == "#":
            NumVisitas += 1
            #guarda tiro
            listdTiros.append([tirox, tiroy])
            tabuleiro[tirox][tiroy] = "*"

    while True:
        # Tiros que acertaram alvo...
        if len(listdTiros) == 0:
            #Lista de tiros foi processada
            break
        
        #pega primeiro elemento da lista de tiros
        tirox, tiroy = listdTiros[0]
        #inicia procura recursiva
        afundou = Busca(tirox, tiroy)
        if afundou == True:
            QNaviosAfundados += 1
            
    arqsaida.write(str(QNaviosAfundados)+"\n")
    print ("Total Visitas: %d" %(NumVisitas))
    print ("Navios afundados: %d" %(QNaviosAfundados))
    
#tratando erro de entrada
except IndexError as e:
    arqsaida.write("Reveja o código")

#fechando o arquivo
arqent.close()
arqsaida.close()

#fim do programa  

