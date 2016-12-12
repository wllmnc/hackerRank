//https://www.hackerrank.com/challenges/arrays-introduction
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N=0;
    cin >> N;
    int aInt[N];
    for(int i=0;i<N;i++)cin >> aInt[i];
    for(int i=N;i>0;i--)cout << aInt[i-1] << " ";
    return 0;
}
