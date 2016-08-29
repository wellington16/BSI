#coding:utf8
#
#028 -- Programa para Horas, Minutos, Segundos(Relógio).
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
i = 0

while i < 24:
    j = 0
    while j < 60:
        k = 0 
        while k < 60:
            print( i ," : ", j, " : ",k )
            k += 1
        j += 1
    i += 1

#fim do programa
