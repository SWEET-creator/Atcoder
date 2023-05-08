#include <iostream>
#include <vector>

using namespace std;

int binary_search(int key, vector<int> X) {
    int left = 0, right = (int)X.size() - 1; // 配列 a の左端と右端
    while (right >= left) {
        int mid = left + (right - left) / 2; // 区間の真ん中
        if (X[mid] == key) return mid;
        else if (X[mid] > key) right = mid - 1;
        else if (X[mid] < key) left = mid + 1;
    }
    return -1;
}

vector<int> input_vector (vector<int> X ,int N){
    for (int i = 0; i < N; i++){
        int input;
        cin >> input;
        X.push_back(input);
    }
    return X;
}


int main () {
    int N;
    cin >> N;

    vector<int> X, A, B, C;
    A = input_vector(X, N);
    B = input_vector(X, N);
    C = input_vector(X, N);

    vector<int> count(N);
    for (int j = 0; j < N; ++j) {
        count[B[C[j]]] += 1;
    }

    int answer = 0;
    for (int i = 0; i < N; i++){
        int b = binary_search(A[i], B);
        if(b >= 0) answer += count[b];
    }

    cout << answer << endl;
    
    
    return 0;
}