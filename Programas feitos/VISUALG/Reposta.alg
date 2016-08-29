algoritmo "JOGO  de encontra a resposta correta"
// Função :
// Autor :
// Data : 11/04/2014
// Seção de Declarações
var
Action1,Action2:inteiro
inicio
// Seção de Comandos
escreval ("Qual a resposta esta correta?")
escreval ("Resposta UM!")
escreval ("Resposta DOIS")
escreval ("Resposta TRES")
leia (Action1)
escolha (Action1)
caso 1
   escreval ("Você acertou!")
   escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
caso 2
     escreval ("Você errou!")
     escreva ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
caso 3
     escreval ("Você errou!")
     escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
outrocaso
         escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
fimescolha
//fim da primeira pergunta
limpatela
escreval ("A resposta correta da questao 1 era : Número 1")
escreval("Parabens por você ter acertado a primeira pergunta!")
escreval("A segunda pergunta é: Qual a reposta correta?")
escreval ("Resposta UM!")
escreval ("Resposta DOIS")
escreval ("Resposta TRES")
leia (Action2)
se Action2=3 entao
escreval ("Você acertou!")
escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
se (Action2=2) ou (Action2=1)entao
escreval("Você errou!")
escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
fimse
fimse
caso 1
     escreval ("Você errou!")
escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimescolha
fimalgoritmo
caso 2
     escreval ("Você errou!")
     escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
     fimescolha
fimalgoritmo
caso 3
     escreval ("Você acertou!")
outrocaso
         escreval ("precione ESC+F9 para reiniciar ou apenas ESC para sair.")
fimalgoritmo
