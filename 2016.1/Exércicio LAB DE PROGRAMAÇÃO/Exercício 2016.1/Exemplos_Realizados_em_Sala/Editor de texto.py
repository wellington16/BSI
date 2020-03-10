'''
Exercício para já

A função "desfazer" está presente em varios aplicativos.
Ela permite que o usuário volte a um ponto anterior da
confecção de seu documento. Há também a função"refazer",
que leva a edição do documento a um ponto posterior em um
histórico de alterações neste item.

Tarefa:
    Implementar aS funções "desfazer" e "refazer" em um editor de textos
    tal aplicativo deverá executar um conjunto de comandos simples: adcionar,
    itálico, negrito, apagar, desfazer e refazer.
'''

import sys

class No:
    def __init__(self, valor):
        self.valor =  valor
        self.prox = None
        self.ant = None
        
    def getValor(self):
        return self.valor
    
    def setValor(self, novodado):
        self.prox = novoDado
    
    def getNovValor(self):
        return self.prox
    
    def setNovValor(self, novoNo):
        self.prox = novoNo
        
    def getAntValor(self):
        return self.ant
    
    def setAntValor(self, novoNo):
        self.ant = novoNo
    

class ListEncad:
    def __init__(self):
        self._inicio = None
        self._fim = None
        
    # Verifica se a lista está vazia  
    def listVazia(self):
        return (self._inicio is None) or (self._fim is None)

    #Inseri no inicio
    def InserirNoInicio(self, valor):
        NovoNo = No(valor) 
        if self.listVazia(): 
            self._inicio =  self._fim = NovoNo
        else:                   
            self._inicio.setAntValor(NovoNo)
            NovoNo.setNovValor(self._inicio)
            NovoNo.setAntValor(None)
            self._inicio = NovoNo
            
    #inseri no fim       
    def InserirNoFim(self, valor):   
        NovoNo = No(valor)  
        if self.listVazia(): 
            self._inicio = self._fim = NovoNo
        else:
            self._fim.setNovValor(NovoNo)
            NovoNo.setAntValor(self._fim)
            NovoNo.setNovValor(None)
            self._fim = NovoNo
            
    #pesquisa o valor
    def pesquisar (self, valor):
        if self.listVazia():
            return None
        NoAtual = self._inicio
        while NoAtual.getValor() != valor:
            NoAtual = NoAtual.getNovValor()
            if  NoAtual == None:
                return "Esse valor não foi encontrado!" 
        return NoAtual.getValor()
    
    #Função Impirmir
    def __str__(self):
        NoAtual = self.inicio  
        if self.listVazia():
            print(" A lista está vazia.") 
        while NoAtual != None:
            print(NoAtual.getValor())
            NoAtual = NoAtual.getNovValor()

    #Função remover 
    def remover(self, valor):
        NoAtual = self._inicio
        if self.listVazia():
            return None
        while NoAtual.getValor() != Valor:
            NoAtual = NoAtual.getNovValor()
            if NoAtual == None:
                return "O valor não está na lista"
        if self._inicio == self._fim:
            self._inicio = self._fim = None
            return None
        elif NoAtual == self._inicio:
            aux = self._inicio.getNovValor()
            self._inicio.setNovValor(None)
            aux.setNovValor(None)
            self._inicio = aux
        elif NoAtual == self._fim:
            aux = self._fim.getAntValor()
            self._fim.setAntValor(None)
            aux.setNovValor(None)
            self._fim = aux
        else:
            aux = NoAtual.getAntValor()
            aux2 = NoAtual.getNovValor()
            aux2.setAntValor(aux)
            aux.setNovValor(aux2)

    #Função esvaiziar lista
    def esvaziarList(self):
                  self._inicio = self._fim = None

class Pilha(ListEncad):
    
    #Função remover no final da pilha
    def desempilhar(self):
        if self.listVazia():
            return
        else:
            UltmValNo = self._fim.getValor()
            if self._inicio is self._fim:
                self._inicio = self.fim = None
            else:
                aux1 = self._fim.getAntValor()
                self._fim.setAntValor(None)
                aux1.setNovValor(None)
                self._fim = aux1
            return UltmValNo
    
class Fila(ListEncad):
    
    #Função remover no inicio da fila
    def removerInicio(self):
        if self.listVazia():
            return" A fila está vazia!"
        else:
            PrimValNo = self._inicio.getValor()
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            else:
                aux2 = self._inicio.getNovValor()
                self._inicio.setNovValor(None)
                aux2.setAntValor(None)
                self._inicio = aux2
            return PrimValNo

######################## Núcleo Programa ##################


#arqEnt = open(sys.argv[1], 'r')
#arqSaida = open(sys.argv[2], 'w')
arqEnt = open('e9.in', 'r')
arqSaida = open('e9.out', 'w')
Refazer = Pilha()
Formato = Pilha()
Textos = Pilha()
Frase = ''

while True:
    temp = 0
    linhas  = (arqEnt.readline()).split()
    #print(linhas)
    tam = len(linhas)
    if tam == 0:
        break
    func = linhas[0]
    if func == "adicionar":
        Refazer.esvaziarList()
        if Textos.listVazia():
            w = linhas[1:]
            #print(w)
            Textos.InserirNoFim(w)
        else:
            w = Textos.desempilhar() + linha[1:]
            Textos.InserirNoFim(w)
            #print(w)
            
    elif linhas[0] == "italico":
        Refazer.esvaziarList()
        if Formato.listVazia():
            Formato.InserirNoFim(" italico")
        else:
            w = Formato.desempilhar() + " italico"
            Formato.InserirNoFim(w)
            
    elif linhas[0] == "negrito":
        Refazer.esvaziarList()
        if Formato.listVazia():
            Formato.InserirNoFim("negrito")
        else:
            w = Formato.desempilhar() + " negrito"
            Formato.InserirNoFim(w)
            
    elif linhas[0] == "apagar":
        pas = int(linhas[1])
        temp= Textos.desempilhar()
        aux2 = temp[ :-pas]
        Textos.InserirNoFim(temp)
        Textos.InserirNoFim(aux2)
        
    elif linhas[0] == "desfazer":
        temp = Textos.desempilhar()
        Refazer.InserirNoFim(temp)
    elif linhas[0] == "refazer":
        if Refazer.listVazia():
            pass
        else:
            elemt = Refazer.desempilhar()
            Textos.InserirNoFim(elemt)

guard = Textos.desempilhar()
for x in range(len(guard)):
    FazerFrase = Frase + "%s" % guard[x]
arqSaida.write(FazerFrase + " | " + str(Formato.desempilhar()))
arqSaida.close()
        
        
         
         
    


