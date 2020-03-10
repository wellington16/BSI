fibonacci = lambda n,a=1,b=1:[b,0][n>0] or fibonacci(n-1,b,a+b)

for x in range(4):
    a =fibonacci(x)
    print(a)
