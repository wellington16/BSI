# -*- coding:utf-8 -*-
# Weliington Luiz Antonio

'''
Exercício 4 - Laboratório de Programação
 Esse programa verifica se, dado um quadrado, ele consegui determinar se ele é
 magico ou não e qual a soma dele (caso seja mágico).
'''
import sys

#Abrindo e fazendo a leitura do arquivo com Hardcode 
entrada=open('E4.in', 'r')
saida=open('E4.out', 'w')

#Tratamento
string=entrada.read()
string2=string.split('\n')

N=int(string2[0])
somas=[]
if (N >=2) and (N<=10):
    for i in range (N):
        linhas=0
        for j in range (N):
            linha=string2[i+1].split(' ')
            linhas+=int(linha[j])
        somas.append(linhas)
for x in range (N+(N-1)):
    colunas=0
    for y in range(N):
        if (string2[y+1][x])!=' ':
            colunas+=int(string2[y+1][x])
    if colunas!=0:
        somas.append(colunas)
contador=0
while contador < N:
    diagonal_s = 0
    for p in range(N + 1, -1, -2):
        contador += 1
        if contador <= N:
            diagonal_s += int(string2[contador][p])        
    somas.append(diagonal_s)
contador = 0
while contador < N:
    diagonal_p=0
    for p in range(0,N+2,2):
        contador+=1
        if contador<=N:
            diagonal_p+=int(string2[contador][p])
    somas.append(diagonal_p)


#verificação eescrita de resultado
quadrado_magico=True
for v in range(len(somas)-1):
    if somas[v]==somas[0]:
        pass
    else:
        quadrado_magico=False

if quadrado_magico:
    saida.write(str(somas[0]))
else:
    saida.write('-1')

#fechando arquivos
entrada.close()
saida.close()

#fim do programa
