//https://www.hackerrank.com/challenges/bon-appetit
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,k,bc;
    cin >> n >> k;    
    int sum=0;
    for(int i=0;i<n;i++){
        int val=0;
        cin >> val;
        if (i!=k) sum+=val;
    }
    int payperperson=sum/2;
    cin >> bc;
    if(bc>payperperson)cout << bc-payperperson;
    else cout << "Bon Appetit";    
    return 0;
}
