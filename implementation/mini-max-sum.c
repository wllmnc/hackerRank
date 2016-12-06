//https://www.hackerrank.com/challenges/mini-max-sum
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
    long int a;
    long int b;
    long int c;
    long int d;
    long int e;
    cin >> a >> b >> c >> d >> e;
    long int total=a+b+c+d+e;
    long int items[5]={a,b,c,d,e};
    long int min=items[0],max=items[0];
    for(int i=1;i<5;i++){
        if(items[i]>max)max=items[i];
        if(items[i]<min)min=items[i];
    }
    cout << total-max << " " << total-min;    
    return 0;
}
