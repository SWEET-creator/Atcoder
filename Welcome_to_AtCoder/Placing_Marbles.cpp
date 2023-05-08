#include <iostream>

using namespace std;

int main () {
    int s = 0;
    cin >> s;
    cout << s/100 + (s/10)%10 + s%10 << endl;
}