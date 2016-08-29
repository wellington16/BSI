class aluno:
    def _init_(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


class equipe:
    def _init_ (self,projeto):
        self.projeto= projeto
        self.alunos = []

    def inscricaoaluno(self,a):
        self.alunos.append(a)
        
    def pertence(self,aluno):
        return aluno in self.alunos

class gerenciadorEquipes:
    def _init_ (self):
        listaequipes=[]

    def criarequipe(self,nome,alunos):
        erro=False
        for d in listaequipes:
            for a in alunos:
                
        
        
