# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:21:53 2016

@author: WELLINGTON
"""

#041 -- Programa de Algoritmo por borbulhamento.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
from datetime import datetime
import random
random.seed()
l = input("Digite o tamanho da lista :  " )
A= []
#Gerando a lista a ser utilizada 
i = 0
while i < l:
    x = random.randint(1, l)
    if x not in A:
        A.append(x)
        i += 1
print("-------------------")
print("Lista Original ")
print(A)

perms = True
inicio = datetime.now()
while perms:
    perms = False
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            perms = True

fim = datetime.now()
duracao = fim - inicio
print('----------------------')
print("Lista ordenada : ")
print(A)
print('----------------------')
print("tempo(ms): %2.8f" % float(duracao.seconds * 1000 + \
 float(duracao.microseconds) / 1000))
        
#fim do programa