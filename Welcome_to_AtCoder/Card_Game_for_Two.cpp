#include <iostream>
#include <algorithm>
#define MAXLINE 100

using namespace std;

int main () {
    int N;
    cin >> N;
    int a[MAXLINE];
    for (int i=0; i<N; i++){
        cin >> a[i];
    }

    int Alice_score = 0, Bob_score = 0;

    int k=0;
    while (k < N){
        int *max = max_element(a, a+N);
        Alice_score += *max;
        *max = 0;

        max = max_element(a, a+N);
        Bob_score += *max;
        *max = 0;
        k++;
    }
    cout << Alice_score - Bob_score << endl;
}