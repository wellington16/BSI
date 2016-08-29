#coding:utf-8
import sys

#Autor Wellington Luiz

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 11 - Laboratório de Programação
    título: Juvenal se perdeu.
    Executado em python 3.5
'''

class No:
    #def __init__(self,chave,dado):
    def __init__(self,chave):
        #self._dado = dado
        self._filhoesq = None
        self._filhodir = None
        self._pai = None
        self._chave = chave
    def getChave(self):
        return self._chave
    def setChave(self,k):
        self._chave = k
    #def getDado(self):
        #return self._dado
    #def setDado(self,dado):
        #self._dado = dado
    def getFilhoEsq(self):
        return self._filhoesq
    def setFilhoEsq(self,filho):
        self._filhoesq=filho
    def getFilhoDir(self):
        return self._filhodir
    def setFilhoDir(self,filho):
        self._filhodir=filho
    def getPai(self):
        return self._pai
    def setPai(self,pai):
        self._pai=pai
    def __str__(self):
        return str("Nó: "+str(self.getChave())) #+" "+ self.getDado())    
        
class ArvoreBB:
    def __init__(self):
        self._raiz = None
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, no):
        self._raiz=no
    def percorrerEmOrdem(self,x, lista):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq(), lista) #PERCORRER SUB ARVORE ESQUERDA
            print("O nó é esse: "+str(x)) #VISITA
            lista.append(str(x.getChave()))
            self.percorrerEmOrdem(x.getFilhoDir(), lista) #PERCORRER SUB ARVORE DIREITA
        return lista
            
    def percorrerEmPreOrdem(self, x, lista):
        if x != None:
            print("O nó é esse: "+str(x)) #visitando
            lista.append(str(x.getChave()))
            self.percorrerEmOrdem(x.getFilhoEsq(), lista)#PercorrendoArvorePelaEsquerda
            self.percorrerEmOrdem(x.getFilhoDir(), lista)#PercorrendoArvorePelaDireita
        return lista

    def percorrerEmPosOrdem(self,x, lista):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq(), lista)#PercorrendoArvorePelaEsquerda
            self.percorrerEmOrdem(x.getFilhoDir(), lista)#PercorrendoArvorePelaDireita
            lista.append(str(x.getChave()))
            print("O no é esse: "+str(x)) #visitando
        return lista
        
    def buscar(self,x,k):
        if x == None or x.getChave() == k:
            return x
        if k < x.getChave():
            return self.buscar(x.getFilhoEsq(),k)
        else:
            return self.buscar(x.getFilhoDir(),k)
    
    def minimo(self,x):
        while x.getFilhoEsq() != None:
            x = x.getFilhoEsq()
        return x
    
    def maximo(self,x):
        while x.getFilhoDir() != None:
            x = x.getFilhoDir()
        return x
    def sucessor(self,x):
        if x.getFilhoDir() != None:
            return self.minimo(x.getFilhoDir())
        y = x.getPai()
        while y != None and x is y.getFilhoDir():
            x = y
            y = y.getPai()
        return y
    def antecessor(self,x):
        try:
            if x.getFilhoEsq() != None:
                return self.maximo(x.getFilhoEsq())
            y = x.getPai()
            while y != None and x == y.getFilhoEsq():
                x = y
                y = y.getPai()
            return y
        except:
            return 0
            
        
    def inserir(self,z):
        y=None
        x = self.getRaiz()
        while x != None:
            y=x
            if z.getChave() <= x.getChave():
                x = x.getFilhoEsq()
            else:
                x = x.getFilhoDir()
        z.setPai(y)
        if y == None:
            self.setRaiz(z)
        else:
            if z.getChave() < y.getChave():
                y.setFilhoEsq(z)
            else:
                y.setFilhoDir(z)
                      
    def remover(self,z):
        if z.getFilhoEsq() == None or z.getFilhoDir() == None:
            y = z
        else:
            y = self.sucessor(z)
        if y.getFilhoEsq() != None:
            x = y.getFilhoEsq()
        else:
            x = y.getFilhoDir()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getFilhoEsq():
                y.getPai().setFilhoEsq(x)
            else:
                y.getPai().setFilhoDir(x)
        if y != z:
            z.setChave(y.getChave())
            z.setDado(y.getDado())
            
import sys
tree = ArvoreBB()
#ent=open("e11.txt")
#out=open('e11s.txt',"w")

ent=open(sys.argv[1])
out=open(sys.argv[2],"w")

linha=None
caso=1
text=""
while True:
    linha = ent.readline()
    if linha == '':
        break
    tree.setRaiz(None)
    n=int(linha)
    text="Caso "+ str(caso) +":\n"
    for i in range(n):
        linha=ent.readline()
        if linha.startswith("A"):
            l=linha.split(" ")
            x=int(l[1])
            tree.inserir(No(x))
        elif linha.startswith("B"):
            l=linha.split(" ")
            x=int(l[1])
            tree.remover(tree.buscar(tree.getRaiz(), x))
        elif linha.startswith("C"):
            linha.split(" ")
            x=int(l[1])
            node=tree.buscar(tree.getRaiz(), x)
            try:
                e = tree.antecessor(node)
                while e.getChave()== x:
                    e = tree.antecessor(e)
                text+=str(e.getChave())+"\n"
            except:
                text+=str(tree.antecessor(node))+"\n"
        elif "PRE" in linha:
            lista=[]
            lista=tree.percorrerEmPreOrdem(tree.getRaiz(),lista)
            if len(lista)>0:
                for i in lista:
                    text+=i+" "
                text=text[:-1]+"\n"
            else:
                text+="0\n"
        elif "IN" in linha:
            lista=[]
            lista=tree.percorrerEmOrdem(tree.getRaiz(),lista)
            if len(lista)>0:
                for i in lista:
                    text+=i+" "
                text=text[:-1]+"\n"
            else:
                text+="0\n"
        elif "POST" in linha:
            lista=[]
            lista=tree.percorrerEmPosOrdem(tree.getRaiz(),lista)
            if len(lista)>0:
                for i in lista:
                    text+=i+" "
                text=text[:-1]+"\n"
            else:
                text+="0\n"
    caso += 1
    out.write(text)
    text=""
out.close()
