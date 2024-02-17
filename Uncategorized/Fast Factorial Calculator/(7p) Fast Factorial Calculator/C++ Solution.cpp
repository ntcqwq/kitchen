#include <iostream>
using namespace std;
int main() {
    int a;
    cin >> a;
    for(int j = 1; j <= a; ++j) {
        unsigned long long n;
        cin >> n;
        if (n < 35) {
            long long factorial = 1.0;
            for(int i = 1; i <= n; ++i) {
                factorial *= i;
            }
            long long mod = 4294967296;
            cout << (factorial % mod) << endl;
        } else {
            printf("0\n");
        }
    }
    return 0;
}