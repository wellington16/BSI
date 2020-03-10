#coding:utf8
#
#035 -- Programa faz uma permutação de uma lista de tamanho 3.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

lista =['a','b','c']
for i in lista:
    for j in lista:
        for k in lista:
            if i != j and j != k and i != k: print(i," : ", j," : ",k)
#fim do programa
