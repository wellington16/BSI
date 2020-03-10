import time
#de forma recursiva
def fib1(n):
    print('1 calculando fibonacci de', n)
    if n <= 1:
        return n
    else:
        print('2 calculando fibonacci de', n)
        return (fib1(n-1) + fib1(n-2))


t0 = time.clock()
a = fib1(30)
t1 = time.clock()
print(t1 - t0)

#de forma iterativa
def fib2(n):
    i = 1
    f = 0
    for k in range(n):
        f += i
        i = f - i
    return f

t0 = time.clock()
b = fib2(30)
t1 = time.clock()
print(t1 - t0)





            
