#coding:utf8
#
#030 -- Programa para calcular o fatorial de n.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

def fat(n):
    if n < 0:
        return(":(. Não existe fatorial de número negativo. ")
    elif n == 0:
        return 1
    else:
        fat = n
        for i in range(1, n):
            fat = fat * i
        return fat


x = int(input("Digite o valor para calcular o fatorial -> "))

# chamando a função
print("O fatorial de ", x, " é ", fat(x))

#fim do programa
