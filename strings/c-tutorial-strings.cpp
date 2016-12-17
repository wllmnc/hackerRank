//https://www.hackerrank.com/challenges/c-tutorial-strings
#include <iostream>
#include <string>
using namespace std;

int main() {
   // Complete the program
  string a,b;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl << a+b << endl;
    char bk=a[0];
    a[0]=b[0];
    b[0]=bk;
    cout << a << " " << b;
    return 0;
}
