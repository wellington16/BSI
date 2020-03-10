print ('Do you like video games? yep?! Then you can to play with us')
print ('Para iniciar digite o seguinte codigo "seu nome = Inicio()"')
def Inicio( ):
    print ('-'*50,' Have Fun ','-'*50)
        
#Perguntando se o usuario deseja, ou nao, configurar o jogo.
    n=input("Deseja configurar o jogo ou quer jogar com nossas regras? ('S' ou 'N') ")
    n.upper()
    if n=='S' or n=='s':
        #Colocamos aqui o codigo de abrir o arquivo (config.txt)
        Config= open("config.txt",)
        Config.read(11)
        dimensao = Config
        quantidade_D_Navios = Config.read(20)
        erros = Config.read(20)
        close()
        print (dimensao) 

    elif n=='N' or n=='n':
        #Colocamos aqui o codigo de abrir o arquivo (grid.txt)
        Grid= open("grid.txt",r)
        erros = Grid.read(18)+ Grid.read(19)
        grid.readline() 
        close()
        
        print ('abrindo arquivo "grid.txt" ')
