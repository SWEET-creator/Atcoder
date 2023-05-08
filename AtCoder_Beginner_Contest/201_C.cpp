#include <iostream>
#include <vector>

using namespace std;

int main () {
    string S;
    cin >> S;
    int ans = 0;
    for (int i = 0; i < 9999; i++){
        vector<bool> flag(10);
        int X = i;
        for (int j = 0; j < 4; j++){
            flag[X%10] = true;
            X /= 10;
        }

        bool flag2 = true;
        for (int i = 0; i < 10; i++){
            if(S[i]=='o' && !flag[i]) flag2 = false;
            if(S[i]=='x' && flag[i]) flag2 = false;
        }
        ans += flag2;
    }
    cout << ans << endl;
    
    return 0;
}