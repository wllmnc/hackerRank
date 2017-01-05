//https://www.hackerrank.com/challenges/balanced-brackets
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
    int t;    
    string openBr = "([{";
    string closeBr= ")]}";
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string s;
        cin >> s;        
        std::stack<char> stackBrakets;
        for(int i=0;i<s.length();i++){
            char ch=s[i];
            int index=openBr.find(ch);
            if(index>=0 and index<4)
            {
                stackBrakets.push(ch);
            }else{
                if (!stackBrakets.empty()){
                    if (stackBrakets.top()==openBr[closeBr.find(ch)])
                        stackBrakets.pop();
                    else
                        break;
                }else{
                        stackBrakets.push(ch);
                        break;
                     }
            }
        }
        if(stackBrakets.empty())
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}
