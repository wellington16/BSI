import math
class max_heap:
    def __init__(self,a):
        self.arranjo = a
        self.tamanhoHeap = len(a)


    def __trocaElementoArranjo(self,i,j):
        aux = self.arranjo[i]
        self.arranjo[i]=self.arranjo[j]
        self.arranjo[j] = aux

    def __str__(self):
      string = "O Arranjo eh:"
      for i in range(len(self.arranjo)):
         string += str( self.arranjo[i] ) + " "
      return string

    def __left(self,i):
        return 2*i+1

    def __right(self,i):
        return 2*i+2

          
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

