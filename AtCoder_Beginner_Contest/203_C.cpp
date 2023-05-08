#include <iostream>
#include <vector>
#include <algorithm>
#define MAXLINE 200000

using namespace std;

int main () {
    int N;
    long long K;
    cin >> N >> K;
    vector< vector<int> > a(2, vector<int>(MAXLINE));
    long long now = 0;

    for (int i = 0; i < N; i++){
        cin >> a[i][0] >> a[i][1];
    }

    sort(a.begin(),a.end());//,[](const vector<int> &alpha,const vector<int> &beta){return alpha[0] < beta[0];});
    for (int i = 0; i < N; i++){
        cout << a[i][0] << a[i][1] << endl;
    }
/*
    for (int i = 0; i < N; i++) {
        K -= (a[0][i] - now);
        if (K < 0){
            cout << K + a[0][i] << endl;
            cout << a[0][i]  << endl;
            return 0;
        } else {
            K += a[1][i];
        }
        now = a[0][i];
    }

    if(K > 0) {
        cout << now + K << endl;
    }
    */
    return 0;
}