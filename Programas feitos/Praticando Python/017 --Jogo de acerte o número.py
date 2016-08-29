#coding:utf8
#
# Jogo de acerte o número
#
#import os # Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows
import random
random.seed()
valor = random.randint(1,9)
chute = 0
tentativas = 0

while chute != valor:
    chute = int(input("Digite o seu palpite "))
    tentativas += 1
    if chute == valor:
        print("Parabéns. Você acertou em ",tentativas," tentativas!!")
    elif chute < valor:
        print( "Você errou para menos na tentivas ",tentativas)
    else:
        print(" Você errou para mais na tentativas ",tentativas)
        
#fim do programa
