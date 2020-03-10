#coding:utf8
#
# Programa para adicionar elementos em uma lista (Imprimir na ordem inversa)
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

vetor = []
n = int(input("Digite a quantidade de elementos a ser adicionada"))
i= 0
while i < n:
    temp = input("Digite o elemento a ser adicionada -> ")
    vetor.append(int(temp))
    i = i + 1
print("Vetor recebido = ", vetor)
i = len(vetor)- 1
r = []
while i >= 0:
    r.append(vetor[i])
    i-= 1
print("Na ordem inversa : ", r)


#fim do programa
