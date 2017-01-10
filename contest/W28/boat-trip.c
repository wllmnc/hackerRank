//https://www.hackerrank.com/contests/w28/challenges/boat-trip
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    int c; 
    int m; 
    scanf("%d %d %d",&n,&c,&m);    
    int maxPassengers=m*c;
    int *p = malloc(sizeof(int) * n);   
    for(int p_i = 0; p_i < n; p_i++){
       scanf("%d",&p[p_i]);
       if(p[p_i]>maxPassengers){
           printf("No");
           return 0;
       }
    }
    printf("Yes");
    return 0;
}
