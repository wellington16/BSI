"""
Funcionamento:
    empilha os operadores e calcula os valores

primeira parte:
    criacao de funcoes que executem as operacoes e seu acoplamento a um
    dicionario que servira de forma similar a um switch

segunda parte:
    funcao que implementara a notacao polonesa se valendo de recursividade, das
    funcoes da primeira parte deste codigo e do modulo que contem a classe pilha

"""
#################################################################################
#                           criando a classe pilha                              #
#################################################################################
class Pilha(object):

    """ O ultimo a entrar e o primeiro a sair """

    def __init__(self):
        """ apenas inicia os atributos  """
        self.elementos = []

    def __repr__(self):
        return 'elementos {0}'.format(self.elementos)

    def adiciona(self, elemento):
        """adiciona um elemento no 'topo' da pilha

        :elemento: o objeto que será inserido
        :returns: None

        """
        self.elementos.append(elemento)

    def retira(self):
        """retira o elemento mais recente adicionado a pilha

        :returns: elemento do topo da pilha

        """
        return self.elementos.pop()
        
  
#################################################################################
#                               primeira parte                                  #
#################################################################################

oprcs = {'+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '*' : lambda x, y : x * y,
        '/' : lambda x, y : x / y }

#################################################################################
#                               segunda parte                                   #
#################################################################################

def calculadora(pilha_op,pilha_num, expressao, op):
    """TODO: Docstring for calculadora.

    :pilha_op: o objeto que implementa a estrutura 'pilha' para as operacoes
    :pilha_num: o objeto que implementa a estrutura 'pilha' para os numeros
    :expressao: str que contem o calcula a ser realizado em notacao polonesa
    :op: dicionario contendo as operacoes matematicas e funcoes que as
    implementam
    
    :returns: resultado do calculo

    """

    # tratando da expressao
    expr_list = []

    if type(expressao) == str:
        expr_list = expressao.split(' ')
    elif type(expressao) == list:
        expr_list = expressao
    else:
        print('erro quanto ao tipo de dado da expressao!!!')

    # verificando cada elemento da expressao
    
    if len(pilha_num.elementos) == 2 and len(expr_list) > 2:
        a = pilha_num.retira()
        b = pilha_num.retira()
        result = pilha_op.retira()(a, b)
#        import pdb; pdb.set_trace()
        return pilha_op.retira()(result, calculadora(pilha_op,pilha_num,
            expr_list, op))

    elif len(pilha_op.elementos) == 1 and len(pilha_num.elementos) == 2:
        a = pilha_num.retira()
        b = pilha_num.retira()
        result = pilha_op.retira()(a, b)
#        import pdb; pdb.set_trace()
        return result
    
    elif expr_list[0] in op.keys():
        key = expr_list.pop(0)
        pilha_op.adiciona(op[key])
#        import pdb; pdb.set_trace()
        return calculadora(pilha_op,pilha_num, expr_list, op)
    
    elif len(pilha_num.elementos) < 2:
        num = int(expr_list.pop(0))
        pilha_num.adiciona(num)
#        import pdb; pdb.set_trace()
        return calculadora(pilha_op,pilha_num, expr_list, op)
