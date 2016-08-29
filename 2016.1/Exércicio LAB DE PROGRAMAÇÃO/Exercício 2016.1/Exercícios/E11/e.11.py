class Node():
    def __init__(self, chave, valor=None):
        self._valor = valor
        self._left = None
        self._right = None
        self._pai = None
        self._chave = chave
        
    def getChave(self):
        return self._chave
    def setChave(self, x):
        self._chave = x
        
    def getValor(self):
        return self._valor
    def setValor(self, valor):
        self._valor = valor
        
    def getLeft(self):
        return self._left
    def setLeft(self, E):
        self._left = E
        
    def getRight(self):
        return self._right
    def setRight(self, D):
        self._right = D
        
    def getPai(self):
        return self._pai
    def setPai(self, P):
        self._pai = P
        
    def __str__(self):
        return str("No: " + str(self.getChave())+ "\t"+ "dado: "+ str(self.getValor()))
        
class ArvoreBinaria:
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, R):
        self._raiz = R
    def walk_in_order(self, node, array):
        if node != None:
            self.walk_in_order(node.getLeft(), array)
            array.append(str(node.getChave()))
            self.walk_in_order(node.getRight(), array)
        return array
    def walk_in_postOrder(self, node, array):
        if node != None:
            self.walk_in_postOrder(node.getLeft(), array)
            self.walk_in_postOrder(node.getRight(), array)
            array.append(str(node.getChave()))
        return array
    def walk_in_preOrder(self, node, array):
        if node != None:
            array.append(str(node.getChave()))
            self.walk_in_preOrder(node.getLeft(), array)
            self.walk_in_preOrder(node.getRight(), array)
        return array
    def search(self, node, key):
        if (node == None) or (node.getChave() == key):
            return node
        if key < node.getChave():
            return self.search(node.getLeft(), key)
        else:
            return self.search(node.getRight(), key)
    
    def minimo(self, x):
        while x.getLeft() != None:
            x = x.getLeft()
        return x
    def maximo(self, x):
        while x.getRight() != None:
            x = x.getRight()
        return x
    
    def sucessor(self, x):
        if x.getRight() != None:
            return self.minimo(x.getRight())
        y = x.getPai()
        while y != None and x is y.getRight():
            x = y 
            y = y.getPai()
        return y 
    
    def antecessor(self, x):
        try:
            if x.getLeft() != None:
                return self.maximo(x.getLeft())
            y = x.getPai()
            while y != None and x == y.getLeft():
                x = y 
                y = y.getPai()
            return y
        except:
            return 0
        
            
    def inserir(self, z):
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if z.getChave() <= x.getChave():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setPai(y) 
        
        if y == None:
            self.setRaiz(z)
        else:
            if z.getChave() <= y.getChave():
                y.setLeft(z)
            else:
                y.setRight(z)
                
                
    def remover(self, z):
        if z.getLeft()==None or z.getRight()==None:
            y = z 
        else: 
            y = self.sucessor(z)
        
        if y.getLeft() != None:
            x = y.getLeft()
        else:
            x = y.getRight()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getLeft():
                y.getPai().setLeft(x)
            else:
                y.getPai().setRight(x)
        if y != z:
            z.setChave(y.getChave())
            z.setValor(y.getValor())
                   
                
    
    def rotateLeft(self, t, x): #t eh a arvore, e x o no
        y = x.getRight()
        x.setRight(y.getLeft())
        x = y.getRight().getPai()
        y.setpai(x.getPai())
        if x.getPai() == None:
            t.setRaiz(y)
        else:
            if x == x.getPai().getLeft():
                x.getPai().setLeft(y)
            else:
                x.getPai().setRight(y)
        y.setLeft(x)
        x.setPai(y)
        
    def rotateRight(self, t, x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        x = y.getRight().getPai()
        y.setPai(x.getPai())
        if x.getPai() == None:
            t.setRaiz(y)
        else:
            if x == x.getPai().getRight():
                x.getPai().setRigt(y)
            else:
                x.getPai().setLeft(y)
        y.setRight(x)
        x.setPai(y)


import sys
tree=ArvoreBinaria()
ent=open("e11.txt")
out=open('e11s.txt',"w")
linha=None
caso=1
text=""
while True:
    linha=ent.readline()
    if linha=='':
        break
    tree.setRaiz(None)
    n=int(linha)
    text="Caso "+str(caso)+":\n"
    for i in range(n):
        linha=ent.readline()
        if linha.startswith("A"):
            l=linha.split(" ")
            x=int(l[1])
            tree.inserir(Node(x))
        elif linha.startswith("B"):
            l=linha.split(" ")
            x=int(l[1])
            tree.remover(tree.search(tree.getRaiz(), x))
        elif linha.startswith("C"):
            linha.split(" ")
            x=int(l[1])
            node=tree.search(tree.getRaiz(), x)
            try:
                e=tree.antecessor(node)
                while e.getChave()==x:
                    e=tree.antecessor(e)
                text+=str(e.getChave())+"\n"
            except:
                text+=str(tree.antecessor(node))+"\n"
        elif "PRE" in linha:
            lista=[]
            lista=tree.walk_in_preOrder(tree.getRaiz(),lista)
            if len(lista)>0:
                for i in lista:
                    text+=i+" "
                text=text[:-1]+"\n"
            else:
                text+="0\n"
        elif "IN" in linha:
            lista=[]
            lista=tree.walk_in_order(tree.getRaiz(),lista)
            if len(lista)>0:
                for i in lista:
                    text+=i+" "
                text=text[:-1]+"\n"
            else:
                text+="0\n"
        elif "POST" in linha:
            lista=[]
            lista=tree.walk_in_postOrder(tree.getRaiz(),lista)
            if len(lista)>0:
                for i in lista:
                    text+=i+" "
                text=text[:-1]+"\n"
            else:
                text+="0\n"
    caso+=1
    out.write(text)
    text=""
out.close()
