
algoritmo "Media"
// Fun��o :
// Autor :
// Data : 08/04/2014
// Se��o de Declara��es
var
    nota1,nota2,media:real
inicio
escreval ("Digite nota1: ")
leia (nota1)
escreval ("Digite nota2: ")
leia (nota2)
media :=(nota1+nota2)/2
se media=10 entao
   escreval ("pontua��o maxima")
senao
   se media >=7 entao
     escreval ("aprovado por media")
    senao
       se (media >=5) e ( media <7) entao
        escreval (" Final")
        senao
          escreval("reprovado")
        fimse
     fimse
fimse
fimalgoritmo
