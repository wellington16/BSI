#coding:utf8
#
#031 -- Programa para calcular o fatorial(Recursiva) de n.
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
        return n * fat(n - 1)


x = int(input("Digite o valor para calcular o fatorial -> "))

# chamando a função
print("O fatorial de ", x, " é ", fat(x))

#fim do programa
