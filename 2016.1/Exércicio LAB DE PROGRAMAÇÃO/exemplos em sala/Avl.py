class No:
    def __init__(self, chave, dado=None):
        self._dado = dado
        self._filhoesq = None
        self._filhodir = None
        self._pai = None
        self._chave = chave

    def getChave(self):
        return self._chave

    def setChave(self, k):
        self._chave = k

    def getDado(self):
        return self._dado

    def setDado(self, dado):
        self._dado = dado

    def getFilhoEsq(self):
        return self._filhoesq

    def setFilhoEsq(self, filho):
        self._filhoesq = filho

    def getFilhoDir(self):
        return self._filhodir

    def setFilhoDir(self, filho):
        self._filhodir = filho

    def getPai(self):
        return self._pai

    def setPai(self, pai):
        self._pai = pai

    def __str__(self):
        return str("No: " + str(self.getChave()) + "\t" + "dado: " + str(self.getDado()))


class ArvoreBB:
    def __init__(self):
        self._raiz = None

    def getRaiz(self):
        return self._raiz

    def setRaiz(self, no):
        self._raiz = no

    def percorrerEmOrdem(self, x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq())  # PERCORRER SUB ARVORE ESQUERDA
            print("O " + str(x))  # VISITA
            self.percorrerEmOrdem(x.getFilhoDir())  # PERCORRER SUB ARVORE DIREITA

    def percorrerEmPreOrdem(self, x):
        print("O " + str(x))  # visitando
        self.percorrerEmOrdem(x.getFilhoEsq())  # PercorrendoArvorePelaEsquerda
        self.percorrerEmOrdem(x.getFilhoDir())  # PercorrendoArvorePelaDireita

    def percorrerEmPosOrdem(self, x):
        self.percorrerEmOrdem(x.getFilhoEsq())  # PercorrendoArvorePelaEsquerda
        self.percorrerEmOrdem(x.getFilhoDir())  # PercorrendoArvorePelaDireita
        print("O No: " + str(x))  # visitando

    def buscar(self, x, k):
        if x == None or x.getChave() == k:
            return x
        if k < x.getChave():
            return self.buscar(x.getFilhoEsq(), k)
        else:
            return self.buscar(x.getFilhoDir(), k)

    def minimo(self, x):
        while x.getFilhoEsq() is not None:
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
        return y

    def antecessor(self, x):
        if x.getFilhoEsq() != None:
            return self.maximo(x.getFilhoEsq)
        y = x.getPai()
        while y != None and x is y.getFilhoEsq():
            x = y
            y = y.getPai()
        return y

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

class ArvAvl(ArvoreBB):
    def altura(self, x):
        if x == None:
            return -1
        hesq = self.altura(x.getFilhoEsq())
        hdir = self.altura(x.getFilhoDir())
        '''if hesq > hdir:
            return hesq + 1
        return hdir + 1'''
        return (max(hesq, hdir) + 1)