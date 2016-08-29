l = [1,2,3,5]
m = 5
k =[]
for i in range(m+1):
    k.append(i)
k.remove(k[0])
print(k)

for j in k:
    if j not in l:
        print(j)
