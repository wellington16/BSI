def delete(self,chave, value):
    table = self._table
    i = self.FuncHash(chave,valor)
    table[i] = Hash( self.tamanho, valor,)
    x = table[i].remover(i)
    
