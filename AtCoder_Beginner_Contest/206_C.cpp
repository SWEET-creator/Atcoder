#include <iostream>
#include <algorithm>
#include <vector>
#define MAXLINE 310000

using namespace std;

int main () {
    long long int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }

    long long res = (N*(N-1)/2);

    sort(A.begin(), A.end());

    long long cnt = 1;

    for (int i = 0; i < N; i++){
        if (A[i] != A[i+1]){
            res -=((cnt*(cnt-1))/2);
            cnt = 1;
        }
        else{cnt++;}
    }
    
    cout << res << endl;
    
    return 0;
}