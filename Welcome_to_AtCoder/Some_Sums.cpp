#include <iostream>

using namespace std;

int main () {
    int N, A ,B;
    cin >> N >> A >> B;

    int n = 0, sum = 0 ,out = 0;
    while (n <= N){
        sum = (n/10000)%10 + (n/1000)%10 + (n/100)%10 + (n/10)%10 + n%10;
        if (A <= sum && sum <= B)
            out += n;
        n++;
    }
    cout << out << endl;
}