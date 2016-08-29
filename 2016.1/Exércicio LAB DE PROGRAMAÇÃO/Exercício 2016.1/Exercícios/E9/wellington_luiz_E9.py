import sys
import os 
# Limpar o video
if sys.platform.startswith("Win32"):
    os. system("cls") 
elif sys.platform.startswith("Linux"):
    os.system("clear") 


#Autor Wellington Luiz

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 9 - Laboratório de Programação
    título: Juvenal não quer lavar louça.
    Executado em python 3.4
'''
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
    
arqEntrada = open(sys.argv[1], "r")
arqSaida = open(sys.argv[2], "w")

#arqEntrada = open("e9.txt", "r")
#arqSaida = open("e9saida.txt", "w")

quantFestas = int(arqEntrada.readline())
for i in range(1, quantFestas+1):
    deckMesa = (arqEntrada.readline()).split()
    cartMesa = Fila()
    cartMesa.InserirNoFim(deckMesa)
    filas = Fila()
    deck = None
    contMenos = 1
    while True:
        deck = (arqEntrada.readline()).split()
        if (deck == ["-1"]):
            break
        filas.InserirNoFim(deck)
        contMenos += 1
    rodadas = 1000
    juvenal = True
    tmp = contMenos
    while rodadas > 0:
        contMenos = tmp
        removeCartInicio = cartMesa.removerInicio()
        pegaInicio = removeCartInicio[0]
        contMais = 1
        while contMenos > 1:
            removidoInicio = filas.removerInicio()
            if len(removidoInicio) == 0:
                juvenal = False
                break
            else:
                teste = removidoInicio[0]
                if pegaInicio == teste:
                    removidoInicio = removidoInicio[1:]
                    filas.InserirNoFim(removidoInicio)
                    contMenos -= 1
                    contMais += 1
                else:
                    del removidoInicio[0]
                    removidoInicio.append(teste)
                    filas.InserirNoFim(removidoInicio)
                    contMenos -= 1
                    contMais += 1
        if juvenal == False:
            break
        del removeCartInicio[0]
        removeCartInicio.append(pegaInicio)
        cartMesa.InserirNoFim(removeCartInicio)
        rodadas -= 1
    if juvenal:
        arqSaida.write("0\n")
    else:
        arqSaida.write(str(contMais)+"\n")
        
arqSaida.close()
arqEntrada.close()
