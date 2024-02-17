#include <bits/stdc++.h>
using namespace std;
#define endl "\n";
#define fio cin.tie(nullptr) -> sync_with_stdio(false); 
typedef long long ll;
const int inf = INT_MAX;

int C, N, ans;
string r = "Casper";

int main() {
    fio;
    cin >> C;
    for (int i = 0; i < C; ++i) {
        int a, b;
        cin >> a >> b;
        ans = max(ans, a*b);
    }
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int a, b;
        cin >> a >> b;
        if (a*b > ans) {
            r = "Natalie";
            break;
        } else if (a*b == ans) {
            r = "Tie";
        }
    }
    cout << r; 
    return 0;
}