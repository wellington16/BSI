a=['..#.#','#...','...#.','##...','...#.']


listaM = []
listad = []
def antVert(j,i):
    a= j - i
    #print(a)
    
def buscL(ab,listaM):
        for h in range(len(listaM)):
            for i in listaM:
                #print('é h:',h)
                if i[0] == ab :
                    continue   
                    #print('passei aqui',i)
            #print('é listaMh:',listaM[h])
        listaM[h].extend(ab)
    #break
            
                

def ant(a,b):
    if a =='#':
        #print('é sequilha')
        buscL(a,b)
        
    else:
        return False
        #print('não é serquilha')
    

for i in a:
    for j in range(len(i)):
        if i[j]== '#':
            #print('aqui: ',j)
            
            listad.append(i[j]) 
            ab =i[j-1]
            #print("é ab:"  ,ab)
            if j == 0:
                antVert(j,len(i))
            else:
                ant(ab, listaM)
        listaM.append(listad)
print(listaM)
            
    
            
        
               
