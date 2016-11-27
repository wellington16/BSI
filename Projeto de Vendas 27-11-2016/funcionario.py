
funcionario = []

def pede_nome():
     return(input("Nome: "))

def pede_endereco():
     return(input("Endereço: "))

def pede_bairro():
     return(input("Bairro: "))

def pede_cidade():
     return(input("Cidade: "))

def pede_cep():
     return(input("CEP: "))

def pede_estado():
     return(input("Estado: "))

def pede_telefone():
     return(input("Telefone: "))

def pede_celular():
     return(input("Celular: "))

def pede_fax():
     return(input("Fax: "))

def pede_email():
     return(input("Email: "))

def pede_rg():
     return(input("RG: "))

def pede_cpf():
     return(input("CPF/CNPJ: "))

def pede_nascimento():
     return(input("Data de nascimento: "))

def pede_contato():
    return(input("Digite o Contato: "))

def pede_sexo():
    return (input("Sexo: "))

def pede_cargo():
    return (input("Cargo: "))

def mostra_dadosFuncionario(nome,cargo,nascimento,sexo,endereco,bairro,cidade,cep,estado,telefone,celular):
     print(""""Nome: %s
    Cargo: %s
    Data de Nascimento: %s
    Sexo: %s
    Endereço: %s
    Bairro: %s
    Cidade: %s
    Cep: %s
    Estado: %s
    Telefone: %s
    Celular: %s
    """ % (nome,cargo,nascimento,sexo,endereco,bairro,cidade,cep,estado,telefone,celular))

def pede_nome_arquivo():
     return(input("Nome do arquivo: "))

def pesquisaFuncionário(nome):
     mnome = nome.lower()
     for p, e in enumerate(funcionario):
         if e[0].lower() == mnome:
               return p
     return None

def novoFuncionario():
     global funcionario
     nome = pede_nome()
     cargo = pede_cargo()
     nascimento = pede_nascimento()
     sexo = pede_sexo()
     endereco = pede_endereco()
     bairro = pede_bairro()
     cidade = pede_cidade()
     cep = pede_cep()
     estado = pede_estado()
     telefone = pede_telefone()
     celular = pede_celular()
     funcionario.append([nome,cargo,nascimento,sexo,endereco,bairro,cidade,cep,estado,telefone,celular])

def apaga_funcionario():
     global funcionario
     nome = pede_nome()
     p = pesquisaFuncionário(nome)
     if p != None:
         del funcionario[p]
     else:
         print("Nome não encontrado.")

def altera_Funcionario():
     p = pesquisaFuncionário(pede_nome())
     if p != None:
         nome = funcionario[p][0]
         cargo = funcionario[p][1]
         nascimento = funcionario[p][2]
         sexo = funcionario[p][3]
         endereco = funcionario[p][4]
         bairro = funcionario[p][5]
         cidade = funcionario[p][6]
         cep = funcionario[p][7]
         estado = funcionario[p][8]
         telefone = funcionario[p][9]
         celular = funcionario[p][10]
         print("Encontrado:")
         mostra_dadosFuncionario(nome,cargo,nascimento,sexo,endereco,bairro,cidade,estado,cep,telefone,celular)
         nome = pede_nome()
         cargo = pede_cargo()
         nascimento = pede_nascimento()
         sexo = pede_sexo()
         endereco = pede_endereco()
         bairro = pede_bairro()
         cidade = pede_cidade()
         estado = pede_estado()
         cep = pede_cep()
         telefone = pede_telefone()
         celular = pede_celular()
         fornecedor[p] = [nome,cargo,nascimento,sexo,endereco,bairro,cidade,estado,cep,telefone,celular]
     else:
         print("Nome não encontrado.")


def listaFuncionario():
     print("\nFuncionario\n\n------")
     # Usamos a função enumerate para obter a posição na lista funcionario
     for posição, e in enumerate(funcionario):# Imprimimos a posição, sem saltar linha
         print("N° Fornecedor Cadastrado: %d " % posição)
         mostra_dadosFuncionario(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11])
     print("------\n")

def lêFuncionario():
     global funcionario
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r")
     funcionario = []
     for l in arquivo.readlines():
         print(l)
     arquivo.close()

def gravaFuncionario():
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w")
     for e in fornecedor:
         arquivo.write("Nome: %s Cargo: %s Nascimento: %s Sexo: %s Endereço: %s Bairro: %s Cidade:%s  Estado: %s Cep: %s  Telefone: %s Celular: %s " % (e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11]))
     arquivo.close()

def validaFuncionario(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menuFuncionario():
     print("""
-----------------------------------
   01 - Cadastrar Funcionário
   02 - Altera dados do Funcionário
   03 - Apaga Funcionário
   04 - Lista de Funcionário
   05 - Grava arquivo do Funcionário
   06 - Lê arquivo do Funcionário
------------------------------------
   0 - voltar
------------------------------------

               """)
     print("\nNomes na agenda: %d\n" % len(funcionario))
     return validaFuncionario("Escolha uma opção: ",0,6)
trueFalse = True
while trueFalse:
     opcao = menuFuncionario()
     if opcao == 0:
          trueFalse = False
          import principal
          menu()
          break
     elif opcao == 1:
         novoFuncionario()
     elif opcao == 2:
         altera_Funcionario()
     elif opcao == 3:
         apaga_funcionario()
     elif opcao == 4:
         listaFuncionario()
     elif opcao == 5:
         gravaFuncionario()
     elif opcao == 6:
         lêFuncionario()















