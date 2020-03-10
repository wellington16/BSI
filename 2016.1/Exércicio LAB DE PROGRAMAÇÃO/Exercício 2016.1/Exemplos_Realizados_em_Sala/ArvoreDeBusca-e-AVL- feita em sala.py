#coding:utf-8
class No:
    def __init__(self, chave, dado = None):
        self._dado = dado
        self._filhoesq = None
        self._filhodir = None
        self._pai = None
        self._chave = chave
        self._altura = None

    def getAltura(self):
            return self._altura

    def setAltura(self, A):
            self._altura = A

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
        self._filhoesq = filho

    def getFilhoDir(self):
        return self._filhodir

    def setFilhoDir(self,filho):
        self._filhodir = filho

    def getPai(self):
        return self._pai

    def setPai(self,pai):
        self._pai = pai

    def __str__(self):
        return str("No: " + str(self.getChave())+ "\t"+ "dado: "+ str(self.getDado()))    
        
class ArvoreDeBuscaBinaria:
    def __init__(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz

    def setRaiz(self, no):
        self._raiz = no

    def percorrerEmOrdem(self,x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq()) #PercorrendoArvorePelaEsquerda
            print("O " + str(x)) #visitando
            self.percorrerEmOrdem(x.getFilhoDir()) #PercorrendoArvorePelaDireita
    def percorrerEmPreOrdem(self,x):
            print("O " + str(x)) #visitando
            self.percorrerEmOrdem(x.getFilhoEsq())#PercorrendoArvorePelaEsquerda
            self.percorrerEmOrdem(x.getFilhoDir())#PercorrendoArvorePelaDireita
    def percorrerEmPosOrdem(self,x):
            self.percorrerEmOrdem(x.getFilhoEsq())#PercorrendoArvorePelaEsquerda
            self.percorrerEmOrdem(x.getFilhoDir())#PercorrendoArvorePelaDireita
            print("O No: " + str(x)) #visitando
        
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

    def balancear(self, x):
        Q = self.fatorBalanceamento(x)
        if Q > 1:
            if self.fatorBalanceamento(x.getFilhoDir()) < 0:
                self.rotDupESq(x)
            else:
                self.rotaesq(x)

        if Q < -1:
            if self.fatorBalanceamento(x.getFilhoEsq()) > 0:
                self.rotDupDir(x)
            else:
                self.rotadir(x)

    def balancearAvT(self, no):
        if no != None:
            self.balancearAvT(no.getFilhoEsq())
            self.balancearAvT(no.getFilhoDir())
            self.balancear(no)

    def inserir(self, z):
        no = No(z)
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if no.getChave() < x.getChave():
                x = x.getFilhoEsq()
            else:
                x = x.getFilhoDir()
        no.setPai(y)
        if y == None:
            self.setRaiz(no)
        else:
            if no.getChave() < y.getChave():
                y.setFilhoEsq(no)
            else:
                y.setFilhoDir(no)
        self.balancearAvT(self.getRaiz())

    def remover(self,z):
        no = self.buscar(self.getRaiz(), z)
        if no.getFilhoEsq() == None or  no.getFilhoDir() == None:
            y = no
        else:
            y = self.sucessor(no)
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
        if y != no:
             no.setChave(y.getChave())
             no.setDado(y.getDado())
        self.balancearAvT(self.getRaiz())

class ArvoreAvl(ArvoreDeBuscaBinaria):
    def altura(self,x):
        if x == None:
            return -1
        hesq = self.altura(x.getFilhoEsq())
        hdir = self.altura(x.getFilhoDir())
        if hesq > hdir:
            return hesq + 1
        return hdir + 1
        
    def fatorBalanceamento(self,x):
        return self.altura(x.getFilhoDir()) - self.altura(x.getFilhoEsq())

    def rotaesq(self, x):
        y = x.getFilhoDir()
        x.setFilhoDir(y.getFilhoEsq())
        if y.getFilhoEsq() != None:
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

    def rotadir(self, x):
        y = x.getFilhoEsq()
        x.setFilhoEsq(y.getFilhoDir())
        if y.getFilhoDir()!= None:
            y.getFilhoEsq().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() == None:
            self.setRaiz(y)
        elif x == x.getPai().getFilhoDir():
            x.getPai().setFilhoDir(y)
        else:
            x.getPai().setFilhoEsq(y)
        y.setFilhoDir(x)
        x.setPai(y)
            
            
    def rotDupESq(self,x):
        dir =x.getFilhodir()
        self.rotadir(dir)
        self.rotaesq(x)

    def rotDupDir(self,x):
        esq = x.getFilhoEsq()
        self.rotaesq(esq)
        self.rotadir(x)

    def inserirNaAvl(self,No):
        self.inserir(No)
            
    def removerDaAvl(self, No):
        self.remover(No)

a = ArvoreAvl()

a.inserir(10)
a.inserir(30)
a.inserir(20)
a.inserir(25)
a.inserir(27)
a.inserir(26)
'''a.inserir(2)
a.inserir(16)
a.inserir(100)
a.inserir(1702)'''


a.percorrerEmOrdem(a.getRaiz())
print("##############")
a.remover(44)
print("x############")
a.percorrerEmPosOrdem(a.getRaiz())
a.remover(739)
print("###########jhbcdsb")
a.percorrerEmPreOrdem(a.getRaiz())


            
'''chaves = [5, 44, 88, 90, 33, 31, 100, 70]
dados = ["9", "7", "6", "5", "4", "3", "2", "1"]
minhaarvore = ArvoreAvl()
for i in range(len(chaves)):
    a = No(chaves[i],dados[i])
    minhaarvore.inserirNaAvl(No(chaves[i],dados[i]))
print("arvore com 88")
minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())
minhaarvore.rotaesq(minhaarvore.getRaiz())
minhaarvore.remover(minhaarvore.buscar(minhaarvore.getRaiz(), 88))
print("arvore sem 88")
minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())


como dicidir as rotaÃ§Ãµes
FuncDecisao():
 Calcule Q = R - l

Se -1 <= Q <= 1 entÃ£o "nÃ³ balanceado"
Se Q > 1:
    Se a sub-arvore da direita tem Q < 0:
        RotaÃ§Ã£o dupla Ã  esquerda
    SenÃ£o:
        RotaÃ§Ã£o simples Ã  esquerda
SenÃ£o:
    Se a sub-arvore da esquerda tem Q > 0:
        RotaÃ§Ã£o dupla Ã  direita
    SenÃ£o:
        RotaÃ§Ã£o simples Ã  direita

    def balancear(self, x):
        if x != None:
            Q = self.fatorBalanceamento(x)
            if Q >= (-1) and Q <= 1:
                no = no.getPai()
            if Q > 1:
                if self.fatorBalanceamento(no.getFilhoDir()) < 0:
                    no =  self.rotDupESq(no)
                else:
                    no = self.rotaesq(no)
            elif Q < -1:
                if self.fatorBalanceamento(no.getFilhoEsq()) > 0:
                    no = self.rotDupDir(no)
                else:
                    no = self.rotadir(no)
'''
        
