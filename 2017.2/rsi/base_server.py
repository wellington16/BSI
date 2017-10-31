# -*- coding: utf-8 -*-

"""
Lado do Servidor: Abre um TCP/IP numa port, espera por uma menssagem
de um cliente, e manda essa mensagem de volta como resposta. Esse
é uma simples ouve/responde conversação por cliente, mas percorre um loop
infinito para ouvir por mais clientes enquanto o script do servidor
estiver rodando. O cliente pode rodar em outra máquina ou no mesmo
computador se usar o 'localhost' como servidor
"""


import time, string, sys, os
from socket import *
from threading import *
from os import listdir
from os.path import isfile, join

# Cria o nome do host
meuHost = ''

# Utiliza este número de porto
minhaPort = 50007

# Cria um objeto socket. As duas constantes referem-se a:
# Familia do endereço (padrão é socket.AF_INET)
# Se é stream (socket.SOCK_STREAM, o padrão) ou datagram (socket.SOCK_DGRAM)
# E o protocolo (padrão é 0)
# Da maneira como configuramos:
# AF_INIT == Protocolo de endereço de IP
# SOCK_STREAM == Protocolo de transferência TCP
# Combinação = Server TCP/IP
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ServerFolder = os.getcwd() + "/imagens"

# Vincula o servidor ao número de porto
sockobj.bind((meuHost, minhaPort))

# O socket começa a esperar por clientes limitando a
# 1 conexões por vez
sockobj.listen(1)

listaNomes = ['jose', 'joao', 'maria', 'fabio', 'ricardo', 'diego', 'wellington', 'lucas']
listaArq = ['ic_arroz.jpg', 'ic_creme_de_pele.png', 'ic_leite.png', 'ic_pao.png', 'ic_pizza.png',
            'ic_refrigerante.png', 'ic_shampoo.png']

def encontrarArq(conexao, seq_num, reply, arq):

    arq = arq.strip("[")

    # print(arq)


    files = sorted([f for f in listdir(ServerFolder) if isfile(join(ServerFolder, f))])
    print(files)
    for arqList in files:
        print(arqList)
        print(arq)
        if arq == "'"+arqList+"'":
            print("passou")
            filesize = os.stat(ServerFolder + '/' + arqList)
            filesize  = filesize.st_size
            f = open(ServerFolder + '/' + arqList, "r")
            print(f)
            targetFileData = f.read(filesize)
            conexao.sendall(seq_num + reply + str(filesize)+" "+ targetFileData)
            f.close()
    else:
        conexao.send(seq_num + ' NOK')



def encontrar(nome):
    for nomex in listaNomes:
        if nomex == nome:
            print(nomex)
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
        # time.sleep(3)

        # Se não receber nada paramos o loop
        if not data:break

        # O servidor manda de volta uma resposta
        #conexão.send(b'Eco=>' + data)
        mensagemCliente = data.decode('ascii').split(" ")
        global cont

        if mensagemCliente[1] == 'CUMP':
            nome = mensagemCliente[2]
            reply = (encontrar(nome.lower()))
            seq_num = mensagemCliente[0].encode('ascii')
            # print(reply)
            conexao.send((seq_num + reply))
            continue


        elif mensagemCliente[1] == 'LIST':
            reply = ' ARQS '
            seq_num = mensagemCliente[0]
            print((listaArq))
            conexao.send((str(seq_num) + reply + str(listaArq).replace("[]","")).encode('ascii'))
            continue
        elif mensagemCliente[1] == 'PEGA':
            reply = ' ARQ '
            print(mensagemCliente[1])
            seq_num = mensagemCliente[0].encode('ascii')
            mensagemCliente[2] = str(mensagemCliente[2]).replace("]","")
            # print(mensagemCliente[2])
            if mensagemCliente[2] == "":
                print('passou 1')
                # print(str(mensagemCliente[3]))
                arquivo = encontrarArq(conexao, seq_num,reply,mensagemCliente[3])

                # print (tamanho)
            else:
                arquivo = encontrarArq(conexao, seq_num, reply, mensagemCliente[2])
                print('passou 2')
            continue
        else:
            reply = ' NOK'
            seq_num = mensagemCliente[0]
            conexao.send((seq_num + reply).encode('ascii'))
            continue

    # Fecha a conexão criada depois de responder o
    # cliente
    conexao.close()

