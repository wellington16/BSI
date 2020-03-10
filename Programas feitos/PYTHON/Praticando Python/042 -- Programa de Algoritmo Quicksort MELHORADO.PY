def quickSort(a,p,r):
    if p < r:
        q = Partition(a,p,r)
        #print(q)
        quickSort(a,p,q-1)
        quickSort(a,q+1,r)
    return(a)

def Partition(a,p,r):
    x = a[r]
    i = p - 1
    #print(x)
    for j in range(p , r):
        if a[j] <= x:
            #print(a[j])
            i += 1
            a[i],a[j] = a[j],a[i]
            #print(a[i])
    a[i + 1],a[r] = a[r],a[i + 1]
    #print(a[i + 1], a[r])
    return (i + 1)

l = [1,5,9,7,6,3,8,4,2]
print('ANTES')
print(l)

b = quickSort(l,0,len(l)-1)
print('Depois')
print(b)

