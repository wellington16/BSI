# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:58:33 2016

@author: WELLINGTON
"""
#047 -- Programa de cadastro e listagem de aluno


import os
# Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

class Aluno:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email
    def __str__(self):
        return"\nAluno : "+ self.nome +"\nEnd. : "+self.endereco + "\nEmail : " +self.email
    #fim da classe
        
#Menu do programa
lista =[]
while True:
    os.system("cls")
    print("Escolha uma opção abaixo:")
    print("<1> Cadastrar um Aluno")
    print("<2> Listar os alunos")
    print("<3> Sair do programa :(")
    escolha = raw_input("Digite sua escolha e pressione <ENTER>")
    if escolha != "1" and escolha != "2" and escolha != "3":
        continue
    elif escolha == "1":
        os.system("cls")
        nome = raw_input("Digite o nome do aluno: ")
        endereco = raw_input("Digite o endereço do aluno: ")
        email =raw_input("Digite o e-mail do aluno: ")
        objeto = Aluno(nome,endereco,email)
        lista.append(objeto)
    elif escolha == "2":
        for i in lista:
            print(i)
        raw_input("Digite <ENTER> para continuar")
    elif escolha == "3":
        print("Programa Emcerrado" )
        break
    
    print("Programa Emcerrado" )
        