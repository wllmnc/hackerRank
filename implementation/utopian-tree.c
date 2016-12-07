//https://www.hackerrank.com/challenges/utopian-tree
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int t;
    cin >> t;    
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;     
        int H=1;   
        for(int i=0;i<n;i++)
            if(i%2==1)H+=1;
            else H=H*2;
        cout << H << "\n";
    }
    return 0;
}
