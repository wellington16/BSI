#coding:utf8
#
# Programa para calcular a media aritmetica de uma lista
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
soma = 0

i = 0

while  i < len(vetor):
    soma += vetor[i]
    i += 1
media= float(soma)/len(vetor)

print("Vetor dado : ", vetor)
print("Vetor dado : ", media)
print("Vetor dado : ", soma)

#fim do programa
