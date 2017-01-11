//https://www.hackerrank.com/contests/w28/challenges/the-great-xor
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int comb(int n,int k){    
    if (k > n) return 0;
    if (k * 2 > n) k = n-k;
    if (k == 0) return 1;
    int result = n;
    for( int i = 2; i <= k; ++i )
    {
        result *= (n-i+1);
        result /= i;
    }
    return result;
}


int main(){
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        int x;
        int *point;
        int size=0;
        int itemsCount=0;
        cin >> x;     
        bool first1=false;
        bool first0=false;        
        string binary=bitset< 64 >( x ).to_string();
        for( int i =0; i<binary.length();i++){            
            if (binary[i]=='1' && !first1){
                first1=true;            
            }else{
                if (first1){
                    if (!first0){
                        if (binary[i]=='0'){
                            first0=true;  
                            itemsCount++;  
                            size=binary.length()-i;
                            point = (int *)malloc(size*sizeof(int));
                            point[itemsCount-1]=0;
                        }
                    }else{
                        if(first0){
                            itemsCount++; 
                            point[itemsCount-1]=(binary[i]=='1'?1:0);
                        }
                    }
                }
            }
        }
       int discount=0; 
       for(int i=0;i<size;i++)
       {
           discount+=((point[i]==1)?pow(2,size-1-i):0);
       }
        int npossibles=pow(2,itemsCount)-1;   
        cout << npossibles- discount << endl;       

    }
    return 0;
}
