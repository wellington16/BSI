pontos=0
questão=1
while questão<=3:
    resposta=input("reposta da questão%d:"% questão)
    if questão==1 and resposta =="b":
        pontos =pontos +1
    if questão==2 and resposta =="a":
        pontos=pontos+1
    if questão==3 and resposta=="d":
        pontos=pontos+1
    questão+=1
print ("O aluno fez %d pontos(s)"% pontos)
