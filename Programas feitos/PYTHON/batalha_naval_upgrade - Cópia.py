
#BATALHA NAVAL

import random

def configuração(x="sim",y="nao"):
    deseja=input("Deseja configuraro jogo? ")
    if deseja == "nao":
        arquivos= open("config.txt",)
        arquivos.read(11)
        dimensao = arquivos
        #quantidade_D_Navios = arquivos.read(20)
        #erros = aruivos.read(20)
        close()

campo_de_batalha=[]
espelho=[]

#dimensao=int(input('Dimens�o: '))
#tiros=int(input('Tiros: '))

for i in range (dimensao):
        campo_de_batalha.append([])
        espelho.append([])
        for j in range(dimensao):
            campo_de_batalha[i].append(random.randint(0,1))
            espelho[i].append('*')

while tiros > 0:
    tiros-=1
    #cord_x=int(input('Y: '))
    cord_x-=1
    #cord_y=int(input('X: '))
    cord_y-=1
    if campo_de_batalha[cord_y][cord_x] == 1:
        print('KABUM!:-D, Voc� ACERTOU!' )
        espelho[cord_y][cord_x]='@'
        #print(espelho)
        for x in range(dimensao):
            print('%s , %s , %s'% (espelho[x][0], espelho[x][1],espelho[x][2]))
    else:
        print('splash :/ ,Voc� ERROU !')
        for x in range(dimensao):
            print('%s , %s , %s'% (espelho[x][0], espelho[x][1],espelho[x][2]))

#for x in range(dimensao):
#    print('#'*dimensao)

#for x in range(dimensao):
    #print('%d , %d , %d'% (espelho[x][0], espelho[x][1],espelho[x][2])
    

#for y in range(dimensao):
       # print(espelho[x], espelho[x+1], espelho[x+2])
