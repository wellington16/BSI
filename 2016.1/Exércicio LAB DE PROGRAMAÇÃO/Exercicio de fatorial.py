
#Fatrial com função
def fat(n):
     p=1
     for i in range(n):
         p = p*(i+1)
     return p

x = int(input('Digite um numero: '))

f=fat(x)
print(f)

resultado = 1

lista = range(1,n+1)

for x in lista:

    resultado = x * resultado

print( "%s! = %s" % (n, resultado))


#Com rercividade
def fatRec(n):
    if n == 0:
        return 1
    return n*fatRec(n -1)

def fib(n):
    if n == 0:
        return 0
    if n ==1:
       return 1
    else:
        return fib(n-1) + f(n+2)
    

