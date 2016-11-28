# coding: utf-8
#Discentes: Wellington Luiz  e Emanuel Medeiros


# OPERAÇÕES-------------------------------------------------------------------------
operacao = {'+':'+','/':'/','-':'-','*':'*'}

# ARQUIVO-------------------------------------------------------------------------
def entrada(arquivo):
    '''  Recebe um arquivo e Faz a leitura do arquivo
        Devolve os casos bases, a expressão e o n'''
    f = open(arquivo).read().splitlines()
    casosBase = [int(i) for i in f[1:-2]]
    casosBase_new = { i: casosBase[i] for i in range(len(casosBase))}
    expressao = f[-2]
    n = f[-1]
    return casosBase_new, expressao, int(n)


if __name__ == '__main__':
    #validando o arquivo a ser recebido
    arq = 'Lep.in'
    casosBase, expressao, n = entrada(arq)

    
# PILHA---------------------------------------------------------------------------------------------    

class Node:
    """ Classe que define um nodo simples de uma Estrutura de dados: (info, NextNodo)"""

    def __init__(self, data):
        """Construtor do Nodo"""
        self.data = data
        self.nextNode = None
    
    def getData(self):
        "Retorna o Dado armazenado no nodo"
        return self.data
    
    def setData(self,data):
        "Atribui valor ao Dado do nodo"
        self.data = data
    
    def getNextNode(self):
        "Retorna a referencia do proximo nodo"
        return self.nextNode
        
    def setNextNode(self,newNode):
        "Ajusta a referencia do proximo nodo"
        self.nextNode = newNode;
        
    
class Pilha:
    """Classe Pilha com Lista Encadeada:
            Esta classe tem dois ponteiros:
                firstNode: aponta para o primeiro nodo da lista
                lastNode: aponta para o ultimo nodo da lista
            Ao iniciar a lista ambos os ponteiros apontam para NULO"""
    
    def __init__(self):
        "Construtor da Lista  que aponta para o final e inicio"
        self.firstNode = None
        self.lastNode = None
    
    def __str__(self):
        "Override do Estatuto STRING"
        if self.isEmpty():
            return "A pilha esta vazia!"
        correntNode = self.firstNode
        string = "Situação da pilha\n O estado da pilha eh: "
        #print ('\n')
        while correntNode is not None:
            string += str( correntNode.getData() ) + " "
            correntNode = correntNode.getNextNode()    
        return string
    
        
    def add(self, value):
        "Insere elemento o final da PILHA"
       
        newNode = Node(value)  #instancia de um novo nodo
        
        if self.isEmpty():  #Se a PILHA esta vazia
            self.firstNode = self.lastNode = newNode
        else:
            self.lastNode.setNextNode(newNode)
            self.lastNode = newNode
        
    def pop(self):
        "Remove o ultimo elemento da pilha"
        if self.isEmpty():
            raise IndexError( "Esta remoçao não é permitida, pois a Pilha está vazia!")
        lastNodeValue = self.lastNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            currentNode = self.firstNode
            while currentNode.getNextNode() is not self.lastNode:
                currentNode = currentNode.getNextNode()
            currentNode.setNextNode(None)
            self.lastNode = currentNode
        return lastNodeValue
    
    def isEmpty(self):
        "A pilha esta vazia? True or False"
        return self.firstNode is None    
    
   

# CÁCULO -------------------------------------------------------------------------------------------

def calculadora(oper,a,b):
    ''' Recebe a operação  os operandos
        Devolve o resultado de acordo com a operação'''
    if oper == '+':
          result = int(a) + int(b)
          return(result)
    elif oper == '*':
        result = int(a) * int(b)
        return (result)
    elif oper == '-':
        result = int(a) - int(b)
        return (result)
    
    elif oper == '/':
      result = int(a) / int(b)
      return (result)
    

# FUNÇÃO PRINCIPAL----------------------------------------------------------------------------------

def notacaoPosFixa(expressao, exp_origin, operacao, casosBase, n, estan_pilha = Pilha()):
    '''
      Recebe a "expressao" pos-fixa em forma de lista
      Recebe a "expressao_original(exp_origin)" pos-fixa 
      Recebe as operações(operacao) que estão no dicionário
      Recebe os "casos bases(casosBase)"  e calcula quando encontra com os operadores 
      Recebe 'n' e retorna n na exp
      Cria uma estancia pilha(estan_pilha) na classe Pilha

      Retorna o resultado final com todos os prints
      Chama a função calcula    '''
    
    # tratamento da exp:
    if type(expressao) == str and len(expressao) != 0 and n != None :
        expressao = expressao.replace('n', str(n)).split()
        
    
    if len(expressao) != 0:
        operador = expressao[0]
        
    # caso base:
    if len(expressao) == 0:
        return estan_pilha.pop()
    
    
    elif operador in operacao.keys():
        # Se o item for um operador, desempilhe, calcule e empilhe novamente o resultado
        b = estan_pilha.pop()
        a = estan_pilha.pop()
        result = calculadora((operacao[operador]),int(b), int(a))
        estan_pilha.add(result)
        # recursividade
        return notacaoPosFixa(expressao[1:], exp_origin, operacao, casosBase, n, estan_pilha)
        
            
    # se número, entram vários outros 'se'...
    else:
        
        mumero = int(operador)       
        if mumero < 0:
            auxiliar = 0
        # recursividade -----------------------------------------------
            try:
                auxiliar = (n + mumero)
                _casosBases = casosBase[auxiliar]
                estan_pilha.add(_casosBases)
                
                print(estan_pilha)#Imprimindo a pilha
                return notacaoPosFixa(expressao[1:], exp_origin, operacao, casosBase, n, estan_pilha)
        
        # recursividade -----------------------------------------------   
            except KeyError:
                novosCasosBases = notacaoPosFixa(exp_origin, exp_origin, operacao, casosBase, auxiliar, estan_pilha)
                casosBase[auxiliar] = novosCasosBases
                estan_pilha.add(novosCasosBases)
                print(estan_pilha) #Imprimindo a pilha
                return notacaoPosFixa(expressao[1:], exp_origin, operacao, casosBase, n, estan_pilha)
        
        estan_pilha.add(mumero)
        return notacaoPosFixa(expressao[1:], exp_origin, operacao, casosBase, n)
    

# ESTOURO DE PILHA-----------------------------------------------------------------------------------------   

def parar(x):
    num_maximo = 1000000000
    for i in range(1): 
        if int(x) == (num_maximo):
            print('ESTOURO DE PILHA')
        break
    return
parar(notacaoPosFixa(expressao,expressao, operacao, casosBase, n))

    
# IMPRESSÃO DOS CASOS BASES, DA EXPRESSÃO E DO RESULTADO FINAL----------------------------------------------------

print("\nResultado FINAL = ", notacaoPosFixa(expressao,expressao, operacao, casosBase, n))
print('CasosBases = ',casosBase, '\nexpressão = ', expressao,'\nn =', n)
