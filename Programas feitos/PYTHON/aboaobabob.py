#JOGO BATALHA NAVAL

import random

tentativas=0
erros=0
acertos=0
m=[ ]
s=[]
y=8
z=2
#.
n=int(input("Digite o primeiro numero para dimensão : "))
#.
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(random.randint(1,9))
for f in range (n):
    print ('* ' *len(m[f]))
    

