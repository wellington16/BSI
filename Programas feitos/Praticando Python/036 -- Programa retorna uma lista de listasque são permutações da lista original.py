#coding:utf8
#
#036 -- Programa retorna uma lista de listasque são permutações da lista original..
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

def permutacoes(lista):
    if len(lista) == 1:
        return[lista]
    primeiro = lista[0]
    resto = lista[1:]
    resultado = []
    for perm in permutacoes(resto):
        for i in range(len(perm) + 1):
            resultado = resultado + [perm[ : i] + [primeiro] + perm[i : ]]
    return resultado


x = input ("Digite a lista ->  ")
print (permutacoes(x))
#fim do programa
