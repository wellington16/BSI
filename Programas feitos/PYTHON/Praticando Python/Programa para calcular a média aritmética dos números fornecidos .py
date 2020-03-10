#coding:utf8
#
# Programa para calcular a média aritmética dos números fornecidos 
contador = 0
acumulador = 0
guardaNumdigitados = [] 
quantidade = int(input("Digite a quantidade de números a ser utlizada => " ))
while contador < quantidade:
    numero = int(input("Digite um valor numerico => "))
    contador += 1
    acumulador= (acumulador + numero)/2
    guardaNumdigitados.append(numero)
    print ("A soma total dos números fornecidos é ",acumulador,"e o(os) número(os) digitado(os) = ",guardaNumdigitados)

#fim de programa
