#coding:utf8
#
# Programa para pesquisar um elementos pares (linearmente)
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
i = 0
print("Vetor Recebido : ",vetor)
a=[]
while  i < len(vetor):
    if vetor[i] % 2 == 0:
        print("elemento pares : ", vetor[i])
        a=[]
        a.append(vetor[i])
        print("Lista" ,a )
    if vetor[i] % 2 == 1:
        print("elemento ímpares : ", vetor[i])
    i += 1
print("Lista" ,a[:] )        
#fim do programa
