//https://www.hackerrank.com/challenges/equal-stacks
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
    int n1,n2,n3;
    stack<int> s1,s2,s3;
    cin >> n1 >> n2 >> n3;    
    vector<int> v1(n1), v2(n2), v3(n3);
    for(int h1_i = 0;h1_i < n1;h1_i++)cin >> v1[h1_i];    
    for(int h2_i = 0;h2_i < n2;h2_i++)cin >> v2[h2_i];    
    for(int h3_i = 0;h3_i < n3;h3_i++)cin >> v3[h3_i];        
    s1.push(0);
    s2.push(0);
    s3.push(0);
    for(int h1_i = n1-1;h1_i >=0;h1_i--)s1.push(s1.top()+v1[h1_i]);    
    for(int h2_i = n2-1;h2_i >=0;h2_i--)s2.push(s2.top()+v2[h2_i]);  
    for(int h3_i = n3-1;h3_i >=0;h3_i--)s3.push(s3.top()+v3[h3_i]); 
    
    while(s1.top()!=s2.top() || s1.top()!=s3.top() || s2.top()!=s3.top())
    {
        int max=0;
        int counts[3]={s1.top(),s2.top(),s3.top()};
        int j=0;
        for(int i=0;i<3;i++)
            if(counts[i]>max){
                max=counts[i];
                j=i;
            }
        int temp_val=0;
        switch(j)
        {
            case 0: 
                    s1.pop();
                    break;
            case 1:
                    s2.pop();
                    break;
            case 2:
                    s3.pop();
                    break;
        }
    }
    cout << s1.top() << endl;
    return 0;
    
}
