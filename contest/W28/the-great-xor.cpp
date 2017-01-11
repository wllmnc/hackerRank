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
        long x;
        int *point;
        long size=0;
        long itemsCount=0;
        cin >> x;        
        long count=0;
        bool first1=false;
        bool first0=false;        
        /*for( int i =bitset< 64 >( x ).to_string().length()-1; i>=0; --i)
            if ((x & (1 << i) ) && !first1){
                first1=true;            
        }else{
                if (first1){
                    if (!first0){
                        if (!(x & (1 << i) )){
                            first0=true;  
                            itemsCount++;
                            size=i+1;
                            point = (int *)malloc(size*sizeof(int));
                            point[itemsCount-1]=0;
                        }
                    }else{
                        if(first0){
                            
                            count += (x & (1 << i) ? 0 : 1);
                            itemsCount++; 
                            point[itemsCount-1]=(x & (1 << i) ? 1 : 0);
                        }
                    }
                }
            }
       long discount=0; 
       cout << "size" << size<< endl;
       for(int i=0;i<size;i++)
       {
           cout << ((point[i])?1:0) <<" "<< pow(2,size-1-i)<< " ";
           discount+=((long)(point[i])?pow(2,size-1-i):0);
       }
        cout << "discount " << discount << endl;
        cout << "IC " << itemsCount << endl;
        long npossibles=pow(2,itemsCount)-1;
        cout << "posibles " << npossibles << endl;        
        cout << npossibles- discount << endl;        */
        int count2=0;
        for (int i=0;i<x;i++)
        {
            if(((i)^x)>x){
                count2++;
               // cout << i << endl;
            }
        }
        cout << count2 << endl;
    }
    return 0;
}
