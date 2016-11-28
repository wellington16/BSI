import math

class Ordena:
    "Classe com os metodos de ordenacao: InsertionSort, MergeSort, HeapSort e QuickSort"
    def __init__(self, lista):
      " Construtor da Classe "
      self.arranjo = lista
      self.tamanhoHeap = len(lista)

    def __str__(self):
      "Override do Estatuto STRING"
      if self.isEmpty():
         return "Arranjo vazio!"
      string = "O Arranjo eh:"
      for i in range(len(self.arranjo)):
         string += str( self.arranjo[i] ) + " "
      return string
   
    def isEmpty(self):
      "O arranjo esta vazio? True or False"
      return self.arranjo is []


    def insertionSort(self):
      "Implemantacao do insertion sort"
      if self.isEmpty():
         return "Arranjon Vazio!"
      for j in range(1,len(self.arranjo)):
         chave = self.arranjo[j]
         i = j-1
         while i>=0 and self.arranjo[i]>chave:
            self.arranjo[i+1] = self.arranjo[i]
            i -= 1
         self.arranjo[i+1] = chave
    
    
    def __merge(self,p,q,r):
        "Funcao auxiliar no merger-sort"
        n1=q-p+1
        n2=r-q
        left = []
        right = []
        for i in range(n1):
            left.append(self.arranjo[p+i])
        for j in range(n2):
            right.append(self.arranjo[q+j+1])
        left.append("Inf")
        right.append("Inf")
        i=0
        j=0
        for k in range(p,r+1):
            if (left[i] != "Inf" and right[j] == "Inf") or left[i] <= right[j]:
                self.arranjo[k] = left[i]
                i=i+1
            else:
                self.arranjo[k] = right[j]
                j=j+1
   
    
    def mergeSort(self,p,r):
        "Algoritmo MergeSort. p eh o indice do primeiro elemento do arranjo e r e o indice do ultimo elemento"
        if p < r:
            q = int(math.floor((p+r)/2))
            self.mergeSort(p,q)
            self.mergeSort(q+1,r)
            self.__merge(p,q,r)

            
    def __parent(self,i):
        "Funcao que retorno o indice do pai do no i do Heap"
        return int(math.floor((i-1)/2))

    def __left(self,i):
        "Funcao que retorna o indice do filho esquerdo do no i do Heap"
        return 2*i+1

    def __right(self,i):
        "Funcao que retorna o indice do filho direito do no i do Heap"
        return 2*i+2

    def __trocaElementoArranjo(self,i,j):
        aux = self.arranjo[i]
        self.arranjo[i]=self.arranjo[j]
        self.arranjo[j] = aux

    
    def Max_Heapify(self,i):
        "Funcao que garante a manutencao do heap maximo"
        l = self.__left(i)
        r = self.__right(i)
        if l <= self.tamanhoHeap-1 and self.arranjo[l] > self.arranjo[i]:
            maior = l
        else:
            maior = i
        if r <= self.tamanhoHeap-1 and self.arranjo[r] > self.arranjo[maior]:
            maior = r
        if maior != i:
            self.__trocaElementoArranjo(i,maior)
            self.Max_Heapify(maior)

    def build_Max_Heap(self):
        "Funcao que constroi um heap maximo"
        for i in range(int(math.floor((len(self.arranjo)-1)/2)),-1,-1):
            self.Max_Heapify(i)

    def  heapSort(self):
        "Algoritmo de ordenamento HeapSort"
        self.build_Max_Heap()
        for i in range(len(self.arranjo)-1,0,-1):
            self.__trocaElementoArranjo(0,i)
            self.tamanhoHeap -= 1
            self.Max_Heapify(0)
