#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main () {
    int N; cin >> N;
    vector<int> C(N);
    for (int i = 0; i < N; i++) cin >> C[i];
    sort(C.begin(),C.end());
    long long ans = 1;
    for (int i = 0; i < N; i++){ ans = ans * max(0, C[i] - i) % MOD;
    
    cout << ans << endl;
    
    return 0;
}