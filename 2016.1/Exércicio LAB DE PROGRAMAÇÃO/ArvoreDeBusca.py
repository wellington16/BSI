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
        return str("Noh: "+str(self.getChave()) +" "+ self.getDado())
        
class ArvoreDeBuscaBinaria():
    def __init__(self):
        self._raiz = None
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, no):
        self._raiz=no
    def percorrerEmOrdem(self,x):
        if x != None:
            self.percorrerEmOrdem(x.getFilhoEsq()) #PERCORRER SUB ARVORE ESQUERDA
            print("O noh eh esse: "+str(x)) #VISITA
            self.percorrerEmOrdem(x.getFilhoDir()) #PERCORRER SUB ARVORE DIREITA
        
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
                    

chaves = [5, 44, 88, 90, 33, 31, 100, 70]
dados = ["felipe", "lucas", "danilo", "nichene", "bruna", "wellington", "igor", "Eridson"]
minhaarvore = ArvoreDeBuscaBinaria()
for i in range(len(chaves)):
    minhaarvore.inserir(No(chaves[i],dados[i]))
print("arvore com danilo")
minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())
minhaarvore.remover(minhaarvore.buscar(minhaarvore.getRaiz(), 88))
print("arvore sem danilo")
minhaarvore.percorrerEmOrdem(minhaarvore.getRaiz())
        