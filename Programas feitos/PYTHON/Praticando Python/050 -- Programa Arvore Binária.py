# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:01:27 2016

@author: WELLINGTON
"""
import os
import random 

#050 -- Programa Arvore Binária

class Noh: #classe Nó 
    dado, esquerdo, direito = 0, None, None
    def __init__(self, dado):
        self.esquerdo = None
        self.direito = None
        self.dado = dado
        
    def __str__(self):
        return"{", str(self.dado),"}"
    #fim da Classe

    
class ArvoreBinaria: #criando a classe arvore
    def  __init__(self):
        self.raiz = None
        
    def criarNoh(self,dado):
        return Noh(dado)
        
    def insere(self, raiz, dado):
        if raiz == None:
             return self.criarNoh(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
        return raiz
    
    
    def pesquisar(self, raiz, valor):# função pesquisa valor na árvore
        if raiz == None:
            return 0
        else:
            if valor == raiz.dado:
                return 1
            else:
                if valor < raiz.dado:
                    return self.pesquisar(raiz.esquerdo, valor)
                else:
                    return self.pesquisar(raiz.direito, valor)
    def imprimirArvore(self, raiz):
        if raiz == None:
            pass
        else:
            self.imprimirArvore(raiz.esquerdo),
            print('[', raiz.dado,']'),
            self.imprimirArvore(raiz.direito)
            
    def imprimirArvoreInvertida(self, raiz):
        if raiz == None:
            pass
        else:
            self.imprimirArvore(raiz.direito)
            print('[', raiz.dado,']'),
            self.imprimirArvore(raiz.esquerdo)
            

    def imprimirNohs(self,raiz):

        if raiz == None:return 
        a = raiz.dado
        if raiz.esquerdo != None:
            b = raiz.esquerdo.dado
        else:
            b = None
        if raiz.direito != None:
            c = raiz.direito.dado
        else:
            c = None
        print('{', a,'[',b,',',c,']','}'),
        self.imprimirNohs(raiz.esquerdo)
        self.imprimirNohs(raiz.direito)
        
    #Função que retorna o menor da árvore     
    def menorValor(self, raiz):
        while(raiz.esquedo != None):
            raiz = raiz.esquerdo
        return raiz.dado
    
    #Função que retorna o maior da árvore    
    def maiorValor(self, raiz):
        while(raiz.direito != None):
            raiz = raiz.direito
        return raiz.dado

    #Profundidade da árvore
    def profundidadeMaxima(self, raiz):
        if raiz == None:
            return 0
        else:
            profe = self.profundidadeMaxima(raiz.esquerdo)
            profd = self.profundidadeMaxima(raiz.direito)
            return max(profe,profd) + 1

    #função tamanho
    def tamanho(self, raiz):
        if raiz == None:
            return 0
        else:
            return self.tamanho(raiz.esquerdo) + 1 + self.tamanho(raiz.direito)
        
    #Função sucessor
    def sucessor(self, noh):
        paiSucessor = noh
        sucessor = noh
        atual = noh.direito
        while atual != None:
            paiSucessor = atual
            atual = atual.esquerdo
        if sucessor != noh.direito: #refazendo as conexões
            paiSucessor.esquerdo = sucessor.direito
            sucessor.direito = noh.direito
        return sucessor    
    
    #Função apagar Valor da árvore
    def apagar(self, raiz, valor):
        atual = raiz
        noPai = raiz
        ehFilhoEsquerdo = True
        while atual.dado != valor:
            noPai = atual 
            if valor < atual.dado:
                ehFilhoEsquerdo = True
                atual = atual.esquerdo
            else:
                ehFilhoEsquerdo = False
                atual = atual.direito
            if atual == None:
                return False
    
            if atual.esquerdo == None and atual.direito == None:
                if atual == raiz:
                    raiz = None
                elif ehFilhoEsquerdo:
                    noPai.esquerdo = None
                else:
                    noPai.direito = None
            elif atual.direito == None:
                if atual == raiz:
                    raiz = atual.esquerdo
                elif ehFilhoEsquerdo:
                    noPai.esquerdo = atual.esquerdo
                else:
                    noPai.direito = atual.direito
            elif atual.esquerdo ==None:
                if atual ==raiz:
                    raiz = atual.direito
                elif ehFilhoEsquerdo:
                    noPai.esquerdo = atual.direito
                else:
                    noPai.direito = atual.esquerdo
            else:
                suc = self.sucessor(atual)
                if atual == raiz:
                    raiz = suc
                elif ehFilhoEsquerdo:
                    noPai.esquerdo = suc
                else:
                    noPai.direito = suc
                suc.esquerdo = atual.esquerdo
            return True
    
             
#valorRaiz = int(raw_input('Digite o valor da raiz:'))

#ArvoreBin = ArvoreBinaria()
        
#raiz = ArvoreBin.criarNoh(valorRaiz)         
while True:
    #os.system("cls")
    print('Menu da Arvore \n')
    print('<1> Adicionar dados(aleatorios)')
    print('<2> Imprimir')
    print('<3> Pesquisar na arvore')
    print('<4> Estatística da arvore')
    print('<5> Remover da arvore')
    print('<6> Sair')
    resposta = input('Digite a escolha e pressione <ENTER>   ')
    if resposta == "6":
        break
    elif resposta == "1":
        l = []
        quantidade = int(input('Quantos nós a inserir? '))
        i = 0
        while i < quantidade:
            j = random.randint(0, quantidade)
            if j not in l:
                l.append(j)
                i += 1
        print('Lista de entrada', l)
        ArvoreBin = ArvoreBinaria()
        raiz = ArvoreBin.criarNoh(l[0])
        for i in range(1, len(l)):ArvoreBin.insere(raiz, l[i])
        input('Arvore criada. Tecle <ENTER> para continuar    ')
    elif resposta == '2':
        print('\nImpressao na forma de lista:', ArvoreBin.imprimirArvore(raiz))
        print('\nImpressao na forma de lista Invertida:', ArvoreBin.imprimirArvoreInvertida(raiz))
        print('\nImpressao por nós:', ArvoreBin.imprimirNohs(raiz))
    elif resposta == '3':
        dado = int(input('\nDigite o valor a ser pesquisado: '))
        if ArvoreBin.pesquisar(raiz, dado):
            print( 'Encontrado')
        else:
             print('Não encontrado')
        raw_input('Tecle <ENTER> para continuar')
    elif resposta == '5':
        noApagar = int(input('Digite o valor a ser removido da arvore '))
        ArvoreBin.apagar(raiz, noApagar)
        input('Valor removido ou inexistente. Pressione <ENTER> para continuar  ')
        
# Fim do programa
        
        
