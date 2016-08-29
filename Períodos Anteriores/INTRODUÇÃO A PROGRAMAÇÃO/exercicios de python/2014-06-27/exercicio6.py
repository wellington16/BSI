arquivo = raw_input('Digite o nome do arquivo: ')
arq = open (arquivo)
x = arq.readlines()
arq.seek(0)
texto = arq.read()
arq.close()
print("Quantidade de linhas do arquivo: %d" % len(x))
qtde = 0
pos = texto.find('print')
while pos!=-1:
	qtde+=1
	pos = texto.find('print',(pos+1))
print("Quantidade de vezes que o comando print foi usado no arquivo: %d" % qtde)