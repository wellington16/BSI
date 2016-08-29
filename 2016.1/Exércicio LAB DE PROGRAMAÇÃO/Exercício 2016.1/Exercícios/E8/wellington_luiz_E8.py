import sys
import os # Biblioteca de funções do sistema operacional
# Limpar o video
if sys.platform.startswith("Win32"):
    os. system("cls") # No windows
elif sys.platform.startswith("Linux"):
    os.system("clear") # No linux ou mac os


#Autor Wellington Luiz

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 2 - Laboratório de Programação
    título: Times.
    O seu antigo professor de educação física pediu para ele escrever um programa que,
    dada uma lista de alunos que serão escolhidos e seus respectivos níveis de habilidade para os times
    e a quantidade de times que serão formados.
    Executado em python 3.4
'''

try:
    def Cresc(lista):
        tamlist = len(lista)
        for x in range(tamlist - 1):
            Min = x
            for j in range(x + 1, tamlist):
                if (lista[j] < lista[Min]):
                    Min = j
            lista[x],lista[Min]=lista[Min],lista[x]
        return (lista)

    def Decresc(lista):
        tamlist = len(lista)
        print(lista)
        for x in range(tamlist - 1):
            Min = x
            for j in range(x + 1,tamlist):
                if (lista[j] > lista[Min]):
                   Min = j
            lista[x],lista[Min]=lista[Min],lista[x]
        return (lista)
        

    #leitura do arquivo sem HARDCODE
    #arqentrada = open(sys.argv[1], "r")
    #arqsaida = open(sys.argv[2], "w")
    
    #leitura do arquivo com hardcode
    arqentrada = open('entrada.txt', "r")
    arqsaida = open('saida.txt', "w")

    #Tratamento
    linha1 = (arqentrada.readline()).split()
    quantAlunos = int(linha1[0])
    quantTimes = int(linha1[1])
    cont = 0
    listaAlunos = []
    
    # "núcleo" do programa
    #restrição de N e T.
    if 2 <= quantAlunos <= 10000: # N
        if 2 <= quantTimes <= 1000: # T
            while cont < quantAlunos:
                x = (arqentrada.readline()).split()
                #print(x)
                x[1] = int(x[1])
                x[0], x[1] = x[1], x[0]
                listaAlunos.append(x)
                cont += 1
                #print(listaAlunos)
            guardar1 = Decresc(listaAlunos)

            for index in range(1,quantTimes+1):
                listaTempNome = []
                arqsaida.write("Time %d\n" % index)
                
                for j in range(index - 1,len(listaAlunos), quantTimes):
                    listaTempNome.append(listaAlunos[j][1])
                    #print(listaTemp)
                guardar2 = Cresc(listaTempNome)
                
                for l in range(len(listaTempNome)):
                    arqsaida.write(listaTempNome[l]+"\n")
                    #print(listaTempNome[l])
                arqsaida.write("\n")
        
#tratando erro de entrada
except IndexError as e:
    arqsaida.write(str("Reveja o código."))
    arqsaida.write(str(e))

#fechando os arquivos
arqentrada.close()
arqsaida.close()

#Fim do programa
