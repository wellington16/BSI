# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:59:06 2016

@author: WELLINGTON
"""

#039 -- Programa de Algoritmo por Seleção.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
from datetime import datetime
#A = input("Digite a lista a ser ordenada:  " )
A= []
l = 1000

def selct(l):
    for i in range(l):A.append(l - i)
    for i in range(len(A)):
        posMenor = i
        for j in range(i + 1, len(A)):
            if A[posMenor] > A[j]:
                posMenor = j
        temp = A[i]
        A[i] = A[posMenor]
        A[posMenor] = temp
        
inicio = datetime.now()
B = selct(l)
fim = datetime.now()
duracao = fim - inicio
print("Lista ordenada : ", A)
print("Feito em ",duracao.seconds, "segundos",\
 duracao.microseconds, "microsegundos")
        
    


#fim do programa