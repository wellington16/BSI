# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:21:36 2016

@author: WELLINGTON
"""
#037 -- Programa gerador de permutação iterativamente.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

#função fatorial
def fat(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        fat = n
        for i in range(1, n):
            fat = fat * i
        return fat
#fim da função fatorial

# Início do programa

a = input("Digite a lista A: ")
for i in range(0, fat(len(a))):
    l = i
    a2 = []
    a2.extend(a)
    temp = []
    for j in range(len(a), 0, -1): # De trás pra frente
            d = fat(j - 1)
            p = l / d
            l = l % d
            temp.append(a2[p])
            del a2[p]
    print(temp)
#fim do programa