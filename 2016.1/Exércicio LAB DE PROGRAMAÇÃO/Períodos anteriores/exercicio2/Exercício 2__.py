class figura():
    pass
class centro(figura):
    def __init__(self,mover):
        self.mover = mover

    def __init__(self,desenhar):
        self.desenhar = desenhar

    def __init__(self,apagar):
        self.apagar = (0,0)

class ponto(self,x,y):
    self.x = x
    self.y = y
    
class segementodereta(centro):
    def __init__(self,y1,y2,ax1,ax2,b):
        self.y1 = y1
        self.ax1 = ax1
        self.b = b
        c = ax1 + b
        print (c)
        d = ax2 + b
        print(d)
        
    
class circulo(centro):
    def __init__(self,raio):
        self.mover = 3
        self.raio = raio

class retangulo(centro,ponto):
    pass

class quadrado(retangulo):
    def __init__(self,):
        pass
