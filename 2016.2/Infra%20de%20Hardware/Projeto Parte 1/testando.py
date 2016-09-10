def ConverteParaBinario(hexa):
    base = 16 ## equals to hexadecimal
    bits = 8

    binario = bin(int(hexa, base))[2:].zfill(bits)
    #print(binario)
    
    for i in range(32 - len(binario)):
        binario = '0' + binario

    listaComSeis= []
    for test in range(6) :
        listaComSeis.append(binario[test])
    stringBinaria = tranformarString(listaComSeis)
    #print(listaComSeis)
    ConvertBinDecimal1(stringBinaria)
    
    #print(binario)    
    return binario

def tipo2(dec):
    decimal = int(dec,2)
    print(decimal)
    return decimal
    

def Tipo1(decimal):
    if decimal == 35:
        print("lw")
    elif decimal == 43:
        print("sw")
    elif decimal == 2:
        print("j")
    elif decimal == 5:
        print("bne")
    elif decimal == 4:
        print("beq")
    elif decimal == 3:
        print("jal")
    if decimal == 0:
        listadoFinal= []
        listax = list(binario)
        #print(listax)
        for x in listax[26::]:
                listadoFinal.append(x)
        stringB = tranformarString(listadoFinal)
        print(listadoFinal)
        a = tipo2(stringB)
        if  a == 8:
            print("jr")
        elif a == 32:
            print("Add")
        elif a == 34:
            print("sub")
        elif a == 42:
            print("slt")
    
def tranformarString(b):
        b = ''.join(b)
        return b
        

def ConvertBinDecimal1(Pbinario):
    decimal = int(Pbinario,2)
    Tipo1(decimal)
    #print(decimal)
    return decimal

arqEntrada = open("entrada.txt", "r")  
while True:
    
    expressao = (arqEntrada.readline()).split()
    #print(expressao)
    if (expressao) == []:
        break
   
    for linha in expressao:
        binario = ConverteParaBinario(linha)
        #print(binario)
                
        

