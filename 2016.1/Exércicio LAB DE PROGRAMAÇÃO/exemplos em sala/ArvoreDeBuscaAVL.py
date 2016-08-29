class No:
    def __init__(self, chave, dado=None):
        self._dado = dado
        self._filhoesq = None
        self._filhodir = None
        self._pai = None
        self._chave = chave
        self._altura = None


    def getAltura(self):
        return self._altura


    def setAltura(self, a):
        self._altura = a


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

class ArvoreAvl:
    def __init__(self):
        self._raiz = None

    def  getRaiz(self):
        return self._raiz

    def setRaiz(self, x):
        self._raiz = x

    def percorrerEmOrdem(self, x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq())  # PERCORRER SUB ARVORE ESQUERDA
            print(x)  # VISITA
            self.percorrerEmOrdem(x.getFilhoDir())  # PERCORRER SUB ARVORE DIREITA

    def percorrerEmPreOrdem(self, x):
        if x != None:
            print(x)  # visitando
            self.percorrerEmOrdem(x.getFilhoEsq())  # PercorrendoArvorePelaEsquerda
            self.percorrerEmOrdem(x.getFilhoDir())  # PercorrendoArvorePelaDireita

    def percorrerEmPosOrdem(self, x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq())  # PercorrendoArvorePelaEsquerda
            self.percorrerEmOrdem(x.getFilhoDir())  # PercorrendoArvorePelaDireita
            print(x)  # visitando

    def buscar(self, x, k):
        if x == None or x.getChave() == k:
            return x
        if k < x.getChave() and k != None:

            return self.buscar(x.getFilhoEsq(), k)
        elif k < x.getChave() and k != None:
            return self.buscar(x.getFilhoDir(), k)

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
        while y != None and x == y.getFilhoDir():
            x = y
            y = y.getPai()
        return y

    def antecessor(self, x):
        if x.getFilhoEsq() != None:
            return self.maximo(x.getFilhoEsq())
        y = x.getPai()
        while y != None and x == y.getFilhoEsq():
            x = y
            y = y.getPai()
        return y

    def rotadir(self, x):
        y = x.getFilhoEsq()
        x.setFilhoEsq(y.getFilhoDir())
        if y.getFilhoDir() != None:
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

    def rotDupESq(self, x):
        if x.getFilhoDir() is not x.getFilhoDir():
            self.rotadir(x.getFilhodir())
            self.rotaesq(x)

    def rotDupDir(self, x):
        if x.getFilhoEsq() != None:
            self.rotaesq(x.getFilhoEsq())
            self.rotadir(x)

    def altura(self, x):
        if x == None:
            return -1
        hesq = self.altura(x.getFilhoEsq())
        hdir = self.altura(x.getFilhoDir())
        if hesq > hdir:
            return hesq + 1
        return hdir + 1

    def fatorBalanceamento(self, x):
        return (self.altura(x.getFilhoDir()) - self.altura(x.getFilhoEsq()))

    def balancear(self, x):
        #no = self.buscar(self.getRaiz(), x)
        if self.fatorBalanceamento(x) > 1:
            if self.fatorBalanceamento(x.getFilhoDir()) < 0:
                self.rotDupESq(x)
            else:
                self.rotaesq(x)

        if self.fatorBalanceamento(x) < -1:
            if self.fatorBalanceamento(x.getFilhoEsq()) > 0:
                self.rotDupDir(x)
            else:
                self.rotadir(x)

    def balancearAvT(self, x):
        if x != None:
            self.balancearAvT(x.getFilhoEsq())
            self.balancearAvT(x.getFilhoDir())
            self.balancear(x)
        else:
            pass

    def inserir(self, z, w):
        no = No(z, w)
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

    def remover(self, z):
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
        self.balancearAvT(self.getRaiz())

a = ArvoreAvl()

a.inserir(60, 20)
a.inserir(70, 20)
a.inserir(80, 20)
a.inserir(85, 20)
a.inserir(90, 20)
a.inserir(100, 20)



a.percorrerEmOrdem(a.getRaiz())
print("##############")
#a.remover(a.buscar(a.getRaiz(), 44))
a.percorrerEmOrdem(a.getRaiz())
print("x############")
a.percorrerEmPosOrdem(a.getRaiz())
#a.remover(a.buscar(a.getRaiz(), 639))
print("###########jhbcdsb")
a.percorrerEmPreOrdem(a.getRaiz())
