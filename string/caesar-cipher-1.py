#https://www.hackerrank.com/challenges/caesar-cipher-1
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int k;
    cin >> k;
    for(int i=0;i<n;i++){
        int delay=0;
        int ival=int(s[i]);
        if ((ival>64 and ival<91) or (ival>96 and ival<123)){
            delay=k;
            int mod=(ival<91)?65:97;            
            ival=(ival+(delay%26))%mod;
            ival=ival%26+mod;            
            }
        cout << char(ival);
    }
    return 0;
}
