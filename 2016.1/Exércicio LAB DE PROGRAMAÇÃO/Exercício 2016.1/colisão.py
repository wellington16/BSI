#Autor Wellington
import sys

#leitura do arquivo com hardcode
entrada = open('entrada.txt', 'r')
saida = open('saida.txt', 'w')

#Tratamento
aqentrada = entrada.read()
aqentrada = aqentrada.split('\n')
listaA = listaB =[] 
listaA = aqentrada[0]
listaB = aqentrada[1]
a = []
b = []
for i in range (len(listaA)):
    a.append(listaA[i])
for j in range (len(listaA)):
    b.append(listaB[j])
    

#entrada sem HARDCODE
#entrada = open(sys.argv[1], 'r')
#saida = open(sys.argv[2], 'w')

print(aqentrada)



Ax1 = a[0]
Ax2 = a[4]
Ay1 = a[2]
Ay2 = a[6]

Bx1 = b[0]
Bx2 = b[4]
By1 = b[2]
By2 = b[6]

if (Bx1 > Ax2) or (Ax1 > Bx2) or (By1 > Ay2) or (Ay1 > By2):
    saida.write(str('0'))
else:
    saida.write(str('1'))

saida.close()
entrada.close()   
