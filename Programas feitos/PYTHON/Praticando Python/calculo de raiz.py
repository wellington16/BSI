#coding:utf8
#
# Progrma 10 raízes de uma equação do segundo grau

# uma equação do segundo grau é algo do tipo ax**2 + bx + c

import math # precisaremos dessa biblioteca

# Entrada de dados
a = int(input("Digite um valor para o coeficiente a "))
b = int(input("Digite um valor para o coeficiente b "))
c = int(input("Digite um valor para o coeficiente c "))
#Calcular o delta

delta = b * b  - 4 * a * c

#testes

if delta < 0:
    print("A equação não possui raízes reais")
elif delta == 0:
    raiz =(-1 * b + math.sqrt(delta))/(2 * a)
    print( "A equação possui uma só raiz que é", raiz)
else:
    raiz1 =(-1 * b + math.sqrt(delta))/(2 * a)
    raiz2 =(-1 * b - math.sqrt(delta))/(2 * a)
    print( "A equação possui duas raiz que são", raiz1," e ",raiz2)

#fim de software
