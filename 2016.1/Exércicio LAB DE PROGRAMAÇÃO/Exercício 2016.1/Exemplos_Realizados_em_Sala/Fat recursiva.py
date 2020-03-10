
def fat(n):
    if n >  0:
        n = n *fat(n-1)
        return(n)
    else:
        return(1)
    
a = fat(1)
print(a)