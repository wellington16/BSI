algoritmo "semnome"
// Função :
// Autor :
// Data : 14/04/2014
// Seção de Declarações 
var
  i,numerador:inteiro
  soma:real
inicio
// Seção de Comandos 
soma:=0
numerador:= 1000
para i de 50 ate 1 faca
     se ((1% 2)=0) entao
     soma:= soma +numerador/i
     senao
     soma := soma+numerador/i
     fimse
     numerador:=numerador-3
     escreval ("o valor dos primeiros 50 termos d a série é: ",soma)

fimalgoritmo
