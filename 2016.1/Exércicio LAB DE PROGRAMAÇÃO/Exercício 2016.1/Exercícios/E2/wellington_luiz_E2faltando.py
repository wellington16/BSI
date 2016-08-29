
import sys
import os # Biblioteca de funções do sistema operacional
# Limpar o video
os.system("clear") # No linux ou mac os
os. system("cls") # No windows

#Autor Wellington Luiz

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 2 - Laboratório de Programação
    título: Colisões
    O programa recebe as coordenadas de dois retangulos
    e verifica se os retangulos colidem em algum momento.
    Executado em python 3.5
'''

try:
    #leitura do arquivo sem HARDCODE
    entrada = open(sys.argv[1], 'r')
    saida = open(sys.argv[2], 'w')

    #leitura do arquivo com hardcode
    #entrada = open('entrada.txt', 'r')
    #saida = open('saida.txt', 'w')

    #Tratamento
    aqentrada = entrada.read()
    aqentrada = aqentrada.split('\n')
    listaA = listaB = [] 
    listaA = aqentrada[0]
    listaB = aqentrada[1]
    listaA = listaA.split(' ')
    listaB = listaB.split(' ') 

    #Retangulo A
    retanAx1 = int(listaA[0])
    retanAx2 = int(listaA[2])
    retanAy1 = int(listaA[1])
    retanAy2 = int(listaA[3])

    #Retangulo B
    retanBx1 = int(listaB[0])
    retanBx2 = int(listaB[2])
    retanBy1 = int(listaB[1])
    retanBy2 = int(listaB[3])


    #verificação (colide ou não) "núcleo" do programa
    if (retanAx1 > retanBx2) or (retanBx1 > retanAx2) or (retanBy1 > retanAy2) or (retanAy1 > retanBy2):
        saida.write(str('0'))
    else:
        saida.write(str('1'))
        

    #fechando o arquivo
    saida.write("\n")
    saida.close()
    entrada.close()
#tratando erro de entrada
except IndexError as e:
    print("Digite o endereço correto para o arquivo.")
    print(e)
#fim do programa
