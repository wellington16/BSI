#coding:utf8
#
#034 -- Programa retorna a True se a lista a é permutação de b.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
def permutacao(a, b):
    if len(a) == 0: return len(b) == 0
    if a[0] in b:
        i = b.index(a[0])
        return permutacao(a[1:], b[0: i] + b[i + 1 : ])
    return False
'''l = input("Digite a lista A ")
v= input("Digite a lista B ")'''
l = [12,33,44,55,67,89,123,456]
v = [33,12,55,67,44,123,456,89]
print(permutacao(l, v))
#fim do programa
