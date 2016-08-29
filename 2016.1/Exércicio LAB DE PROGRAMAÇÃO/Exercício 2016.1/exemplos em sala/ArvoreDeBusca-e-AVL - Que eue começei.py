#coding:utf-8
class No:
    def __init__(self,chave,dado):
        self._dado = dado
        self._filhoesq = None
        self._filhodir = None
        self._pai = None
        self._chave = chave
    def getChave(self):
        return self._chave
    def setChave(self,k):
        self._chave = k
    def getDado(self):
        return self._dado
    def setDado(self,dado):
        self._dado = dado
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
        return str("Nó: "+str(self.getChave()) +" "+ self.getDado())    
        
class ArvoreDeBuscaBinaria:
    def __init__(self):
        self._raiz = None
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, no):
        self._raiz=no
    def percorrerEmOrdem(self,x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq()) #PERCORRER SUB ARVORE ESQUERDA
            print("O nó é esse: "+str(x)) #VISITA
            self.percorrerEmOrdem(x.getFilhoDir()) #PERCORRER SUB ARVORE DIREITA
    def percorrerEmPreOrdem(self,x):
                print("O nó é esse: "+x) #visitando
                percorrerEmOrdem(x.getFilhoEsq)#PercorrendoArvorePelaEsquerda
                percorrerEmOrdem(x.getFilhoDir)#PercorrendoArvorePelaDireita
    def percorrerEmPosOrdem(self,x):
                percorrerEmOrdem(x.getFilhoEsq)#PercorrendoArvorePelaEsquerda
                percorrerEmOrdem(x.getFilhoDir)#PercorrendoArvorePelaDireita
                print("O no é esse: "+x) #visitando
        
    def buscar(self,x,k):
        if x == None or x.getChave() == k:
            return x
        if k < x.getChave():
            return self.buscar(x.getFilhoEsq(),k)
        else:
            return self.buscar(x.getFilhoDir(),k)
    
    def minimo(self,x):
        while x.getFilhoEsq() is not None:
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
        if x.getFilhoEsq() != None:
            return self.maximo(x.getFilhoEsq)
        y = x.getPai()
        while y != None and x is y.getFilhoEsq():
            x = y
            y = y.getPai()
        return y
    def inserir(self,z):
        y=None
        x = self.getRaiz()
        while x != None:
            y=x
            if z.getChave() < x.getChave():
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
            
class ArvoreAvl(ArvoreDeBuscaBinaria):
    def altura(self,x):
        if x == None:
            return -1
        hesq= self.altura(x.getFilhoEsq())
        hdir= self.altura(x.getFilhoDir())
        if hesq > hdir:
            return +1
        return +1
    def fatorBalanceamento(self,x):
        return self.altura(x.getFilhoDir()) - self.altura(x.getFilhoEsq())


    def rotaesq(self):
        x.getFilhoDir().getFilhoEsq(y)
        y=(self.FilhoEsq())
        if y.getFilhoEsq != None:
            y.getPai().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        else:
            if x == x.getPai().setFilhoEsq():
                X.getPai().setFilhoEsq(y)
            else:
                x.getPai().setFilhoDir(y)
            y.setFilhoEsq(x)
            x.setPai(y)

    def rotadir(self):
        y=self.FilhoDir()
        x.getFilhoEsq() .getFilhoDir(y)
        if y.getFilhoDir!=None:
            y.getPai().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() ==None:
            self.setRaiz(y)
        else:
            if x == x.getPai().setFilhoDir():
                X.getPai().setFilhoDir(y)
            else:
                x.getPai().setFilhoEsq(y)
            y.setFilhoEsq(x)
            x.setPai(y)
        self.fatorBalanceamento()
            
    def rotDupESq(self):
        d=self.getFilhoesq.rotaesq()
        e=self.rotadir()
        self.fatorBalanceamento()
        
    def rotDupDir(self):
        f=self.getFilhoDir.rotadir()
        g=self.rotaesq()
        self.fatorBalanceamento()
        
    def inserirNaAvl(self,w):
            self.w = w
            if w <= self.w:
                if not self.setFilhoesq:
                    self.setFilhoesq=No(w)
                else:
                    self.setFilhoesq.inserirNaAvl(w)
            else:
                if not self.setFilhodir:
                    self.setFilhodir=No(w)
                else:
                    self.setFilhodir.inserirNaAvl(w)
            self.fatorBalanceamento()
            if self.altura(x.getFilhoEsq()) < -1:
                self.rotaesq()
            if self.altura(x.getFilhoDir()) > +1:
                self.rotadir()
                
    def removerDaAvl(self):
        self.remover()
        self.fatorBalanceamento()
        
            
                    

chaves = [5, 44, 88, 90, 33, 31, 100, 70]
dados = ["9", "7", "6", "5", "4", "3", "2", "1"]
minhaarvore = ArvoreAvl()
for i in range(len(chaves)):
    a = No(chaves[i],dados[i])
    minhaarvore.inserir(No(chaves[i],dados[i]))
print("arvore com 88")
minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())
minhaarvore.remover(minhaarvore.buscar(minhaarvore.getRaiz(), 88))
print("arvore sem 88")
minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())

'''
minhaAvl= ArvoreAvl()

for i in chaves:
    t  = No(chaves[i], dados[i])
    arvore.inserirNaAvl(chaves[i])

arvore.minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())

'''

# como dicidir as rotações
'''FuncDecisao():
 Calcule Q = R - l

Se -1 <= Q <= 1 então "nó balanceado"
Se Q > 1:
    Se a sub-arvore da direita tem Q < 0:
        Rotação dupla à esquerda
    Senão:
        Rotação simples à esquerda
Senão:
    Se a sub-arvore da esquerda tem Q > 0:
        Rotação dupla à direita
    Senão:
        Rotação simples à direita
'''        
        
