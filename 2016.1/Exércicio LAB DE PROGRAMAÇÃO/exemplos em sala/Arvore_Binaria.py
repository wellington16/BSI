class No:
    #def __init__(self, chave, dado):
    def __init__(self, chave):
        #self.__dado = dado
        self.__filhoesq = None
        self.__filhodir = None
        self.__pai = None
        self.__chave = chave
    def getChave(self):
        return self.__chave
    def setChave(self, nova):
        self.__Chave = nova
    def getDado(self):
        return self.__dado
    def setDado(self, dado):
        self.__dado = dado
    def getFilhoesq(self):
        return self.__filhoesq
    def setFilhoesq(self, filho):
        self.__filhoesq = filho
    def getFilhodir(self):
        return self.__filhodir
    def setFilhodir(self, filho):
        self.__filhodir = filho
    def getPai(self):
        return self.__pai
    def setPai(self, pai):
        self.__pai = pai
    def __str__(self):
        return str("No: " + str(self.getChave()))# + " " + self.getDado())
        
class ArvoreBinaria(No):
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self, novo):
        self.__raiz = novo
    def percorrerEmOrdem(self, x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoesq())
            print ("o noh eh: " + str(x))
            self.percorrerEmOrdem(x.getFilhodir())
    def percorrerPreOrdem(self, x):
        if x != None:
            print ("o noh eh: " + x)
            self.percorrerPreOrdem(x.getFilhoesq())
            self.percorrerPreOrdem(x.getFilhodir())
    def percorrePosOrdem(self, x):
        if x != None:
            self.percorrePosOrdem(x.getFilhoesq())
            self.percorrePosOrdem(x.getFilhodir())
            print ("o noh eh: " + x)
    def buscar(self, x, k):
        if x == None or x.getChave() == k:
            return x 
        if k < x.getChave():
            return self.buscar(x.getFilhoesq(), k)
        else:
            return self.buscar(x.getFilhodir(), k)
    def minimo(self, x):
        while x.getFilhoesq() is not None:
            x = x.getFilhoesq()
        return x
    def maximo(self, x):
        while x.getFilhodir() != None:
            x = x.getFilhodir()
        return x
    def sucessor(self, x):
        if x.getFilhodir() != None:
            return self.minimo(x.getFilhodir())
        y = x.getPai()
        while y != None and x is y.getFilhodir():
            x = y
            y = y.getPai()
        return y
    def predecessor(self, x):
        if x.getFilhoesq() != None:
            return self.maximo(x.getFilhoesq)
        y = x.getPai()
        while y != None and x is y.getFilhoesq():
            x = y
            y = y.getPai()
        return y
    def inserir (self, z):
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if z.getChave() < x.getChave():
                x = x.getFilhoesq()
            else:
                x = x.getFilhodir()
        z.setPai(y)
        if y == None:
            self.setRaiz(z)
        else:
            if z.getChave() < y.getChave():
                y.setFilhoesq(z)
            else:
                y.setFilhodir(z)
        
    def remover(self, x):
        if x.getFilhoesq() == None or x.getFilhodir() == None:
            y = x
        else:
            y = self.sucessor(x)
        if y.getFilhoesq() != None:
            z = y.getFilhoesq()
        else:
            z = y.getFilhodir()
        if z != None:
            z.setPai(y.getPai())
        if y.getPai() == None:
            self.setRaiz(z)
        else:
            if y == y.getPai().getFilhoesq():
                y.getPai().setFilhoesq(z)
            else:
                y.getPai().setFilhodir(z)
        if y != x:
            x.setChave(y.getChave())
            x.setDado(y.getDado())
        return y
    

dados = ["lucas", "tiago", "joao", "maria", "jose", "gustavo", "pablo", "lucio"]
arvore = ArvoreBinaria()
for i in dados:
    t = No(i)
    arvore.inserir(t)


arvore.percorrerEmOrdem(arvore.getRaiz())
arvore.remover(arvore.buscar(arvore.getRaiz(), "lucio"))
print("aqui")
arvore.percorrerEmOrdem(arvore.getRaiz())
