#include <iostream>
#include <algorithm>

#define MAXLINE 2000

using namespace std;

int main () {
    int N, t[MAXLINE];
    double l[MAXLINE], r[MAXLINE];
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> t[i] >> l[i] >> r[i];
    }

    for (int i = 0; i < N; i++){
        if(t[i] == 2)
            r[i] -= 0.5;
        else if(t[i] == 3)
            l[i] += 0.5;
        else if (t[i] == 4){
            l[i] += 0.5;
            r[i] -= 0.5;
            }
    }

    int ans = 0;
    for (int i = 0; i < N; i++){
        for (int j = i + 1; j < N; j++){
            ans += (max(l[i], l[j]) <= min(r[i], r[j]));
        }

    }
    cout << ans << endl;
      
    return 0;
}