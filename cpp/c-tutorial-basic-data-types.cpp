//https://www.hackerrank.com/challenges/c-tutorial-basic-data-types
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int       a;
    long      b; 
    long long c;
    char      d;
    float     e;
    double    f;  
    cin >> a >> b >> c >> d >> e >> f;
    cout << a << endl << b << endl << c << endl << d << endl;
    printf("%.3f\n%lf\n",e,f);
    return 0;
}
