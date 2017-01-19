#https://www.hackerrank.com/challenges/maximum-draws
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n=0;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        int pair=0;
        cin >> pair;
        cout << pair + 1<< endl;
    }
    return 0;
}
