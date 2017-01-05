//https://www.hackerrank.com/challenges/ctci-making-anagrams
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

int number_needed(string a, string b) {    
    int count=0;  
   for(int i=0;i<a.length();i++)
   {
       int index=b.find(a[i]);
       if(index>=0 && index<b.length())
           b.erase(index,1);
       else
           count++;
   }
   return count+b.length();   
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed(a, b) << endl;
    return 0;
}
