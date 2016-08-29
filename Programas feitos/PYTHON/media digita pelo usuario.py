array=[]

for x in range(1,5):
    notas= int(input("digite uma nota %d :" % x))
    array.append(notas)
soma= sum(array)
media= soma /len(array)
print ("nota %d: %6.2f" %(soma,media))

print ("média : %2.2s "%(soma/x))
