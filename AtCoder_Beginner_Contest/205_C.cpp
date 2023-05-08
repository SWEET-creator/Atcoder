#include <iostream>

using namespace std;

void Judgment (long long int X) {
    if (X > 0)
        cout << ">" << endl;
    else if (X < 0)
        cout << "<" << endl;
    else
        cout << "=" << endl;
    
    return;
}

int main () {
    long long int A, B, C;
    cin >> A >> B >> C;

    // 0 partern
    if (A == 0 && B != 0)
        cout << "<" << endl;
    else  if (A != 0 && B == 0) 
        cout << ">" << endl;
    else if (A == 0 && B == 0)
        cout << "=" << endl;

    // ++
    if (A > 0 && B > 0)
        Judgment(((A) - (B)) * C);

    // +-
    if ((A > 0 && B < 0) || (A < 0 && B > 0)){
        if (C%2 == 0){
            Judgment(((abs(A)) - (abs(B))) * C);
        }
        else
            if (A < B) {
                cout << "<" << endl;
            } else {
                cout << ">" << endl;
            }
    }

    //--
    if (A < 0 && B < 0){
        if (C%2 == 0){
            Judgment((A - B) * C);
        }
        else
            Judgment(((abs(A)) - (abs(B))) * C);
    }
    return 0;
}