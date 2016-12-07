//https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getReverse(int x)
{
    int result=0;
    int i=0;
    while(x>0){
        result=(result*(10))+x%10;
        x=(x-(x%10))/10;
    }
    return result;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int i,j,k;
    cin >> i;
    cin >> j;
    cin >> k;
    int nbdays=0;
    for(i;i<=j;i++)        
        if(abs(i-getReverse(i))%k==0)nbdays++;
    cout << nbdays << "\n";
    return 0;
}
