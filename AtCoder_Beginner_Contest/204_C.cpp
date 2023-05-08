#include <iostream>
#define MAXLINE 2000

using namespace std;

int check (int s, int e, int a[], int b[], int M){
    if(s == e){
        return 1;
    } else {
        for (int i = 0; i < M; i++){
            if (s == a[i] && check(a[i], b[i] ,a ,b, M))
                return 1;
        }
        return 0;
    }
}

int main () {
    int N, M;
    cin >> N >> M;
    int a[MAXLINE], b[MAXLINE];
    
    for (int i = 0; i < M; i++){
        cin >> a[i] >> b[i];
    }

    int count = 0;

    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= N; j++){
            count += check(i, j, a, b, M);
        }
    }

    cout << count << endl;

    return 0;
}