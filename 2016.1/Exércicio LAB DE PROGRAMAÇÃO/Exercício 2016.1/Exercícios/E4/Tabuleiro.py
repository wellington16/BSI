
'''
def tabu(l):
    x = 4
    y = 3  
    for i in (l):
        if i == 0:
            print(x,y, '=>0')
            cont = 1
            l.remove(i)
            break
            
        elif i == 1:
            print(x+1,y+2,'=>1')
            cont+= 1
            l.remove(i)
            break
            
        elif i == 2:
            print(x+2,1+y,'=>2')
            cont += 1
            l.remove(i)
            break
            
        elif i == 3:
            print(x+2,y-1,'=>3')
            cont += 1
            l.remove(i)
            
        elif i == 4:
            print(x+1,y-2,'=>4')
            cont += 1
            l.remove(i)
            break
            
        elif i == 5:
            print(x-1,y-2,'=>5')
            cont += 1
            l.remove(i)
            break
            
        elif i == 6:
            print(x-2,y-1,'=>6')
            cont += 1
            l.remove(i)
            break
        elif i == 7:
            print(x-2,y+1,'=>7 ')
            cont += 1
            l.remove(i)
            break
            
        elif i == 8:
            print(x-1,y+2,'=>8')
            cont += 1
            l.remove(i)
            break

        print(cont+1)
    return(cont)'''

def buracos(a):
    b1 = (1,3)
    b2 = (2,3)
    b3 = (2,5)
    b4 = (5,4)
    
    for i in range(a):
        if a == b1:
            break
        if a == b2:
            break
        if a == b3:
            break
        if a == b4:
            break
                
l = [1,8,5,3,4]
m = max(l)
N =l[0]

if 1<= N <= 100:
    if 1 <= m <= 8:
        global cont
        cont=0
        for x in l:
               #c = tabu(l)
               #print(c)
               for i in l:
                    x = 4
                    y = 3
                    if i == 0:
                        a =(x,y)
                        print(x,y, '=>0')
                        a = buracos(a)
                        cont = 1
                        l.remove(i)
                        
                    elif i == 1:
                        #a = 
                        print(x+1,y+2,'=>1')
                        cont+= 1
                        l.remove(i)
    
                    elif i == 2:
                        print(x+2,1+y,'=>2')
                        cont += 1
                        l.remove(i)
                        
                    elif i == 3:
                        print(x+2,y-1,'=>3')
                        cont += 1
                        l.remove(i)
                        
                    elif i == 4:
                        print(x+1,y-2,'=>4')
                        cont += 1
                        l.remove(i)
                        
                    elif i == 5:
                        print(x-1,y-2,'=>5')
                        cont += 1
                        l.remove(i)
                        
                        
                    elif i == 6:
                        print(x-2,y-1,'=>6')
                        cont += 1
                        l.remove(i)
                        
                        
                    elif i == 7:
                        print(x-2,y+1,'=>7 ')
                        cont += 1
                        l.remove(i)
                       
                        
                    elif i == 8:
                        print(x-1,y+2,'=>8')
                        cont += 1
                        l.remove(i)
            
        print(cont)
               


            
                
                
