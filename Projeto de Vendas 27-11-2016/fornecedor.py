fornecedor = []

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


def mostra_dadosFornecedor(nome,cpf,contato,endereco,bairro,cidade,estado,cep,telefone,celular,fax,email):
     print(""""Nome: %s
    CPF/CNPJ: %s
    Contato: %s
    Endereço: %s
    Bairro: %s
    Cidade: %s
    Cep: %s
    Estado: %s
    Telefone: %s
    Celular: %s
    Fax: %s
    Email: %s
    """ % (nome,cpf,contato,endereco,bairro,cidade,estado,cep,telefone,celular,fax,email))

def pede_nome_arquivo():
     return(input("Nome do arquivo: "))

def pesquisaFornecedor(nome):
     mnome = nome.lower()
     for p, e in enumerate(fornecedor):
         if e[0].lower() == mnome:
               return p
     return None
def novoFornecedor():
     global fornecedor
     nome = pede_nome()
     cpf = pede_cpf()
     contato = pede_contato()
     endereco = pede_endereco()
     bairro = pede_bairro()
     cidade = pede_cidade()
     estado = pede_estado()
     cep = pede_cep()
     telefone = pede_telefone()
     celular = pede_celular()
     fax = pede_fax()
     email = pede_email()
     fornecedor.append([nome,cpf,contato,endereco
                        ,bairro,cidade,estado,cep,telefone,celular,fax,email])

def apaga_fornecedor():
     global fornecedor
     nome = pede_nome()
     p = pesquisaFornecedor(nome)
     if p != None:
         del fornecedor[p]
     else:
         print("Nome não encontrado.")

def altera_Fornecedor():
     p = pesquisaFornecedor(pede_nome())
     if p != None:
         nome = fornecedor[p][0]
         cpf = fornecedor[p][1]
         contato = fornecedor[p][2]
         endereco = fornecedor[p][3]
         bairro = fornecedor[p][4]
         cidade = fornecedor[p][5]
         estado = fornecedor[p][6]
         cep = fornecedor[p][7]
         telefone = fornecedor[p][8]
         celular = fornecedor[p][9]
         fax = fornecedor[p][10]
         email = fornecedor[p][11]

         print("Encontrado:")
         mostra_dados(nome,cpf,contato,endereco,bairro,cidade,estado,cep,telefone,celular,fax,email)
         nome = pede_nome()
         cpf = pede_cpf()
         contato = pede_contato()
         endereco = pede_endereco()
         bairro = pede_bairro()
         cidade = pede_cidade()
         estado = pede_estado()
         cep = pede_cep()
         telefone = pede_telefone()
         celular = pede_celular()
         fax = pede_fax()
         email = pede_email()
         fornecedor[p] = [nome,cpf,contato,endereco,bairro,cidade,estado,cep,telefone,celular,fax,email]
     else:
         print("Nome não encontrado.")

def mostra_dadosFornecedor(nome,cpf,contato,endereco,bairro,cidade,estado,cep,telefone,celular,fax,email):
     print(""""Nome: %s
    CPF/CNPJ: %s
    Contato: %s
    Endereço: %s
    Bairro: %s
    Cidade: %s
    Cep: %s
    Estado: %s
    Telefone: %s
    Celular: %s
    Fax: %s
    Email: %s
    """ % (nome,cpf,contato,endereco,bairro,cidade,estado,cep,telefone,celular,fax,email))

def listaFornecedor():
     print("\nFornecedor\n\n------")
     # Usamos a função enumerate para obter a posição na lista fornecedor
     for posição, e in enumerate(fornecedor):# Imprimimos a posição, sem saltar linha
         print("N° Fornecedor Cadastrado: %d " % posição)
         mostra_dadosFornecedor(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11])
     print("------\n")
     
def lêFornecedor():
     global fornecedor
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "r")
     fornecedor = []
     for l in arquivo.readlines():
         print(l)
     arquivo.close()

def gravaFornecedor():
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w")
     for e in fornecedor:
         arquivo.write("Nome: %s Cpf: %s Contato: %s Endereço: %s Bairro: %s Cidade:%s  Estado: %s Cep: %s  Telefone: %s Celular: %s Fax: %s Email: %s " % (e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11]))
     arquivo.close()

def validaFornecedor(pergunta, inicio, fim):
     while True:
         try:
               valor = int(input(pergunta))
               if inicio <= valor <= fim:
                   return(valor)
         except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menuFornecedor():
     print("""
-----------------------------------
-----------------------------------
   01 - Cadastrar Fornecedor
   02 - Altera dados do Fornecedor
   03 - Apaga Fornecedor
   04 - Lista de Fornecedor
   05 - Grava arquivo do Fornecedor
   06 - Lê arquivo do Fornecedor
------------------------------------
   0 - Sai
------------------------------------
 """)
     print("\nNomes na agenda: %d\n" % len(fornecedor))
     return validaFornecedor("Escolha uma opção: ",0,6)
trueFalse = True
while trueFalse:
     opcao = menuFornecedor()
     if opcao == 0:
        trueFalse = False
        import principal
        menu()
        break
     elif opcao == 1:
          novoFornecedor()
     elif opcao == 2:
          altera_Fornecedor()
     elif opcao == 3:
          apaga_fornecedor()
     elif opcao == 4:
          listaFornecedor()
     elif opcao== 5:
          gravaFornecedor()
     elif opcao == 6:
          lêFornecedor()
