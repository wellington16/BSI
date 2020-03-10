#coding:utf8
#
# Programa para encontrar o maior e menor valor de uma lista
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

vetor = []
n = int(input("Digite a quantidade de elementos a ser adicionada "))
i= 0
while i < n:
    temp = (input("Digite o elemento a ser adicionado ->  "))
    vetor.append(int(temp))
    i += 1
menor = vetor[0]
maior = vetor[0]
i = 0
while  i < len(vetor):
    if vetor [i] < menor:
        menor = vetor[i]
    if vetor[i] > maior:
        maior = vetor[i]
    i += 1
print("Vetor dado : ", vetor)
print("Vetor dado : ", menor)
print("Vetor dado : ", maior)

'''while i < n:
    temp = input("Digite o elemento a ser adicionada -> ")
    vetor.append(int(temp))
    i = i + 1
    vetor.sort()
print( vetor)
print("Vetor = ", vetor[0], " e ", vetor[-1])
'''

#fim do programa
