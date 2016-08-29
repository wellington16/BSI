arq = open ("exercicio2.txt")
x = arq.readlines()
arq.close()
dic = {}
for e in x: 
	e = e.replace('\n','')
	l = e.split(' ')
	dic[l[0]] = l[1]
print (dic)
