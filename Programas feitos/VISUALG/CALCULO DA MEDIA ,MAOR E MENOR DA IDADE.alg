algoritmo "semnome"
// Função :
// Autor :
// Data : 14/04/2014
// Seção de Declarações 
var
idade,maior,menor,soma,quantidade:inteiro
inicio
// Seção de Comandos
escreval("calculo da media ,maior e menor idade de um conjunto.")
escreval("Digite as idades (uma por uma) e para finalizar digite 0: ")
quantidade:=0
soma:= 0
maior:=0
menor:=9999
repita
      leia (idade)
      se idade > 0 entao
      quantidade := quantidade +1
               se idade >maior entao
               maior:= idade
               fimse
               se idade < menor entao
               menor := idade
               fimse
      senao
      se idade<0 entao
      escreval ("Idade negativa não é valida e será desconsiderada")
      fimse
   fimse
ate idade =0
se quantidade < entao
escreval("A maior idade é: ",maior)
escreval("A menor idade é: ",menor)
escreval ("A media das idades é: ",soma/quantidade)
senao
escreval ("Nenhuma idade maior que zero foi digitada, finalizando o programa.")
fimse
fimalgoritmo
