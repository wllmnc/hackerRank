//https://www.hackerrank.com/contests/w26/challenges/game-with-cells
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    int m; 
    scanf("%d %d",&n,&m);
    printf("%d\n",((int)(m/2)+m%2)*(((int)(n/2))+n%2));
    return 0;
}
