//https://www.hackerrank.com/challenges/strange-advertising
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getPeopleWhoRecievedTheAdvice(int n)
{
    return floor (n/2);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin >> n;
    int people=5;
    int result=0;
    for(int i_=0;i_<n;i_++){
        people=getPeopleWhoRecievedTheAdvice(people);
        result+=people;
        people=people*3;
    }
    cout << result; 
    return 0;
    
}
