#include <iostream>
#define MAXLINE 100100

using namespace std;

int main () {
    int N, t[MAXLINE], x[MAXLINE], y[MAXLINE];
    cin >> N;

    t[0] = 0;
    x[0] = 0;
    y[0] = 0;

    for (int i = 0; i < N; i++){
        cin >> t[i+1] >> x[i+1] >> y[i+1];
    }

    bool can = true;

    for (int i = 0; i < N; i++){
        int dis = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]);
        int dt = t[i + 1] - t[i];
        if (dt - dis >= 0 && (dis%2 == dt%2)){
            can = true;
        } else {
            can = false;
            break;
        }
    }

    if (can) cout << "Yes" << endl;
    else cout << "No" << endl;
    

    return 0;
}