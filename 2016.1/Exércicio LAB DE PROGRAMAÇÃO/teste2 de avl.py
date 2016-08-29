class no():
    def __init__(self, chave, dado = None ):
        self._dado = dado
        self._filhoesq = None
        self._filhodir = None
        self._pai = None
        self._chave = chave
        
    def getChave(self):
        return self._chave
    def setChave(self, x):
        self._chave = x
        
    def getDado(self):
        return self._dado
    def setDado(self, dado):
        self._dado = dado
        
    def getFilhoEsq(self):
        return self._filhoesq
    def setFilhoEsq(self, E):
        self._filhoesq = E
        
    def getFilhoDir(self):
        return self._filhodir
    def setFilhoDir(self, D):
        self._filhodir = D
        
    def getPai(self):
        return self._pai

    def setPai(self, P):
        self._pai = P
        
    def __str__(self):
        return str("No: " + str(self.getChave())+ "\t"+ "dado: "+ str(self.getDado()))
        
class arvoreAVL():
    def __init__(self):
        self._raiz = None
        
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, R):
        self._raiz = R
        
        
    def altura(self, x):#x eh um no
        if x == None:
            return -1
        hesq = self.altura(x.getFilhoEsq())
        hdir = self.altura(x.getFilhoDir())
        if hesq > hdir:
            return hesq + 1
        return hdir + 1
    
    def fatorBalanceamento(self, x):
        return self.altura(x.getFilhoDir()) - self.altura(x.getFilhoEsq())
        
    def percorrerEmOrdem(self, r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsq())
            print (r)
            self.percorrerEmOrdem(r.getFilhoDir())

    def percorrerPreOrdem(self, r):
        if r != None:
            print(r)
            self.percorrerEmOrdem(r.getFilhoEsq())
            self.percorrerEmOrdem(r.getFilhoDir())

    def percorrerPosOrdem(self, r):
        if r != None:
            self.percorrerEmOrdem(r.getFilhoEsq())
            self.percorrerEmOrdem(r.getFilhoDir())
            print(r)

    def buscaArvore(self, x, k):
        #busca o valor k , na raiz x
        if (x== None) or (x.getChave() == k):
            return x#retorna o no
        if k < x.getChave():
            return self.buscaArvore(x.getFilhoEsq(), k)
        else:
            return self.buscaArvore(x.getFilhoDir(), k)
    
    def minimo(self, x):
        while x.getFilhoEsq() != None:
            x = x.getFilhoEsq()
        return x
    def maximo(self, x):
        while x.getFilhoDir() != None:
            x = x.getFilhoDir()
        return x
    
    def sucessor(self, x):
        if x.getFilhoDir() != None:
            return self.minimo(x.getFilhoDir())
        y = x.getPai()
        while y != None and x is y.getFilhoDir():
            x = y 
            y = y.getPai()
        return y #pode ser None
    
    def antecessor(self, x):
        if x.getFilhoEsq() != None:
            return self.maximo(x.getFilhoEsq())
        y = x.getPai()
        while y != None and x == y.getFilhoEsq():
            x = y 
            y = y.getPai()
        return y    
            
    def inserir(self, z): #na arvore T, inserir z no prontinho
        No = no(z)
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if No.getChave() < x.getChave():
                x = x.getFilhoEsq()
            else:
                x = x.getFilhoDir()
        No.setPai(y)
        
        if y == None:
            self.setRaiz(No)
        elif No.getChave() < y.getChave():
            y.setFilhoEsq(No)
        else:
            y.setFilhoDir(No)
        No.setFilhoEsq(None)
        No.setFilhoDir(None)

    def transplant(self, u, v):
        if u._pai == None:
            self._raiz = v
        elif u == u.getPai().getFilhoEsq():
            u.getPai().setFilhoEsq(v)
        else:
            u.getPai().setFilhoEsq(v)
        if v != None:
            v.setPai(u.getPai())

    def delete(self, z):
        z = self.buscaArvore(self.getRaiz(), z)
        if z.getFilhoEsq() == None:
            self.transplant(z, z.getFilhodir())
        elif z.right == None:
            self.transplant(z, z.getFilhoEsq())
        else:
            y = self.minimum(z.getFilhodir())
            if y.getPai() != z:
                self.transplant(y, y.getFilhodir())
                y.setFilhodir(z.getFilhodir())
                y.getFilhoEsq().setPai(y)
            self.transplant(z, y)
            y.setFilhoEsq(z.getFilhodir())
            y.getFilhoEsq().setPai(y)


    '''def remover(self, z):# tira o no z
        No = self.buscaArvore(self.getRaiz(), z)
        if No.getFilhoEsq()== None or No.getFilhoDir()== None:
            y = No
        else: 
            y = self.sucessor(No)
        
        if y.getFilhoEsq() != None:
            x = y.getFilhoEsq()
        else:
            x = y.getFilhoDir()

        x.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(x)
        else:
            if y == y.getPai().getFilhoEsq():
                y.getPai().setFilhoEsq(x)
            else:
                y.getPai().setFilhoDir(x)
        if y != No:
            No.setChave(y.getChave())
            No.setDado(y.getDado())'''

            
    def rotateLeft(self, x): #t eh a arvore, e x o no
        y = x.getFilhoDir()
        x.setFilhoDir(y.getFilhoEsq())
        if y.getFilhoEsq()!= None:
            y.getFilhoEsq().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        elif x == x.getPai().getFilhoEsq():
            x.getPai().setFilhoEsq(y)
        else:
            x.getPai().setFilhoDir(y)
        y.setFilhoEsq(x)
        x.setPai(y)

    def rotateRight(self, x):
        y = x.getFilhoEsq()
        x.setFilhoEsq(y.getFilhoDir())
        if y.getFilhoDir()!= None:
            y.getFilhoDir().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        elif x == x.getPai().getFilhoDir():
                x.getPai().setFilhoDir(y)
        else:
            x.getPai().setFilhoEsq(y)
        y.setFilhoDir(x)
        x.setPai(y)

    def doubleRotateRight(self, x):  # x eh no
        filhoesq = x.getFilhoEsq()
        self.rotateLeft(filhoesq)
        self.rotateRight(x)

    def doubleRotateleft(self, x):
        filhodir = x.getFilhoDir()
        self.rotateRight(filhodir)
        self.rotateLeft(x)

 
minhaArvore = arvoreAVL()
minhaArvore.inserir(10)
minhaArvore.inserir(20)
minhaArvore.inserir(30)
print("Em Ordem:")
minhaArvore.percorrerEmOrdem(minhaArvore.getRaiz())
minhaArvore.rotateLeft(minhaArvore.getRaiz())
print("Em Pré-ordem")
minhaArvore.delete(10)
minhaArvore.percorrerPreOrdem(minhaArvore.getRaiz())
print("Em Pós-ordem")
minhaArvore.percorrerPosOrdem(minhaArvore.getRaiz())
