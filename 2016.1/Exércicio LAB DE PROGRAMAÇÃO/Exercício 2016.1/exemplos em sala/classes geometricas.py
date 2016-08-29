class ponto :
    def __init__ (self, x, y):
        self._x = x
        self._y = y
    def mover(self, dx, dy):
        self._x += dx
        self._y += dy
        return
    def getX(self):
        return self._x
    def setX(self, novValor):
        self._x = novValor
        return self._x
    
    def getY(self,_y):
        return self._y
    def setY(self, novValor):
        self._y = novValor
        return self._y
    
    def alterarTam(self):
        pass
    def tadentrotafora():
        pass
    def __str__(self):
        return "ponto x = " + str(self._x)+' ' + "y = " + str(self._y)
        
class Reta():
        def __init__(x1,x2):
            self._x1=x1
            self._x2=x2
        def __init__(self, x1, y1, x2, y2):
            self._x1 = ponto(x1,y1)
            self._x2 = ponto(x2,y2)
            
        def mover(self,dx1,dy1,dx2,dy2):
            self._x1.mover(dx1,dy1)
            self._x2.mover(dx1,dy2)
            
        def alterarTam(self, x1,y1,x2,y2):
                    self.mover(x1,y1,x2,y2)
        def __str__(self):
            return 'imprimindo reta x1:'+' ' + str(self._x1) +' ' +'e x2 eh:' + str(self._x2)


    
        
class RetanguloParalelo(Reta):
    def petence(self, x):
            if x.getX() >=  sel._x.getX() and x.getX() <= self_x2.getX():
                if x.getX() >=  sel._x.getX() and x.getX()<= self_x2.getX():
                     return True
                return False
                     
class Triangulo(RetanguloParalelo):
    pass
'''class quadrado(Retanguloparalelo):
    def __init__(lado1, lado2):
        self._l1 = lado1
        self._l2 = lado2
    def calcular(self):
        calc = self._l1 ** 2
'''
x = RetanguloParalelo(1,1,5,5)
x.alterarTam(3,3,3,3)
print(x)
