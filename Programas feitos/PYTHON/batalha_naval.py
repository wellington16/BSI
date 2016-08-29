
#BATALHA NAVAL

import random

campo_de_batalha=[]
espelho=[]

dimensao=int(input('Dimensão: '))
tiros= int(input('tiros:'))


for i in range(dimensao):
    campo_de_batalha.append([])
    espelho.append([])
    for j in range(dimensao):
        campo_de_batalha[i].append(random.randint(0,1))
        espelho[i].append('*')


#for x in range(dimensao):
#    print('* ' *dimensao)

print campo_de_batalha
print espelho

while tiros > 0:
    tiros-=1
    cord_x=int(input('X: '))
    cord_y=int(input('Y: '))
    if campo_de_batalha[cord_y][cord_x] == 1:
        print('KABUM!:-D, Você ACERTOU!' )        
    else:
        print('splash :/ ,Você ERROU !')

for x in range(dimensao):
    print('#'*dimensao)

