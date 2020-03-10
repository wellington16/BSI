# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:35:04 2016

@author: WELLINGTON
"""

#038 -- Programa torre de Hanoi.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
movimentos = 0
def mover(origem, destino):
    global movimentos 
    movimentos += 1
    obj = origem.pop(-1)
    destino.append(obj)
    print("-------------")
    print("1 : ", h1)
    print("2 : ", h2)
    print("3 : ", h3)

def hanoi(n, origem, destino, temp):
    if n == 1:
        mover(origem, destino)
    else:
        hanoi(n - 1, origem, temp, destino)
        mover(origem, destino)
        hanoi(n - 1, temp, destino, origem)
        
#início
x = int(input("Digite o numero  de aneis: "))
h1 = []
h2 = []
h3 = []
for i in range(0, x): h1.append(x - i)
print("1 : ", h1)
print("2 : ", h2)
print("3 : ", h3)
hanoi(x, h1, h3, h2)
print("Quantidade de movimentos foi ", movimentos)
#fim do programa