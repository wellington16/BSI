class figura(objeto):
        def __init__(self,centro):
            super(figura, self).__init__()
            self._centro = centro
    
        def desenha(self):
            pass
        def apagar(self):
           self.setPenColor(self.BACKGROUND_COLOR)
           self.desenha()
           self.setPenColor(self.FOREGROUND_COLOR)
        def mexer(self, p):
          self.apaga()
          self._centro = p
          self.desenho()

class Circulo(figura):
     def __init__(self, centro, raio):
            super(Circulo, self).__init__(centro)
            self._raio = raio     

class Retangulo(figura):
       def __init__(self,centro,altura,largura):
            super(Retangulo,self).__init__(centro)
            self._altura = altura
            self._largura = largura

class Quadrado(Retangulo):
     def __init__(self, centro, largura):
        super(Quadrado, self).__init__(centro, largura, largura
