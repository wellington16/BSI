# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:04:53 2016

@author: WELLINGTON
"""

#040 -- Programa de Algoritmo por Inserção.
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
inicio = datetime.now()
for i in range(1, len(A)):
    chave = A[i]
    j = i -1
    while A[j] > chave and j >= 0:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = chave
fim = datetime.now()
duracao = fim - inicio
print('----------------------')
print("Lista ordenada : ")
print(A)
print('----------------------')
print("tempo(ms): %2.8f" % float(duracao.seconds * 1000 + \
 float(duracao.microseconds) / 1000))
        
#fim do programa