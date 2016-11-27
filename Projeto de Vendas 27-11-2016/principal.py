
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
    # Cadastro
       01 - Cliente
       02 - Funcionário
       03 - Fornecedor
------------------------------------
    # Controle de estoque
       04 - Categorias
       05 - Produto
------------------------------------
    # Relatório de Vendas
       06 - Por Cliente
       07 - Por Vendedor
------------------------------------
       08 - Aviso de Estoque Baixo
       09 - Controle de Usuários e Acesso
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


