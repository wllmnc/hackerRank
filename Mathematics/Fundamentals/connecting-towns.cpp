#https://www.hackerrank.com/challenges/connecting-towns
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    unsigned long long n;
    cin >> n;
    while(n--)
    {
        unsigned long long val=1;
        unsigned long long n2;
        cin >> n2;        
        while(--n2)
        {               
            int val_=1;
            cin >>val_;
            val=(val*val_)%1234567;
        }
        cout << val <<endl;
        
    }
    return 0;
}
