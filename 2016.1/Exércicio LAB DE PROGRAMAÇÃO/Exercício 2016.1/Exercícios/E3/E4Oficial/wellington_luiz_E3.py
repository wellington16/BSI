
import sys
import os # Biblioteca de funções do sistema operacional
# Limpar o video
os.system("clear") # No linux ou mac os
os. system("cls") # No windows

#Autor : Wellington Luiz 

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 3 - Laboratório de Programação
    titulo: Perça perdida
    O programa recebe um arquivo e
    verifica qual peça(numero) está faltando no arquivo
    Executado em python 3.5
'''

try:
    #leitura do arquivo sem HARDCODE
    aqent = open(sys.argv[1], 'r')
    aqsaida = open(sys.argv[2], 'w')
    
    linha1 = aqent.readline()
    linha2 = aqent.readline()
    aqent.close()

    #linha 1
    linha1 = linha1.split('\n')
    linha1= int(linha1[0])

    #linha 2
    linha2 = linha2.split(' ')
    linha2 = [int(x) for x in linha2]
    #print(linha2)

    #programa principal
    Z =[]
    for i in range(linha1 + 1):
        Z.append(i)
    Z.remove(Z[0])
    #print(k)
    if (1<= linha1<=1000):
        def intersecao(Z,linha2):
            return[x for x in Z if x not in linha2]
            
        resultado= intersecao(Z,linha2)
        aqsaida.write(str(resultado[0]))
    
#tratando erro de entrada
except IndexError as e:
     aqsaida.write("Digite o endereço correto para o arquivo")
     aqsaida.write(str(e))

#fechando o arquivo
aqsaida.write("\n")     
aqsaida.close()
#fim do programa        

