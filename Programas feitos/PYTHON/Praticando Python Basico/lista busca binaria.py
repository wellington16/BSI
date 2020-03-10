lista=[1,2,3,4,5,6,7,9,10,11,12,13,14,17,20,30]
n=int(input("digite um numero:"))
j=0
x=0
center=0
left=0
right=len (lista)
while True:
    center=int((left+right)/2)
    if center==j:
        print ("o numero n esta na lista")
        break
    j=center
    if lista[center]== n:
        print (center)
        break
    elif lista[center]>n:
        right=center
        print("#")
    elif lista[center]<n:
        left=center
        print("*")
