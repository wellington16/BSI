print ("escolha1 opcao:\n1-Coca\n2-fanta")
a=int(input("Digite o valor:"))
if a>50:
    conta50= a/50
    a=a%50
    print("O valor é:",conta50,a)
if a>20:
    conta20=a/20
    b=a%20
    print("O valor é:",conta50,a+b)
if a>5:
    conta5=a/5
    c=a%20
    
    print ("O valor é:",conta5,'valor de c:', a+b+c) 
