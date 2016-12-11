//https://www.hackerrank.com/challenges/c-tutorial-pointer
#include <stdio.h>
#include <cmath> 
void update(int *a,int *b) {
    int newa=(*a+*b);
    int newb=(std::abs(*a-*b));
    *a=newa;
    *b=newb;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
