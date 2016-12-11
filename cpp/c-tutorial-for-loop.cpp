//https://www.hackerrank.com/challenges/c-tutorial-for-loop
#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int main() {
    int i,j;
    char output[]="            ";
    cin >> i >> j;
    for(i;i<=j;i++){
        if (i==1) strcpy(output,"one");
        else if (i==2) strcpy(output,"two"  );
        else if (i==3) strcpy(output,"three");
        else if (i==4) strcpy(output,"four" );
        else if (i==5) strcpy(output,"five" );
        else if (i==6) strcpy(output,"six"  );
        else if (i==7) strcpy(output,"seven");
        else if (i==8) strcpy(output,"eight");
        else if (i==9) strcpy(output,"nine" );
        else if (i>9  && i%2==0) strcpy(output,"even" );
        else strcpy(output,"odd" );
        cout << output << endl;
            }
}
