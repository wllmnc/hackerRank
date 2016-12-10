//https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int i;
    char output[]="Greater than 9";
    cin >> i;
    if (i==1) strcpy(output,"one");
    else if (i==2) strcpy(output,"two"  );
    else if (i==3) strcpy(output,"three");
    else if (i==4) strcpy(output,"four" );
    else if (i==5) strcpy(output,"five" );
    else if (i==6) strcpy(output,"six"  );
    else if (i==7) strcpy(output,"seven");
    else if (i==8) strcpy(output,"eight");
    else if (i==9) strcpy(output,"nine" );
    
    cout << output;
   return 0;
}
