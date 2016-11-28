#include<stdio.h>
#include<stdlib.h>


void insecao(int v[], int n){
   ///Recebe um vetor v[0..,n-1] de inteiros
   ///Permite os elementos de v de forma que o resultado
   ///esteja em ordem crescente

    int i, j, x;
    for (j = 1; j < n; ++j){
        x = v[j];
        for (i =  j - 1; i >= 0 && v[i] > x; --i)
            v[i + 1] = v[i];
        v[i + 1] = x;
    }
}

void selecao(int v[], int n) {

   ///Recebe um vetor v[0..,n-1] de inteiros
   ///Permite os elementos de v de forma que o resultado
   ///esteja em ordem crescente

    int i, j, min, x;
    min =  i;
    for (i = 0; i < n - 1; ++i){
        for (j = i + 1; j < n; ++j)
            if(v[j] < v[min])
                min = j;
        x = v[i];
        v[i] = v[min];
        v[min] = x;
    }
}
