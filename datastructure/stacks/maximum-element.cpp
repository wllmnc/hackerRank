//https://www.hackerrank.com/challenges/maximum-element
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N;
    stack<int> items;  
    cin >> N;
    for(int i=0;i<N;i++)
    {
        int cmd;
        cin >> cmd;
        switch(cmd)
        {
            case 1:
                int value;
                cin >>value;
                if (items.empty())
                    items.push(value);                
                else 
                    items.push(max(value, items.top()));                
                break;
            case 2:
                items.pop();
                break;
            case 3:
                cout << items.top()<< endl ;
                break;
        }
    }
    return 0;
}
