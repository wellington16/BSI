
#060 -- Programa Calcula a raíz

#
import sys
import os
import math

os.system("clear")

class DeltaNegativo(Exception):
    def imprimir():
        return ("valor de delta menor que zero, portanto equação não tem raízes")
while True:
    try:
        a = int(input("Digite o valor do coeficiente A: "))
    except ValueError:
        print("Erro de entrada de dados, digite um número inteiro.")
    else:
        break
while True:
    try:
        b = int(input("Digite o valor do coeficiente B: "))
    except ValueError:
        print("Erro de entrada de dados, digite um número inteiro.")
    else:
        break
while True:
    try:
        c = int(input("Digite o valor do coeficiente C: "))
    except ValueError:
        print("Erro de entrada de dados, digite um número inteiro.")
    else:
        break
try:
    delta = b * b - 4 * a * c
    if delta < 0: raise DeltaNegativo
    raiz1 = (-1 * b + math.sqrt(delta))/(2*a)
    raiz2 = (-1 * b - math.sqrt(delta))/(2*a)
except :
    print(DeltaNegativo.imprimir())
    #print("A equação não possui raízes reais...")
else:
    print("\nA(s) raíz (ízes) da equação é(são) ", raiz1," e ", raiz2)
finally:
    print("Fim de programa")
    
