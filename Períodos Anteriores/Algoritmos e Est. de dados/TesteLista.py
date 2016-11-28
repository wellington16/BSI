#Driver para teste da Classe Lista 
#Algoritmos e Estrutura da Dados
# Prof. Tiago A. E. Ferreira

import sys
from Lista import List

def instructions():
    "Impre as instrucoes para o usuario"
    print "Entre com uma opcao:\n", \
          "  1 para inserir inicio da lista\n",\
          "  2 para inserir no final da lista\n", \
          "  3 para deletar no comeco da lista\n",\
          "  4 para deletar no final da lista\n",\
          "  5 para finalizar programa\n"
    
listObject = List() #instacia uma lista
instructions()
choice = raw_input("? ")

while choice != "5":
    if choice == "1":
        listObject.insertAtBegin(raw_input("Entre com o valor:"))
        print listObject
    elif choice == "2":
        listObject.insertAtEnd(raw_input("Entre com o valor:"))
        print listObject
    elif choice == "3":
        try:
            value = listObject.removeFromBegin()
        except IndexError, message:
            print "Falha na Operacao:", message
        else:
            print value, "removido da lista"
            print listObject
    elif choice == "4":
        try:
            value = listObject.removeFromEnd()
        except IndexError, message:
            print "Falha na Operacao:", message
        else: 
            print value, "removido da lista"
            print listObject
    else:
        print"Opcao invalida:", choice
        instructions()
    choice = raw_input("\n? ")
print"Fim do programa"
