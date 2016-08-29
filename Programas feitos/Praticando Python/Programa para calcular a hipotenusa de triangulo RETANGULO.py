#coding:utf8
#Programa para calcular a hipotenusa de triangulo RETANGULO
import math
a = int( input("Digite o lado a "))
b = int( input("Digite o lado b "))
h = math.sqrt(a * a + b * b) 

print( "Hipotenusa = ",int( h))
