lista=[1,5,4,6,2,8,7,9,3] 
class BBSort:
    def bubble_sort(lista):
        for i in range(len(lista)-1):
            for j in range(len(lista)-1-i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return lista


a = BBSort()
b = BBSort.bubble_sort(lista)

print(b)

class maxHeap:
    def __init__(self,lista,i):
        lista = self.a = lista
        l = i + 1
        r = i + 2
    def tamanho(self):
        if l < lista - 1 and lista[l] > lista[i]:
            maior = l
            print(maior)
        else:
            maior= i
        if r <= len(lista)-1 and lista[r] > lista[i]:
            maior = r
        if maior != i:
            aux= lista[i]
            lista[i] = lista[maior]
            lista[maior] = aux
    def buildMaxHeap(a):
        tam = len(lista)
        for i in range(int(len(lista)/2)):
            print(lista,i)
            maxHeap(lista,i)
        
        
