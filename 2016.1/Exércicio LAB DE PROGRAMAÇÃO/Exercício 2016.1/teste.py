#Autor Wellington
import sys


#entrada com hardcode
entrada = open('entrada.txt', 'r')
saida = open('saida', 'w')

#entrada sem HARDCODE
entrada = open(sys.argv[1], 'r')
saida = open(sys.argv[2], 'w')


#leitura do arquivo
l= []
while True:
    linha  = entrada .readline() 
    if linha == '':
        break
    l.append(int(linha))
def funcao(x):
    m = 1
    for i in x:
        m = m * i
    return m
resultado = funcao(l)

#escrever resultado
saida.write(str(resultado))


print('resultado: ' + str (resultado),'\n')

saida.close()
entrada.close()        