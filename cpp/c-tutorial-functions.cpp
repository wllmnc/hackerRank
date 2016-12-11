//https://www.hackerrank.com/challenges/c-tutorial-functions
#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d);


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(int a, int b, int c, int d)
{
    int array4[4]={a,b,c,d};
    int *iterator=array4;
    int max=*iterator;
    for(int i=1;i<sizeof(array4)/sizeof(int);i++)if (max < *(iterator+i))max =*(iterator+i);
    return max;
}
