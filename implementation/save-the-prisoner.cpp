//https://www.hackerrank.com/challenges/save-the-prisoner
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    unsigned long N,S,M;
    cin >> T;
    for( int i=0;i<T;i++){
        cin >> N >> M >> S;
        cout << ((N+(S+M-1)%N)-1)%N +1 << endl;
    }
    return 0;
}
