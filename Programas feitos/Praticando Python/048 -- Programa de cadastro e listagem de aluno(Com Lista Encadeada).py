# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:58:33 2016

@author: WELLINGTON
"""
#048 -- Programa de cadastro e listagem de aluno(Com Lista Encadeada)


import os
# Biblioteca de funções do sistema operacional
# Limpar o video
#os.system("clear") # No linux ou mac os
#os. system("cls") # No windows

class Aluno:
    proximo = ''
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email
    def __str__(self):
        return"\nAluno : "+ self.nome +"\nEnd. : "+self.endereco + "\nEmail : " +self.email
    #fim da classe

primeiro = Aluno(nome ='', endereco ='', email ='')
atual = primeiro
ultimo = primeiro

#Menu do programa
while True:
    os.system("cls")
    print("Escolha uma das opções abaixo:")
    print("<1> Cadastrar um Aluno")
    print("<2> Listar os alunos")
    print("<3> Pesquisar no programa :)")
    print("<4> Sair do programa :(")
    escolha = raw_input("Digite sua escolha e pressione <ENTER>")
    #Inserindo aluno na lista
    if escolha != "1" and escolha != "2" and escolha != "3":
        print('Essa opção não existe!')
        continue
    elif escolha == "1":
        os.system("cls")
        nome = raw_input("Digite o nome do aluno: ")
        endereco = raw_input("Digite o endereço do aluno: ")
        email =raw_input("Digite o e-mail do aluno: ")
        objeto = Aluno(nome,endereco,email)
        if primeiro.nome == '':
            primeiro = objeto
            ultimo =primeiro
        else:
            ultimo.proximo =objeto
            ultimo = ultimo.proximo
            
    elif escolha == "2":
        atual = primeiro
        while True:
            print(atual)
            if atual.proximo =='':
                break
            else:
                atual = atual.proximo
        raw_input("Digite <ENTER> para continuar")
    elif escolha == "3":
        print("Programa Emcerrado" )
        break
    
print("Programa Emcerrado" )
        