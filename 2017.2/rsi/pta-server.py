# -*- coding: utf-8 -*-



import time, string, sys, os
from socket import *
from threading import *
from os import listdir
from os.path import isfile, join


#Autor Wellington Luiz

"""
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Redes e Sistemas de Internet - 2017.2
    Professor: Glauco Gonçalves
    Prática 1 - PTA
    título: Juvenal se perdeu.
    Executado em python 2.7
    
    obs: Fiz alguns ajustes no pta-client.py.
"""



# Cria o nome do host
meuHost = ''

# Utiliza este número de porto
minhaPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ServerFolder = os.getcwd() + "/imagens"

# Vincula o servidor ao número de porto
sockobj.bind((meuHost, minhaPort))

# O socket começa a esperar por clientes limitando a
# 1 conexões por vez
sockobj.listen(1)

listaNomes = ['glauco', 'filipe', 'jobson','vitor', 'johnatan', 'ariana',
              'diego', 'wellington', 'lucas', 'we']

listaArq = ['ic_arroz.jpg', 'ic_creme_de_pele.png', 'ic_leite.png', 'ic_pao.png', 'ic_pizza.png',
            'ic_refrigerante.png', 'ic_shampoo.png']

def encontrarArq(conexao, seq_num, reply, arq):

    files = sorted([f for f in listdir(ServerFolder) if isfile(join(ServerFolder, f))])
    for arqList in files:
        if arq == "'"+arqList+"'":
            # print("passou")
            filesize = os.stat(ServerFolder + '/' + arqList)
            filesize  = filesize.st_size
            f = open(ServerFolder + '/' + arqList, "r")
            # print(f)
            targetFileData = f.read(filesize)
            conexao.sendall(seq_num + reply + str(filesize)+" "+ targetFileData)
            f.close()
            break
    else:
        conexao.send(seq_num + ' NOK')

def encontrar(nome):
    for nomex in listaNomes:
        if nomex == nome:
            return b' OK'
    else:
        return b" NOK"


while True:
    # Aceita uma conexão quando encontrada e devolve a
    # um novo socket conexão e o endereço do cliente
    # conectado

    conexao, endereco = sockobj.accept()
    print('Server conectado por', endereco)

    while True:	
        # Recebe data enviada pelo cliente
        data = conexao.recv(2048)

        # Se não receber nada paramos o loop
        if not data:break

        mensagemCliente = data.decode('ascii').split(" ")
        global cont
        if mensagemCliente[0] != '0' or mensagemCliente[1] == 'CUMP':
            if mensagemCliente[1] == 'CUMP':
                nome = mensagemCliente[2]
                reply = (encontrar(nome))
                seq_num = mensagemCliente[0].encode('ascii')
                # print(mensagemCliente[0])
                conexao.send((seq_num + reply))


            elif mensagemCliente[1] == 'LIST':
                reply = ' ARQS '
                seq_num = mensagemCliente[0]
                # print (mensagemCliente[0])
                # print(str(listaArq).strip("[]"))
                conexao.send((str(seq_num) + reply + str(listaArq).strip("[]")).encode('ascii'))

            elif mensagemCliente[1] == 'PEGA':
                reply = ' ARQ '
                # print(mensagemCliente[0])
                seq_num = mensagemCliente[0].encode('ascii')
                # print(mensagemCliente[2])
                if mensagemCliente[2] == "":
                    mensagemCliente[3] = str(mensagemCliente[3]).strip("[]")
                    # print(str(mensagemCliente[3]))
                    arquivo = encontrarArq(conexao, seq_num,reply,mensagemCliente[3])
                    # print (tamanho)
                else:
                    mensagemCliente[2] = str(mensagemCliente[2]).strip("[]")
                    arquivo = encontrarArq(conexao, seq_num, reply, mensagemCliente[2])

            elif mensagemCliente[1] == 'TERM':
                # print(mensagemCliente[0])
                reply = ' OK'
                seq_num = mensagemCliente[0].encode('ascii')
                conexao.send((seq_num + reply))
                # conexao.close()
            else:
                reply = ' NOK'
                seq_num = mensagemCliente[0]
                conexao.send((seq_num + reply).encode('ascii'))
                # conexao.close()

        else:
            reply = ' NOK'
            seq_num = mensagemCliente[0]
            conexao.send((seq_num + reply).encode('ascii'))

    # Fecha a conexão criada depois de responder o
    # cliente
    conexao.close()

