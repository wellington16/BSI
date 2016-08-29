# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:32:55 2016

@author: WELLINGTON
"""

#044 -- Programa de Herança.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
import math
class triangulo:
    area = 0
    tipo = " "
    def __init__(self):
        print("Criada a classe Base")

class trianguloRetangulo(triangulo):
    l1 = []
    l2 = []
    def __init__(self):
       
            print("Criada a classe derivada")
            self.l1 = input("Qual o valor do lado 1: ")
            self.l2 = input("Qual o valor do lado 2: ")
            self.area = self.l1 * self.l2 / 2.0
            print("Area = ", self.area)
    def sei(self):
        return math.sqrt(self.l1 ** 2 + self.l2 ** 2)
#fim das classes
#inicio do programa principal
t = triangulo()
tr = trianguloRetangulo()
t = tr
#chamada polimorfica
print("hipotenusa (Usando t) ",t.sei())
print("hipotenusa (Usando tr) ",tr.sei())
t.l1 = 1000
print("l1 em t eh ", t.l1)
print("l1 em tr eh", tr.l1)
