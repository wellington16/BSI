
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
        return NoAtual.getValor
    
    #Função Impirmir
    def __str__(self):
        NoAtual = self._inicio  
        if self.listVazia():
            return(" Este valor não existe.")
        texto = ''
        while NoAtual != None:
            texto = str(NoAtual.getValor())+ " "
            print(NoAtual.getValor())
            NoAtual = NoAtual.getNovValor()
        return texto

    #Função remover 
    def remover(self, valor):
        NoAtual = self._inicio
        if self.listVazia():
            return None
        while NoAtual.getValor() != valor:
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


class Item():
    def __init__(self, chave, valor):
        self._chave = chave
        self._valor = valor

    def __str__(self):
        chav = self.getChave()
        valor1 = self.getValor()
        chav = str(chav)
        valor1 = str(valor1)
        elemt = "Chave = "+ chav +". O valor = "+ valor1+ "\n"
        return elemt
    
    def getChave(self):
        return self._chave
    def setChave(self, chave):
        self._chave = chave
    def getValor(self):
        return self._valor
    def setValor(self, valor):
        self._valor = valor

class Hash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self._table = [None] * tamanho

    def FuncHash(self, chave):
        return chave % self.tamanho

    def pesquisarItem(self, chave):
        x = self.FuncHash(chave)
        l = self._table[x]
        if l == None:
            return None
        h = l._inicio
        
        while h  != None:
            if h.getValor().getValor() == chave:
                return h.getValor.getValor()
            h = h.getNovValor()
        return None
    
    def inserir(self, chave, valor):
        valorHash = self.FuncHash(chave)
        #print(valorHash)
        item = Item(chave,valor)

        if (self._table[valorHash] == None):
            listx = ListEncad()
            listx.InserirNoInicio(item)
            self._table[valorHash]= listx
        else:
            self._table[valorHash].InserirNoInicio(item)
            

    def delete(self, chave):
        v = self.listar(chave)
        if v != "Nao Existe":
            g = v._inicio
            while (g != None):
                if g.getValor().getChave() == chave: 
                    if v._inicio != v._fim:
                        if g == v._inicio:
                            p = v._inicio.getNovValor() 
                            p.setAntValor(None)
                            v._inicio = p
                        elif g == v._fim:
                            a = v._fim.getAntValor()
                            a.setNovValor(None)
                            v._fim = a
                        else:
                            a = g.getAntValor()
                            p = g.getNovValor()
                            p.setAntValor(a)
                            a.setNovValor(p)
                    else:
                        v._inicio = None
                        v._fim = None
                g = g.getNovValor()
        else:
            return ("Não existe esse elemento na tabela")

    def listar(self, chave):
        valorHash = self.FuncHash(chave)
        if self._table[valorHash] != None:
            return self._table[valorHash]
        else:
            return 0
        
    def __str__(self):
        textox = ''
        for x in self._table:
            if x == None:
                pass
            else:
                textox += str(x.__str__() + "\n")
                
        return textox
    
novatabelinha = Hash(5)
novatabelinha.inserir(1, 45)
novatabelinha.inserir(3, 67)
novatabelinha.inserir(5, 5)
novatabelinha.inserir(2, 44)

#print(novatabelinha)
novatabelinha.listar(5)
#novatabelinha.delete(1)
novatabelinha.pesquisarItem(2)
print(novatabelinha)




        
         
         
    


