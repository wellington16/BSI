# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:34:34 2016

@author: WELLINGTON
"""

#045 -- Programa de Algoritmo Quicksort.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
from datetime import datetime
import random
random.seed()

def quicksort(lista):
    L = []
    R = []
    #caso base
    if  len(lista) <= 1:
        return lista 
    #calcula a chave(que é o meio)
    chave = lista[ len(lista) / 2]
    for i in lista:
        if i < chave:
                L.append(i)
        if i > chave:
                R.append(i)
        #finalizar
    return quicksort(L) + [chave] + quicksort(R) 

l = input("Digite o tamanho da lista :  " )
A= []
#Gerando a lista a ser utilizada 
i = 0
img = datetime.now()
while i < l:
    x = random.randint(1, l)
    if x not in A:
        A.append(l - i)# com geração de valores muito altos
        i += 1
tempini = datetime.now()
ger = tempini - img
inicio = datetime.now()
B = quicksort(A)
fim = datetime.now()
duracao = fim - inicio
print("-------------------")
print("Lista Original ")
print(A)
print('----------------------')
print("Lista ordenada : ")
print(B)
print('----------------------')
print("tempo(ms): %2.5f" % float(ger.seconds * 1000 + \
 float(ger.microseconds) / 1000))
print("tempo(ms): %2.5f" % float(duracao.seconds * 1000 + \
 float(duracao.microseconds) / 1000))
        
#fim do programa