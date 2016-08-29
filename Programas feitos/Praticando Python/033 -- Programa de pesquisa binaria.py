#coding:utf8
#
#033 -- Programa de pesquisa binaria.
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
def localiza(lista, valor):
    def pesquisaBinaria(min, max):
        if min == max:
            return min
        else:
            meio =  (max + min) /2
            if int(valor) > lista[int(meio)]:
                return pesquisaBinaria(meio + 1, max)
            else:
                return pesquisaBinaria(min, meio)
    i = pesquisaBinaria(0, len(lista) - 1)
    if lista[int(i)] == int(valor):
        print(valor," encontrado na posição", int(i))
    else:
        print (valor," não encontrado")
        
l = (input("Digite a lista a ser pesquisada\
          \nLembre que deve estar em ordem crescente -> "))
#l = [12,33,44,55,67,89,123,456] 
v = (input('Qual o valor a pesquisar'))
localiza(l, v)
#fim do programa
