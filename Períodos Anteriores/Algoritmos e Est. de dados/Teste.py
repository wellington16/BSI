from Ordena import Ordena

l=[5,3,2,7,1,9,8]
x=Ordena(l)
y=Ordena(l)
z=Ordena(l)

print "x"
print x
print "y"
print y
print "z"
print z

x.insertionSort()
y.mergeSort(0,len(l)-1)
z.heapSort()

print("\n ----- Ordenando ---- \n")

print "x"
print x
print "y"
print y
print "z"
print z
