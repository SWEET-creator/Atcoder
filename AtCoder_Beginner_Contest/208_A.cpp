#include <iostream>

using namespace std;

int main () {
    double A, B ,C;
    cin >> A >> B;

    C = B / A; 

    if (1 <= C && C <=6.0){
        cout << "Yes"<< endl;
    } else {
        cout << "No"<< endl;
    }
    
    return 0;
}