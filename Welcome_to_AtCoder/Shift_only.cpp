#include <iostream>
#define MAXLINE 200

using namespace std;

int main () {
    int N, A[MAXLINE] = {}, flag = 0, count = 0;
    cin >> N;

    for (int i = 0; i<N; i++){
        cin >> A[i];
    }

    while(1){
        for (int i = 0; i<N; i++){
            if (A[i]%2 != 0)
                flag = 1;
            A[i] /= 2;
        }
        if (flag == 1)
            break;
        count++;
    }
    cout << count << endl;
    return 0;
}