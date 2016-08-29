class cavalo:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mov(self,numero):
        if numero == 1:
            self.x += 1
            self.y += 2
        elif numero == 2:
            self.x += 2
            self.y += 1
        elif numero == 3:
            self.x += 2
            self.y -= 1
        elif numero == 4:
            self.x += 1
            self.y -= 2
        elif numero == 5:
            self.x -= 1
            self.y -= 2
        elif numero == 6:
            self.x -= 2
            self.y -= 1
        elif numero == 7:
            self.x -= 2
            self.y += 1
        elif numero == 8:
            self.x -= 1
            self.y += 2
        
    def onde_estou(self):
        a  = (self.x, self.y)
        print(self.x, self.y)
        return(a)
        

    def buracos(self,a):
        b1 = (1,3)
        b2 = (2,3)
        b3 = (2,5)
        b4 = (5,4)
        if a == b1:
            print("passou => b1 ")
            return(a)

        if a == b2:
            print("passou => b2")
            return(a)
            
        if a == b3:
            print("passou => b3")
            return(a)
     
        if a == b4:
            print("passou => b4 ")
            return(a)
                
l= [6,8,1]
N =l[0]
m = max(l)
if 1<= N <= 100:
    if 1 <= m <= 8:
        a = cavalo(4,3)
        for i in l:
            a.mov(i)
            a.buracos(a.onde_estou())



