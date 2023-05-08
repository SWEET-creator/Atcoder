#include <iostream>

using namespace std;

int main () {
    int A, B, C ,X;
    cin >> A >> B >> C >> X;

    int nowmoney = 0, count = 0, a = 0, b = 0, c = 0;

    while(a <= A) {
        nowmoney  = a * 500 + b * 100 + c * 50;
        if (nowmoney == X && a <= A && a <=A && b <=B && c <= C){
            count += 1;
        }
        if (b == B && c == C) {
            a += 1;
            b = 0;
            c = 0;
        }
        else if (b != B && c == C) {
            b += 1;
            c = 0;
        } else
            c += 1;
    }
    cout << count << endl;
}