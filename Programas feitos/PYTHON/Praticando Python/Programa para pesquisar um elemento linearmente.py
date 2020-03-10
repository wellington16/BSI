#coding:utf8
#
# Programa para pesquisar um elemento linearmente
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

elementoProcurado = int(input("Digite o elemento a localizar ->  "))
i = 0
posicao = -1
while i < len(vetor):
    if elementoProcurado == vetor[i]:
         posicao = i
    i += 1 
print("Vetor Recebido : ",vetor)
print("elemento procurado : ",elementoProcurado)
if posicao == -1:
    print("Elemento não encontrado")
else:
    print("a posicao do elemento é ", posicao)
print("Vetor Recebido : ",vetor)    
#fim do programa
