#include <iostream>

using namespace std;
const int MAXLINE = 101;

int main () {
    int N, temp, d[MAXLINE]={} ,count = 0;
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> temp;
        d[temp]++;
    }

    for (int i = 0; i < MAXLINE; i++){
        if (d[i] != 0)
            count++;
    }
    cout << endl << count << endl;

    return 0;
}