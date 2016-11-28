#include <stdio.h>
#include <stdlib.h>

int BuscaBinaria(int x, int n, int v[]){
        int e, d, m;
        e = 0;
        d = n-1;
        while (e <= d){

            m = (e + d) /2;

            if(v[m] == x)
                return m;
            if(v[m] < x)
                e = m + 1;
            else
                d = m - 1;

            }
            return -1;
}
