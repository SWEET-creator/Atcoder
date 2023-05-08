#include <iostream>
using namespace std;

int main () {
    int a=0, b=0;
    cin >> a >> b;
    if (a%2 == 0 || b%2 == 0)
        cout << "Even" << endl;
    else
        cout << "Odd" << endl;
}