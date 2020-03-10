#coding:utf8
#
# Programa para calcular a a tabuada de multiplicar.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
i = 1

while i <= 10:
    j = 1
    while j <= 10:
        print( i ," * ", j, " = ", i*j)
        j += 1
    i += 1
    if i <= 10:
        print()
        print( "Por", i)
        print()

#fim do programa
