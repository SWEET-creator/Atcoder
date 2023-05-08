#include <iostream>
#define MAXLINE 400000

using namespace std;

int main () {
    int n; cin >> n;
    char s[MAXLINE]; cin >> s;
    int q; cin >> q;
    for (int i = 0; i < q ; i++){
        int t; cin >> t;
        int a; cin >> a;
        int b; cin >> b;
        if (t == 1){
            int temp;
            temp = s[a-1];
            s[a-1] = s[b-1];
            s[b-1] = temp;
        }
        else if (t == 2){
            char temp[MAXLINE];
            for (int j = 0; j < n; j++){
                temp[n + j] = s[j];
                temp[j] = s[n + j];
            }
            for (int j = 0; j < 2*n; j++){
                s[j] = temp[j];
            }
        }
    }
    cout << s << endl;
    return 0;
}