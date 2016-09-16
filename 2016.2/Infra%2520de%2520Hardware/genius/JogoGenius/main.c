#include<stdio.h>
//#include<conio2.h>
//#include<conio.h>
#include<stdlib.h>
#include<time.h>


void azul(){
  textbackground(1);               //FUNÇÃO QUE PINTA DE AZUL
  printxy(32, 2, "                "); //DÊ 16 ESPAÇOS ENTRE AS ASPAS
  printxy(32, 3, "                ");
  printxy(32, 4, "                ");
  printxy(32, 5, "                ");
  printxy(32, 6, "                ");
  printxy(32, 7, "                ");
        }
void amarelo(){
  textbackground(14);              //FUNÇÃO QUE PINTA DE AMARELO
  printxy(16,  8, "                "); //DÊ 16 ESPAÇOS ENTRE AS ASPAS
  printxy(16,  9, "                ");
  printxy(16, 10, "                ");
  printxy(16, 11, "                ");
  printxy(16, 12, "                ");
  printxy(16, 13, "                ");
           }
void verde(){
  textbackground(2);              //FUNÇÃO QUE PINTA DE VERDE
  printxy(48,  8,"                "); //DÊ 16 ESPAÇOS ENTRE AS ASPAS
  printxy(48,  9,"                ");
  printxy(48, 10,"                ");
  printxy(48, 11,"                ");
  printxy(48, 12,"                ");
  printxy(48, 13,"                ");
         }
void vermelho(){
  textbackground(4);                 //FUNÇÃO QUE PINTA DE VERMELHO
  printxy(32, 14, "                "); //DÊ 16 ESPAÇOS ENTRE AS ASPAS
  printxy(32, 15, "                ");
  printxy(32, 16, "                ");
  printxy(32, 17, "                ");
  printxy(32, 18, "                ");
  printxy(32, 19, "                ");
            }

int main()
{
   azul();
   amarelo();
   verde();
   vermelho();
   getchar();
}
