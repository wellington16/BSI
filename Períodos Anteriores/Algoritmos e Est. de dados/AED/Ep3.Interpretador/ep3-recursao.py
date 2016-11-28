# coding: utf-8


op = {
    '+':lambda x, y: x + y,
    '-':lambda x, y: x - y,
    '*':lambda x, y: x * y,
    '/':lambda x, y: x / y,
}


def entrada(url):
    f = open(url).read().splitlines()
    
    #idf = f[1:int(f[0])+2]
    idf = f[1:-2]
    
    idf_new = { i: idf[i] for i in range(len(idf))}
    exp = f[-2]
    n = f[-1]
    
    return idf_new, exp, int(n)




class Pilha(object):
    def __init__(self):
        self._p = []
        
    def add(self, q):
        self._p.append(q)
    
    def pop(self): 
        return self._p.pop()



def not_pos_fixa(exp, exp_origin, op, idf, n, pilha=Pilha()):
    '''
    :exp: expressao pos-fixa ainda com o 'n'
    :exp_origin: expressao original
    :op: dict com as operacoes
    :idf: dict com os identificadores
    :n: valor que substituira n na exp
    :pilha: objeto Pilha
    '''
    #import pdb;pdb.set_trace()
    # tratamento da exp:
    if type(exp) == str and len(exp) != 0 and n != None :
        #import pdb;pdb.set_trace()
        exp = exp.replace('n', str(n)).split()
        #import pdb;pdb.set_trace()

    import pdb;pdb.set_trace()
    
    if len(exp) != 0:
        _elem = exp[0]
    
    # caso base:
    if len(exp) == 0:
        return pilha.pop()
    
    # se operador, desempilha, calcula e empilha o resultado
    elif _elem in op.keys():
        b = pilha.pop()
        a = pilha.pop()
        result = op[_elem](int(b), int(a))
        pilha.add(result)
        return not_pos_fixa(exp[1:], exp_origin, op, idf, n, pilha)
    
    # se número, entram vários outros 'se'...
    else:
        #import pdb;pdb.set_trace()
        x_x = int(_elem)
       
        if x_x < 0:
            _tmp = None
            try:
                
                _tmp = (n + x_x)
               
                _idf = idf[_tmp]
                pilha.add(_idf)
                #import pdb;pdb.set_trace()
                return not_pos_fixa(exp[1:], exp_origin, op, idf, n, pilha)
            except KeyError:
                n_idf = not_pos_fixa(exp_origin, exp_origin, op, idf, _tmp, pilha)
                idf[_tmp] = n_idf
                pilha.add(n_idf)
                #import pdb;pdb.set_trace()
                return not_pos_fixa(exp[1:], exp_origin, op, idf, n, pilha)
                
        pilha.add(x_x)
        return not_pos_fixa(exp[1:], exp_origin, op, idf, n, pilha)


if __name__ == '__main__':

    arq = 'projetos/arq.txt'
    
    idf, exp, n = entrada(arq)
    print('idf - ',idf, '\nexp - ',exp,'\nn - ', n, type(n))
    
    print(not_pos_fixa(exp,exp, op, idf, n))
