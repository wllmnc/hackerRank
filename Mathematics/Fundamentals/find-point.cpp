//https://www.hackerrank.com/challenges/find-point
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    for (int i=0;i<n;i++)
    {
        int px,py,qx,qy;
        cin >>px >> py >> qx >> qy;
        cout << qx + (qx-px) << " " << qy + (qy-py) << endl;        
    }
    return 0;
}
