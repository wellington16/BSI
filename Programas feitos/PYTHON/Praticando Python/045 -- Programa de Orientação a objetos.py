# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:10:16 2016

@author: WELLINGTON
"""

#045 -- Programa de Orientação a objetos.

#import os 
#os.system("clear")
class Racional:
    def __init__(self, divisor, dividendo):
        self.divisor = divisor
        self.dividendo = dividendo
        
    def __str__(self):
        return str(self.divisor) + '/' + str(self.dividendo)
        
    def __mul__(self,outro):
        divisor = self.divisor * outro.divisor
        dividendo = self.dividendo * outro.dividendo
        return Racional(divisor, dividendo)
# fim da classe

a = Racional(5, 2)
b = Racional(3, 4)
c = a * b
print("Seja o racional a = ", str(a))
print("Seja o racional b = ", str(b))
print("Seja o racional c (a * b) = ", str(c))