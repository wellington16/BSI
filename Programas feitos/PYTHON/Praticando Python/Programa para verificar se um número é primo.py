#coding:utf8
#
# Programa para verificar se um número é primo
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

valor = int(input("Digite um número "))
i = 2
numeroDiv = 0 # contar o número de divisões exatas
numeroCompar = 0 # contar quantas divisões/comparações 
while i <= valor/2:
    print(i)
    numeroCompar += 1
    if valor % i == 0:
        numeroDiv += 1
    i += 1
if numeroDiv ==0:
    print("O número fornecido é primo")

else:
    print("O número fornecido possui ", numeroDiv,"divisores")

print("Número de comparações realizadas = ",numeroCompar)
      
#fim do programa
