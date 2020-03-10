class No:
    def __init__(self, chave, data):
        self._data = data
        self._chave = chave
        self._pai = None
        self._left = None
        self._right = None
        self._altura = None
        
    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data = data
    
    def getChave(self):
        return self._chave
    
    def setChave(self, x):
        self._chave = x
    
    def getPai(self):
        return self._pai
    
    def setPai(self, P):
        self._pai = P
    
    def getLeft(self):
        return self._left
    
    def setLeft(self, L):
        self._left = L
    
    def getRight(self):
        return self._right
    
    def setRight(self, R):
        self._right = R
    
    def getAltura(self):
        return self._altura
    
    def setAltura(self, A):
        self._altura = A
        
    def __str__(self):
        string = 'Chave: '+str(self.getChave())+'\t'+'dado: '+str(self.getData())
        return string

class ArvoreAVL:
    def __init__(self):
        self._root = None
    
    def getRoot(self):
        return self._root
    
    def setRoot(self, x):
        self._root = x
    
    def percorrerPreOrdem(self, x):
        if x != None:
            print(x)
            self.percorrerPreOrdem(x.getLeft())
            self.percorrerPreOrdem(x.getRight())
    
    def percorrerEmOrdem(self, x):
        if x != None:
            self.percorrerEmOrdem(x.getLeft())
            print(x)
            self.percorrerEmOrdem(x.getRight())
    
    def percorrerPosOrden(self, x):
        if x != None:
            self.percorrerPosOrden(x.getLeft())
            self.percorrerPosOrden(x.getRight())
            print(x)
    
    def buscar(self, x, k):
        if (x == None) or (k == x.getChave()):
            return x
        elif k < x.getChave():
            return self.buscar(x.getLeft(), k)
        else:
            return self.buscar(x.getRight(), k)
    
    def buscaIterativa(self, x, k):
        while(x != None) and (k != x.getChave()):
            if (k < x.getChave()):
                x = x.getLeft()
                x = x.getRight()
        return x
    
    def maximo(self, x):
        while x.getRight() != None:
            x = x.getRight()
        return x
    
    def minimo(self, x):
        while x.getLeft() != None:
            x = x.getLeft()
        return x
    
    def sucessor(self, x):
        if x.getRight() != None:
            return self.minimo(x.getRight())
        y = x.getPai()
        while y != None and x == y.getRight():
            x = y
            y = y.getPai()
        return y
    
    def antecessor(self, x):
        if x.getLeft() != None:
            return self.maximo(x.getLeft())
        y = x.getPai()
        while y != None and x == y.getLeft():
            x = y
            y = y.getPai()
        return y
    
    def rotateLeft(self, x):
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() != None:
            y.getLeft().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRoot(y)
        elif x == x.getPai().getLeft():
            x.getPai().setLeft(y)
        else:
            x.getPai().setRight(y)
        y.setLeft(x)
        x.setPai(y)
    
    def rotateRight(self, x):
        y = x.getLeft()
        x.setLeft(y.getRight())
        if y.getRight() != None:
            y.getRight().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRoot(y)
        elif x == x.getPai().getRight():
            x.getPai().setRight(y)
        else:
            x.getPai().setLeft(y)
        y.setRight(x)
        x.setPai(y)
    
    def doubleRotateLeft(self, x):
        fdir = x.getRight()
        self.rotateRight(fdir)
        self.rotateLeft(x)
    
    def doubleRotateRight(self, x):
        fesq = x.getLeft()
        self.rotateLeft(fesq)
        self.rotateRight(x)
    
    def altura(self, x):
        if x == None:
            return -1
        hleft = self.altura(x.getLeft())
        hright = self.altura(x.getRight())
        if hleft > hright:
            return hleft + 1
        return hright + 1
    
    def fatorBalanceamento(self, x):
        return self.altura(x.getRight())-self.altura(x.getLeft())
    
    def balancearArvore(self, x):
        if x != None:
            self.balancearArvore(x.getLeft())
            self.balancearArvore(x.getRight())
            self.balancear(x)
    
    def balancear(self, x):
        if self.fatorBalanceamento(x) > 1:
            if self.fatorBalanceamento(x.getRight()) < 0:
                self.doubleRotateLeft(x)
            else:
                self.rotateLeft(x)
        if self.fatorBalanceamento(x) < -1:
            if self.fatorBalanceamento(x.getLeft()) > 0:
                self.doubleRotateRight(x)
            else:
                self.rotateRight(x)
                
    def inserir(self, z):
        y = None
        x = self.getRoot()
        while x != None:
            y = x
            if z.getChave() < x.getChave():
                x = x.getLeft()
            else:
                x = x.getRight()
        z.setPai(y)
        if y == None:
            self.setRoot(z)
        else:
            if z.getChave() < y.getChave():
                y.setLeft(z)
            else:
                y.setRight(z)
        self.balancearArvore(self.getRoot())
    
    def remover(self, z):
        if z.getLeft() == None or z.getRight() == None:
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
            self.setRoot(x)
        else:
            if y == y.getPai().getLeft():
                y.getPai().setLeft(x)
            else:
                y.getPai().setRight(x)
        if y != z:
            z.setChave(y.getChave())
            z.setData(y.getData())
        self.balancearArvore(self.getRoot())

a = ArvoreAVL()
a.inserir(No(44, 20))
a.inserir(No(239, 20))
a.inserir(No(1601, 20))
a.inserir(No(1000, 20))
a.inserir(No(4, 20))
a.inserir(No(639, 20))
a.inserir(No(13, 20))
a.inserir(No(31, 20))
a.inserir(No(200, 20))
a.remover(a.buscar(a.getRoot(), 44 ))
a.percorrerEmOrdem(a.getRoot())