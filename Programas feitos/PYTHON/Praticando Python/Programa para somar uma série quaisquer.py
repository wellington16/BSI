#coding:utf8
#
# Programa para somar uma série quaisquer
#
contador = 0
acumulador = 0
guardaNumdigitados = [] 
quantidade = int(input("Digite a quantidade de números a ser utlizada => " ))
while contador < quantidade:
    numero = int(input("Digite um valor numerico => "))
    contador += 1
    acumulador += numero
    guardaNumdigitados.append(numero)
print ("A soma total do(os) número(os) fornecido(os) = ",acumulador,"e o(os) número(os) digitado(os) = ",guardaNumdigitados)

#fim de programa
