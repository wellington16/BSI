
def validaMenuPrincipal(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():
     print("""

    Bem-vindo ao Sistema de Vendas
------------------------------------
   01 - Cliente
   02 - Funcionário
   03 - Fornecedor
------------------------------------
   0 - Sai
------------------------------------
    """)
     return validaMenuPrincipal("Escolha uma opção: ",0,3)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        import cliente
        menu_cliente()
        break
    elif opcao == 2:
        import funcionario
        menuFuncionario()
        break
    elif opcao == 3:
        import fornecedor
        menuFornecedor()
        break


