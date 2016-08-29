rota=None
def F(n):
    if n == 1:
        return 1
    elif (n % 2) == 0:
        rota='Passou aqui'
        return F(n/2)
    elif (n % 2) != 0 and (n > 1):
        rota='Aqui tambem'
        return F(3*n+1)

print(F(1))
print(rota)
print(F(2))
print(rota)
print(F(3))
print(rota)
print(F(5))
print(rota)
print(F(8))
print(rota)
print(F(13))
print(rota)
