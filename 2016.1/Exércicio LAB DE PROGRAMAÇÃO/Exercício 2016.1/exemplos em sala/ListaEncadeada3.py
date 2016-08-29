

def desfazer():
    pass


def refazer():
    pass
'''Exercício para já

A função "desfazer" está presente em varios aplicativos.
Ela permite que o usuário volte a um ponto anterior da
confecção de seu documento. Há também a função"refazer",
que leva a edição do documento a um ponto posterior em um
histórico de alterações neste item.

Tarefa:
    Implementar aS funções "desfazer" e "refazer" em um editor de textos
    tal aplicativo deverá executar um conjunto de comandos simples: adcionar,
    itálico, negrito, apagar, desfazer e refazer.

-------------------------------------------------------------------------------'''


class No:
    def __init__(self, valor):
        self._valor =  valor
        self._prox = None
    def getValor(self):
        return valor
    
    def setValor(self, valor):
        self._valor = valor 
    def getProx(self):
        return self._prox
    
    def setProx(self, novoNo):
        self._prox = novoNo
        
class ListEncad:
    def __init__(self, inicio, fim):
        self.inicio = None
        self.fim = None
    def __str__(self):

        if self.listVazia():
            return 
        atual = self.inicio
        imprimir = " A lista:"  
        while atual is not None:
            imprimir += str( atual.getData() ) + " "
            atual = atual.getProx()
        return imprimir
    def listVazia(self):
        return self.inicio is None
    
    def InserirInicio(self, value):
        
        NovoNo = No(valaor) 
        if self.listVazia(): 
            self.inicio =  self.fim = NovoNo
        else:                   
            NovoNo.setProx(self.inicio)
            self.inicio = NovoNo
    def InserirFim(self, value):
        
        NovoNo = No(valor)  
        
        if self.listVazia(): 
            self.inicio = self.fim = NovoNo
        else:
            self.fim.setProx(NovoNo)
            self.fim = NovoNo

    def pesquisar (self, valor):
        while self.inicio != None:
            if  self.inicio.getValor == valor:
                return o
            self.inicio = self.inicio.getProx()
        return None

      #=========================================================
    def remover(self,dado):
        
        if self.inVazia():
            return("Erro lista esta vazia")
        else:
            x=self.pesquisar(dado)
            if x==None:
                return("Elemento não esta na lista")
            elif self.pesquisar(dado)==self._inicio:
                self._inicio.getprox().setant(None)
                self._inicio=self._inicio.getprox()
            elif self.pesquisar(dado)==self._fim:
                self._fim.getant().setprox(None)
                setant=self._fim.getant()
            else:
                (x.getprox()).setant(x.getant())
                (x.getant()).setprox(x.getprox())
                x.setprox(None)
                x.setant(None)
#Fim da conversa no bate-papo
#============================================================

class Pilha(ListEncad):
    
    def empilhar(self, valor):
        self.InserirInicio
        
    def desempilhar(self, valor):
        self.removerIncio()
    
class Fila(ListEncad):
    def InserirNofim(self, valor):
        self.InserirInicio()
        
    def removerInicio(self, valor):
        self.removerIncio()


x=ListEncad()
x.InserirFim(13)
x.InserirFim(11)
x.InserirFim(18)
x.InserirFim(15)
