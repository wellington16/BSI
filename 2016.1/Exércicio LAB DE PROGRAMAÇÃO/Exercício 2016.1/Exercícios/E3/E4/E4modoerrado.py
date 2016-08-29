#coding:utf8
#
'''
Exercício 4 - Laboratório de Programação
O programa recebe um arquivo (string)
e verifica qual peça(numero) está faltando no arquivo'''
#import sys


#Autor: Wellington Luiz


#leitura do arquivo com hardcode
entrada = open('entrada.txt', 'r')
saida = open('saida.txt', 'w')

#leitura do arquivo sem HARDCODE
#entrada = open(sys.argv[1], 'r')
#saida = open(sys.argv[2], 'w')

#Tratamento
#linha 1
aqentradalinha1 = entrada.readline()
aqentradalinha1 = aqentradalinha1.split()
aqentradalinha1= [int(i) for i in aqentradalinha1]

#linha 2
aqentradalinha2 = entrada.readline()
aqentradalinha2 = aqentradalinha2.split()
aqentradalinha2 = [int(j) for j in aqentradalinha2]

#programa principal
if 2 <= aqentradalinha1[0] <= 1000:
    def peca(i,j):
        for i in aqentradalinha2:
            for j in aqentradalinha2:
                if (j - i)== 1:
                    pass
                elif i < 1 or j < 1 :
                    saida.write(str('Nao estamos trabalhando com numeros menores que 1'))  
                elif(j - i) > 1:
                    print(j+1)
                    saida.write(str(j+1))
                    break
                elif aqentradalinha2[0] > 1:
                    print(aqentradalinha2[0] - 1)
                    saida.write(str(aqentradalinha2[0] - 1))
                    break
            saida.write("\n")
            break
    soguardar = peca(aqentradalinha2,aqentradalinha2)
                            
#fechando o arquivo
saida.close()
entrada.close()
#fim do programa
