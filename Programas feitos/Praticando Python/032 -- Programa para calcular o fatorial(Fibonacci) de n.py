#coding:utf8
#
#032 -- Programa para calcular o fatorial(Fibonacci) de n.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

def fat(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fat(n - 1) + fat(n - 2)


x = int(input("Digite o tamanho da série -> "))

# chamando a função
print("O fatorial de ", x, " é ", fat(x))

#fim do programa
