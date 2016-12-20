//https://www.hackerrank.com/contests/w27/challenges/drawing-book
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
    int n;
    cin >> n;
    int p;
    cin >> p;
    // your code goes here
    int m=0;
    int ajust=0;
    if(n%2==0)
    {
        m=(n)/2;
    }else{
        m=((n+1)/2)-1;
        ajust=1;
    }
    
    int cont=0;
    if(p<=m)//enter from the page 1
    {    
        int q=1;
        while(q<p)
        {
            cont+=1;
            q+=2;
        }
    }else{//enter from the page n
        int q=n-ajust;
        while(q>p)
        {
            cont+=1;            
            q-=2;
        }
    }
    cout << cont;
    return 0;
}
