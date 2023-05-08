#include <iostream>

using namespace std;

int main () {
    long long int P, nowmoney = 0;
    long long int A[10];
    int B[10] = {0};
    cin >> P;

    A[0] = 1;
    for (int i=0; i<10; i++) {
        A[i + 1] = (i+2) * A[i];
    }
    
    for(int i = 0; i < 10; i++ ){
        nowmoney = 0;
        for (int j = 0; j < 10; j++){
            nowmoney += A[j] * B[j];
        }

        if (nowmoney == P)
            break;

        B[9 - i] = (P - nowmoney) / A[9 - i];
    }

    int sum = 0;

    for (int i = 0; i < 10; i++){
        sum += B[i];
    }

    cout << sum << endl;

    return 0;
}