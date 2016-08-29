# coding:utf-8
import sys
import os # Biblioteca de funções do sistema operacional
# Limpar o video
os.system("clear") # No linux ou mac os
os. system("cls") # No windows

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 1 - Laboratório de Programação
    Esse programa recebe um arquivo string
    e visa achar o inverso modular de numero retornando-o'
    Executado em python 3.5
'''
try:
    #leitura do arquivo sem HARDCODE
    arqentrada = open(sys.argv[1], 'r')
    arqsaida = open(sys.argv[2], 'w')

    #Tratamento e leitura com com hardcode
    #arqentrada= open('entrada.txt', 'r')
    TEntString = arqentrada.read()
    linhas = TEntString.split('\n')

    
    #arqsaida=open('saida.txt', 'w')

    #programa pricipal(núcleo)
    T = int(linhas[0])
    if (T >= 1) and (T <= 1000):
        for caso in range (T):
            AC = linhas[caso + 1].split(' ')
            valorA = int(AC[0])
            valorC = int(AC[1])
            valorB = 0
            if ((valorA >= 1) and (valorA <= 10000)):
                if ((valorC >= 1) and (valorC <= 1000)):
                    for x in range(valorC):
                        if ((valorA * x)% valorC)== 1:# Calculo do mod para achar o valorB
                            valorB = x
                    if valorB != 0:
                        arqsaida.write('Caso %d: %d\n' % (caso + 1, valorB))
                        print('Caso %d: %d\n' % (caso + 1, valorB))        
                    elif  valorB == 0:
                        arqsaida.write('Caso %d: muito difícil\n' %(caso + 1))
                        
                elif ((valorA >= 1) and (valorA <= 10000)) == False:
                    arqsaida.write('Caso %d: A (%d) está fora do intervalo permitido (1 <= A <= 10000)\n' % ((caso + 1), valorA))
                    
                elif ((valorC >= 1) and (valorC <= 1000)) == False:
                    arqsaida.write('Caso %d: C (%d) está fora do intervalo permitido (1 <= C <= 1000)\n' % ((caso + 1), valorC))
            
    else:
        print(" 'T' (%d) está fora do intervalo permitido(1<=T<=1000)" % T)

#tratando erro de entrada
except IndexError as e:
    print(str("Digite o endereço correto para o arquivo."))
    print(str(e))
    
#fechando o arquivo
arqsaida.write(str('\n'))
arqsaida.close()
arqentrada.close()

#fim do programa
