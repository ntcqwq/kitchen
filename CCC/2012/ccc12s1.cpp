#include <bits/stdc++.h>
using namespace std;
#define endl "\n";
#define fio cin.tie(nullptr) -> sync_with_stdio(false); 
typedef long long ll;
const int inf = INT_MAX;

int nCk(int n, int k = 3) {
    double ans = 1;
    for(int i = 1; i <= k; i++){
        ans = ans * (n-k+i)/i;
    }
    return (int)ans;
}

int main() {
    fio;
    int J;
    cin >> J;
    cout << nCk(J-1);  
}