//https://www.hackerrank.com/challenges/append-and-delete
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


int main(){
    string s;
    cin >> s;
    string t;
    cin >> t;
    int k;
    cin >> k;
    int i=0;
    int ans=0;
    int ans_=0;
    int sizes=s.length();
    int sizet=t.length();
    while (k>0){
        int opers=0;
        if(sizes==sizet){
            if(k<(sizes*2)+1){
                while(i<sizet && s[i]==t[i])i++;
                if(i==sizet){
                    opers=2;
                }else{
                    opers=sizet-i;
                    sizes-=opers;
                    }
            }else{
                opers=(k/((sizes*2)+1));
                opers=sizes*2*opers + 1;
                sizes=sizet;                
                s=t;
            }
        }else{
            if(sizes>sizet){
                while(i<sizet && s[i]==t[i])i++;    
                opers=(sizes-i);            
                sizes-=opers;
            }else{
                while(i<sizes && s[i]==t[i])i++;
                opers=(sizet-i);
                sizes+=opers;
            }   
            s=t;
        }
        k-=opers;
    }
    cout <<((k==0  && sizes==sizet)?"Yes":"No");
    return 0;
}
