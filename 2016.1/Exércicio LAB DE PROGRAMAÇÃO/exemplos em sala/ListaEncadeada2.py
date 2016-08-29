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
        self.valor =  valor
        self.prox = None
        self.ant = None
    def getValor(self):
        return valor
    
    def setValor(self, novoValor):
        self.valor = novoValor
        
    def getProx(self):
        return self.prox
    
    def setProx(self, novoNo):
        self.prox = novoNo
        
    def getAnt(self):
        return self.ant
    
    def setAnt(self, novoNo):
        self.prevNode = novoNo


        
class ListEncad:
    def __init__(self, inicio, fim):
        self._inicio = None
        self._fim = None


    def __str__(self):
        NoAtual = self.inicio  
        if self.listVazia():
            print(" A lista está vazia.") 
        while NoAtual != None:
            print(NoAtual.getValor())
            NoAtual = NoAtual.getProx()
    
    def listVazia(self):
        return (self._inicio is None) or (self._fim is None)
    
    def InserirNoInicio(self, value):
        NovoNo = No(valor) 
        if self.listVazia(): 
            self.inicio =  self.fim = NovoNo
        else:                   
            NovoNo.setProx(NovoNo)
            NovoNo.setProx(self._inicio)
            NovoNo.setAnt(None)
            self._inicio = NovoNo
            
    def InserirNoFim(self, valor):   
        NovoNo = No(valor)  
        if self.listVazia(): 
            self.inicio = self.fim = NovoNo
        else:
            self._fim.setProx(NovoNo)
            NovoNo.setAnt(self._fim)
            NovoNo.setProx(None)
            self._fim = NovoNo

    def pesquisar (self, valor):
        if self.listVazia():
            return None
        NoAtual = self._inicio
        while NoAtual.getValor() != valor:
            NoAtual = NoAtual.getProx()
            if  NoAtual == None:
                return "Esse valor não foi encontrado!" 
        return NoAtual.getValor()
    
    def remover(self, valor):
        if self.listVazia():
            return None
        NoAtual = self._inicio
        while NoAtual.getValor() != Valor:
            NoAtual = NoAtual.getProx()
            if NoAtual == None:
                return "O valor não está na lista"
        if NoAtual == self._inicio:
            aux = self._inicio.getProx()
            self._inicio.setProx(None)
            aux.setProx(None)
            self._fim = aux
        elif NoAtual == self._fim:
            aux = self._fim.getAnt()
            self._fim.setProx(None)
            aux.setProx(None)
            self._fim = aux
        elif self.inicio == self._fim:
            self._inicio = self._fim = None
            return None
        else:
            aux = NoAtual.getAnt()
            aux2 = NoAtual.getProx()
            aux2.setAnt(aux)
            aux.setProx(aux2)
    def esvaziarList(self):
                  self._inicio = self._fim = None

class Pilha(ListEncad):
    def desempilhar(self):
        if self.listVazia():
            return" A fila está vazia!"
        else:
            PrimValNo = self._inicio.getValor()
            if self._inicio is self._fim:
                self._inicio = self.fim = None
            else:
                aux1 = self._fim.getAnt()
                self._fim.setAnt(None)
                aux1.setProx(None)
                self._fim = aux
            return PrimValNo
    
class Fila(ListEncad):           
    def removerInicio(self):
        if self.listVazia():
            return" A fila está vazia!"
        else:
            PrimValNo = self._inicio.getValor()
            if self._inicio is self._fim:
                self._inicio = self.fim = None
            else:
                aux2 = self._inicio.getProx()
                self._inicio.setProx(None)
                aux2.setAnt(None)
                self._inicio = aux2
            return PrimValNo


######################## Núcleo Programa ##################

import sys
arqEnt = open(sys.argv[1], 'r')
arqSaida = open(sys.argv[2], 'w')
FRefazer = Pilha()
Form = Pilha()
GuardTextos = Pilha()
frase = ''

while True:
    temp = 0
    linhas  = (arqEnt.readline()).split()
    tam = len(linha)
    if tam == 0:
        break
    func = linha[0]
    if func == "adicionar":
        FRefazer.esvaziarList()
        if GuardTextos.listVazia():
            w = linha[1:]
            GuardTextos.InserirNoFim(x)
        else:
            w = GuardTextos.desempilhar() + linha[1:]
            GuardTextos.InserirNoFim(x)
            
    elif linha[0] == "italico":
        FRefazer.esvaziarList()
        if Form.listVazia():
            Form.InserirNoFim("italico")
        else:
            w = Form.desempilhar() + "italico"
            Form.InserirNoFim(x)
    elif linha[0] == "negrito":
        FRefazer.esvaziarList()
        if Form.listVazia():
            Form.InserirNoFim("Negrito")
        else:
            w = Form.desempilhar() + "negrito"
            Form.InserirNoFim(x)
    elif linha[0] == "apagar":
        p = int(linha[1])
        aux1= GuardTextos.desempilhar()
        aux2 = aux1[ : -p]
        GuardTextos.InserirNoFim(aux1)
        GuardTextos.InserirNoFim(aux2)
    elif linha[0] == "desfazer":
        aux3 = GuardTextos.desempilhar()
        FRefazer.InserirNoFim(aux3)
    elif linha[0] == "refazer":
        if FRefazer.listVazia():
            pass
        else:
            elemt = FRefazer.desempilhar()
            GuardTextos.InserirNoFim(elemt)

guard = GuardTextos.desempilhar()
for x in range(len(guard)):
    FazerFrase = frase + "%s" % guard[x]
arqSaida.write(FazerFrase + "|" + str(Form.desempilhar()))
