cliente = []

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


def novoCliente():
    global cliente
    nome = pede_nome()
    endereco = pede_endereco()
    bairro = pede_bairro()
    cidade = pede_cidade()
    cep = pede_cep()
    estado = pede_estado()
    telefone = pede_telefone()
    celular = pede_celular()
    fax = pede_fax()
    email = pede_email()
    rg = pede_rg()
    cpf = pede_cpf()
    nascimento = pede_nascimento()
    cliente.append([nome,endereco,bairro,cidade,cep,estado,
                    telefone,celular,fax,email,rg,cpf,nascimento])


def mostraDadosCliente(nome,endereco,bairro,cidade,cep,estado,
                       telefone,celular,fax,email,rg,cpf,nascimento):
     print(""""Nome: %s
    Endereço: %s
    Bairro: %s
    Cidade: %s
    Cep: %s
    Estado: %s
    Telefone: %s
    Celular: %s
    Fax: %s
    Email: %s
    RG: %s
    CPF/CNPJ: %s
    Data de Nascimento: %s
    """ % (nome,endereco,bairro,cidade,cep,estado,
           telefone,celular,fax,email,rg,cpf,nascimento))


def pesquisaCliente(nome):
     mnome = nome.lower()
     for p, e in enumerate(cliente):
         if e[0].lower() == mnome:
               return p
     return None

def apagaCliente():
     global cliente
     nome = pede_nome()
     p = pesquisa(nome)
     if p != None:
         del cliente[p]
     else:
         print("Nome não encontrado.")


def alteraCliente():
     p = pesquisa(pede_nome())
     if p != None:
         nome = cliente[p][0]
         endereco = cliente[p][1]
         bairro = cliente[p][2]
         cidade = cliente[p][3]
         cep = cliente[p][4]
         estado = cliente[p][5]
         telefone = cliente[p][6]
         celular = cliente[p][7]
         fax = cliente[p][8]
         email = cliente[p][9]
         rg = cliente[p][10]
         cpf = cliente[p][11]
         nascimento = cliente[p][12]
         print("Encontrado:")
         mostra_dados(nome,endereco,bairro,cidade,cep,estado
                      ,telefone,celular,fax,email,rg,cpf,nascimento)
         nome = pede_nome()
         endereco = pede_endereco()
         bairro = pede_bairro()
         cidade = pede_cidade()
         cep = pede_cep()
         estado = pede_estado()
         telefone = pede_telefone()
         celular = pede_celular()
         fax = pede_fax()
         email = pede_email()
         rg = pede_rg()
         cpf = pede_cpf()
         nascimento = pede_nascimento()
         cliente[p] = [nome,endereco,bairro,cidade,
                       cep,estado,telefone,celular,fax,email,rg,cpf,nascimento]
     else:
         print("Nome não encontrado.")
    
def listaCliente():
     print("\nCliente\n\n------")
     # Usamos a função enumerate para obter a posição na lista cliente
     for posição, e in enumerate(cliente):# Imprimimos a posição, sem saltar linha
         print("N° Cliente Cadastrado: %d " % posição)
         mostra_dados(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11], e[12])
     print("------\n")

def pede_nome_arquivo():
     return(input("Nome do arquivo: "))

def lêCliente():
     global cliente
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r")
     cliente = []
     for l in arquivo.readlines():
         print(l)
     arquivo.close()
     
def gravaCliente():
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w")
     for e in cliente:
         arquivo.write("Nome: %s Endereço: %s Bairro:\
                       %s Cidade:%s Cep: %s  Estado: %s Telefone: %s Celular: %s Fax: %s Email: %s RG: %s CPF/CNPJ: %s Nascimento: %s" % (e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11], e[12]))
     arquivo.close()

def valida_cliente(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menuCliente():
     print("""

    Manutenção de Clientes
-----------------------------------
   01 - Cadastrar novo cliente
   02 - Altera dados do cliente
   03 - Apaga cliente
   04 - Lista de clientes
   05 - Grava arquivo do cliente
   06 - Lê arquivo do cliente
------------------------------------
   0 - voltar
------------------------------------
    """)
     print("Nomes na agenda: %d\n" % len(cliente))
     return valida_cliente("Escolha uma opção: ",0,6)
    
trueFalse = True
while trueFalse:
     opcao = menuCliente()
     if opcao == 0:
        trueFalse = False
        import principal
        menu()
        break
     elif opcao == 1:
          novoCliente()
     elif opcao == 2:
          alteraCliente()
     elif opcao == 3:
          apagaCliente()
     elif opcao == 4:
          listaCliente()
     elif opcao == 5:
          gravaCliente()
     elif opcao == 6:
          lêCliente()
        
