import sys
#inicio
entrada = open(sys.argv[1], "r")
resultado = open(sys.argv[2], "w")
inteiro = entrada.readlines()
entrada.close()

inteiro=inteiro.split("\n")
FilaP=[]
FilaR=[]
denovo=int(inteiro[0])
vezes=0

#Meio
for i in inteiro[1::]:
        if str(i).isdigit():
            FilaP = []
            FilaR = []
            vezes+= 1
            denovo+= 1
            resultado.write("Caso %d:\n" %(caso))
            
        elif not str(i).isdigit():
            if i[0] and "f":
                FilaR.append(i)
            elif i[0] and "p":
                FilaP.append(i)
                
            elif i[0] and "A":
                if len(FilaR)==0:
                    if len(FilaP)==0:
                        None
                    else:
                        a=FilaP[0]
                        del FilaP[0]     
                else:
                    b=FilaR[0]
                    del FilaR[0]
                    
            elif i[0] and "B":
                if len(FilaP)==0:
                    if len(FilaR)==0:
                        None
                    else:
                        c=FilaR[0]
                        del FilaR[0]
                else:
                    d=FilaP[0]
                    del FilaP[0]
            #FIM        
            elif i[0] and "I":
                if len(FilaR)==0:
                    resultado.write("0")
                else:
                    resultado.write("%s" %(FilaR[0][2::]))
                    
                if len(FilaP)==0:
                    resultado.write("0\n")
                else:
                    resultado.write("%s\n" %(filaP[0][2::]))
