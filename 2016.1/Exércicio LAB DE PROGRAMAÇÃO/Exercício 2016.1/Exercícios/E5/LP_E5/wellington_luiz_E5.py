import sys

#Autor : Wellington Luiz 

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 3 - Laboratório de Programação
    titulo: Quebrando a banca.
    Executado em python 3.4 
'''

try:
      
        #leitura do arquivo sem HARDCODE
        arqentrada = open(sys.argv[1], 'r')
        arqsaida = open(sys.argv[2], 'w')

        #leitura do arquivo com HARDCODE
        #arqentrada = open("entrada.txt", 'r')
        #arqsaida= open("E5.txt","w")

        def menor(lista):
                ''' Verifica o menor numero da lista
                    e  o devolve para o programa
                '''
                menor = lista[0]
                maior = lista[0]
                i = 0
                while  i < len(lista):
                    if maior == menor:
                        menor
                    if lista[i] < menor:
                        menor = lista[i]
                    i += 1
                return(menor)
            

        def remover(NumRem):
                ''' Remove o menor da lista e escreve no arquivo
                    os numero maiores: dezenas, centenas...
                '''
                i = 0
                while i < NumRem:
                        j = menor(lista)
                        lista.remove(j)
                        i += 1
                for i in range(len(lista)):
                        
                        listas1.append((lista[i]))
                        arqsaida.write(str(lista[i]))
                        print(listas1)
                arqsaida.write('\n')
                return(lista)

        #tratamento da entrada
        linhas = arqentrada.read().splitlines()
        
        listas1 = []

        #programa principal(núcleo)
        for i in range(len(linhas)-1):
                print(linhas)
                if linhas == []:
                        break
                praremover = (int(linhas[0][2]))
                print(praremover)
                lista = [int(i)for i in linhas[1]]
                remover(praremover)
                removendo1 = linhas.pop(0)
                removendo2 = linhas.pop(0)
#tratando erro de entrada
except IndexError as e:
     arqsaida.write("Reveja o código")
     
#fechando o arquivo
arqentrada.close()
arqsaida.close()

#fim do programa  


    
