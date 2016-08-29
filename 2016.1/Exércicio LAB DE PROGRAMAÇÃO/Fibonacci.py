
#fibonacci
'''import time
import sys
def fibInterativa(n):
    if n <= 2:
        return 1
    else:
        a=1
        b=2
        for i in range(n-2):
            x=a+b
            a=b
            b=x
    return x
def fibRecursiva(n):
    print ()
    if n<=a:
        return n
    else:
        return fibRecursiva(n-1) + fibRecursiva (n-2)

print (fibRecursiva(5))

t0= time.clock()
a=fibRecursiva(int(sys.argv[1]))
t1=time.clock()
print(t1 - t0)
b=fibInterativa(int(sys.argv[1]))
t1=time.clock()
print(t1 -t0)'''

#calcular quantas strings pode ser formadas
def SubString(srt,p):
   if p >= (len(str)-1):
       print (str[p:])
   else:
        for i in range(p,len(str)):
            print (str[p:i+1]+"\n")
            SubString(str,p+1)
            
        
SubString('abacaxi',0)                    
