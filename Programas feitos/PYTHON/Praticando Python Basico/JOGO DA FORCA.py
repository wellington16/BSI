# Jogo da Forca

# Modulos a importar
import sys # Para quebrar o jogo a meio se quiser
import string # para manipular as palavras retiradas da lista
import random # para escolher a palavra

# Ir buscar ao ficheiro das palavras uma palavra para o utilizador adivinhar

# Define-se o caminho do ficheiro txt onde esta uma palavra por linha!
caminho ='C:\Users\WELLINGTON\Desktop'

# Abre-se o ficheiro
abrir_ficheiro = open(caminho)

# Le-se o ficheiro TODO para uma lista
base_de_dados = abrir_ficheiro.readlines()

# Criar uma funcao com o jogo para ser mais facil gerir

def novo_jogo():
    print ('Bem-vindo ao Jogo da Forca\n\n')
    print ('Para iniciar um jogo, prima 1. Para sair, prima 0\n')
    escolha = int(raw_input('--> '))
    if not escolha:
        print ('\nAdeus!\n')
        sys.exit() # No IDLE da erro mas sai .. nao percebo porque
    # Escolha de palavra do meio das retiradas da lista
    palavra_inteira = random.choice(base_de_dados)
    # Explode-se a string da palavra para uma lista
    palavra_lista = []
    for char in range(len(palavra_inteira)):
        if palavra_inteira[char]!='\n':
            palavra_lista.append(palavra_inteira[char]) # Para retirar a quebra de linha que resulta da leitura do ficheiro
    # Definir palavra a mostrar ao utilizador
    palavra_utilizador = []
    for char in range(len(palavra_inteira)):
        if palavra_inteira[char]!='\n': # Para retirar a quebra de linha que resulta da leitura do ficheiro
            palavra_utilizador.append('_ ')
    #Mostrar ao utilizador o numero de letras da palavra
    print ('\nA palavra tem',len(palavra_lista),'letras')
    tentativas = 6
    acertou_antes = 0
    acertou_agora = 0
    # Tentativas
    while 1:
        if tentativas == 0:
            break
        elif palavra_lista == palavra_utilizador:
            break
        acertou_antes = acertou_agora
        print ('\nFaltam',len(palavra_lista)-int(acertou_agora),'letras!')
        print ('Faltam',tentativas,'tentativa(s)')
        # Mostrar ao utilizador a palavra com os espacos
        mostrar_palavra = ''
        for char in range(len(palavra_utilizador)):
            mostrar_palavra = mostrar_palavra+palavra_utilizador[char]
        print (mostrar_palavra)
        # Pedir ao utilizador uma letra minuscula (KISS)
        letra_utilizador = raw_input('Digite uma letra em minusculas: ')
        # Comparar a letra com as na palavra_lista
        for char in range(len(palavra_lista)):
            if palavra_lista[char] == letra_utilizador:
                palavra_utilizador[char] = str(letra_utilizador)
                acertou_agora += 1
        if acertou_antes == acertou_agora:
            tentativas-= 1
    if tentativas!=0:
        print ('Parabens! Voce Acertou na palavra!')
    else:
        print ('Perdeu! Pode ser que acerte para a proxima!')

# Comecar um jogo novo
choice = 's'
while choice == 's':
    novo_jogo()
    choice = str(raw_input('Deseja jogar outra vez? [s]im/[n]ao: '))
