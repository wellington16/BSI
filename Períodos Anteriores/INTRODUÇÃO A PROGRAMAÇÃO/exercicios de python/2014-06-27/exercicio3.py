arq = open ("exercicio3.txt")
x = arq.readlines()
arq.close()
for e in x: 
	e = e.replace('\n','')
	l = e.split('.')
	valido = True
	for ad in l:
		num = int(ad)
		if num>254:
			valido = False
			break
	if valido:
		print("%s corresponde a um endereco valido de IP" % e)
	else:
		print("%s corresponde a um endereco invalido de IP" % e)
arq.close()
