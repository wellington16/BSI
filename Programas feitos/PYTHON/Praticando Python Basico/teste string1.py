a=input("Digite a string 1:")
b=input("Digite a string 2:")
c=input("digite a stirng 3:")
d=("brasil")
print ("Tamanho de",a.upper(),":",len(a), "caracteres")
print ("Tamanho de",b.upper(),":",len(b), "caracteres")
if len(a)==len(b):
    a.replace("wellington","2t")
    print("o tamanho de ",a.upper()[::-1],"é igual ao de ",b)
else:
    a.replace("wellington","2t")
    print("o tamanho de ",a.upper()[::-1],"não é igual ao de ",b)
if a==b:
    a.replace("wellington","2t")
    print("o conteúdo  de ",a.lower()[::-1],"é igual ao de ",b)
else:
    
    print("o conteúdo de ",a.lower()[::-1],"não é igual ao de ",b)
for i in range (len(a)+1):
    print(a[:i])
for i in range (len(a)+1):
        print(a[i:])
else:
        print(a)

   
