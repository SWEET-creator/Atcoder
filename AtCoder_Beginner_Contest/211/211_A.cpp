#include <iostream>
#include <iomanip>

using namespace std;

int main () {
    int A, B; cin >> A >> B;
    cout << fixed << setprecision(7)<< (long double)(A - B) /3  + B<< endl;
    return 0;
}