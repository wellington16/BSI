#coding:utf8
#
# Programa para adicionar elementos em uma lista
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

vetor = []
n = int(input("Digite a quantidade de elementos a ser adicionada"))
i= 0
while i < n:
    temp = input("Digite o elemento a ser adicionada -> ")
    vetor.append(int(temp))
    i = i + 1
print("Vetor = ", vetor)

#fim do programa
