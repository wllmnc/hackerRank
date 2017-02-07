//https://www.hackerrank.com/challenges/sherlock-and-squares
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >>T;
    while(T--){
        int cont=0;
        double A,B;
        cin >> A >>B;
        long long int p1 = sqrt(A);
        long long int p2 = sqrt(B);
        cout << ((p1*p1 == A)?p2-p1+1:p2-p1) <<endl;
    }
    return 0;
}
