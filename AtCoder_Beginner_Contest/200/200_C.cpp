#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N; cin >> N;
    vector<long long> A(200);
    for (int i = 0; i < N; i++){
        long long input;
        cin >> input;
        A[input%200]++;
    }

    long long ans = 0;

    for (int i = 0; i < 200; i++){
        ans += A[i] * (A[i] - 1) / 2;
    }

    cout << ans << endl;
    
    return 0;
}