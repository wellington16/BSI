

class Funcionario():
    def __init__(self, nome, nascimento, salario):
        self.nome = nome
        self.nascimento = nascimento
        self.salario = salario
    def informarSalario(self):
        return(self.salario)

    def informarDataNasc(self):
        return(self.nascimento)

    def calcularidade(self):
        from datetime import datetime
        date = date.today()
        return((self.nascimento - (date.year))*(-1))
    
class Gerente(Funcionario):
    def __init__(self,projeto):
        self.projeto = projeto

    def infomarProjeto():
        return(self.projeto)
        
class Programador(Funcionario):
    def __init__(self,linguagem):
        self.linguagem = linguagem

    def infomarLinguagem():
        return(self.linguagem)    
    
        
        
