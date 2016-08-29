import sys
import os # Biblioteca de funções do sistema operacional
# Limpar o video
if sys.platform.startswith("Win32"):
    os. system("cls") # No windows
elif sys.platform.startswith("Linux"):
    os.system("clear") # No linux ou mac os


#Autor Wellington Luiz

'''
    UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO - UFRPE
    Curso: Bacharelado em Sistemas de Informação
    Disciplina: Laboratório de Programação - 2016.1
    Professor: Rodrigo Soares
    Exercício 2 - Laboratório de Programação
    título: Juvenal não tem o que fazer.
    Retornar o valor maximo de recursão da função f(n) até chegar no caso base.
    Executado em python 3.4
'''

try:
    def F(n):
        ''' função do cara que não tem o que fazer durante as férias.
         Quem? Quem? Quem? Juvenal Donato.'''
        global cont
        if (n == 1):
            return 1, cont
        elif (n % 2 == 0):
                cont += 1
                return F(n/2)
        else:
            cont += 1
            return F(3*n+1)
          
    def G(n):
        '''Quantas chamadas recursivas são necessárias para
           que F(n) atinja o caso base.
        '''
        F(n)
        global listadeCont
        listadeCont.append(cont)

    def Max(l):
        menor = l[0]
        maior = l[0]
        i = 0
        while  i < len(l):
            if maior == menor:
                maior
            if l[i] > maior:
                maior = l[i]
            i += 1
        return(maior)


    #leitura do arquivo sem HARDCODE
    arqentrada = open(sys.argv[1], 'r')
    arqsaida = open(sys.argv[2], 'w')

    #leitura do arquivo com hardcode
    #arqentrada = open('entrada.txt',"r")
    #arqsaida = open('saida.txt',"w")

    #Tratamento
    casos = int(arqentrada.readline())

    # "núcleo" do programa
    #restrição de T
    if (casos < 1):
        print("Valor de T  está abaixo do valor permitido que é %d!" % 1)
    elif (casos > 100):
                print("Valor de T  está acima do valor permitido que é %d!" % 100)
    else:
        listaNumCasos = []
        for numCaso in range(1,casos+1):
            listaNumCasos.append(numCaso)
        index = 0
        for linha in arqentrada:
            linhaSep = linha.split()
            n = [int(j) for j in linhaSep]
            A = n[0]
            B = (n[1] + 1)
            #restrição de A e B
            if (1 > A):
                print('Valor de A tem que ser maior que 1.')
                break
            elif (A >= B):
                print('Valor de B tem que ser maior ou igual ao  valor de A.')
                break
            elif(B >= 10**5):
                print('Valor de B tem que ser menor ou igual ao valor de 10 elevado a quinta potência.')
                break
            else:
                sequencia = [x for x in range(A, B)]
                listadeCont = []
                cont = 0
                
            for numSeq in sequencia:
                cont += 1
                G(numSeq)
                cont = 0
            maxdaLista = Max(listadeCont)
            print(listaNumCasos[index], maxdaLista)
            arqsaida.write("Caso %d: %d\n" % (listaNumCasos[index], maxdaLista))
            index += 1

#tratando erro de entrada
except IndexError as e:
    arqsaida.write(str("Reveja o código."))
    arqsaida.write(str(e))

#fechando os arquivos
arqentrada.close()
arqsaida.close()
