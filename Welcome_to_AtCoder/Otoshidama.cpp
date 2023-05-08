#include <iostream>
#include <cstdio>

using namespace std;

int main (){
    int N;
    int Y;
    cin >> N >> Y;
    
    for (int a = 0; a < N + 1; a++)
    {
        for (int b = 0; b < N - a + 1; b++)
        {
            int c = N - (a + b);
            int total = 10000 * a + 5000 * b + 1000 * c;
            if (c >= 0 && total == Y){
                printf("%d %d %d\n" ,a ,b ,c);
                return 0;
            }
        }
    }

    cout << "-1 -1 -1" << endl;
    return 0;
}

//local だと segmentation fault するが，AtCoder なら AC　となる