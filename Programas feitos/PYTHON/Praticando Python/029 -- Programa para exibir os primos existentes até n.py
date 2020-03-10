#coding:utf8
#
#029 -- Programa para exibir os primos existentes até n.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

q =int(input("Digite um número limite  "))
for i in range(2, q):
    for j in range (2, i):
        if i % j == 0:
            print(i," igual a ", j," * ", i/j)
            break
    else:
        #Programa chegou aqui por não ter executado
        print( i," é um número primo ")


#fim do programa
