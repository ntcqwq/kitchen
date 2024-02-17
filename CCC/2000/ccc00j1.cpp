#include <bits/stdc++.h>
using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;
const int inf = INT_MAX;

int main() {
    fastio;
    int a, b, d, l;
    cin >> a >> b;
    cout << "Sun Mon Tue Wed Thr Fri Sat" << endl;
    for (int i = 0; i < a-1; ++i) {
        cout << "    ";
    }
    l = 8-a;
    d = 1;
    while (d != b+1) {
        if (d < 10) {
            cout << "  " << d;
        } else {
            cout << " " << d;
        }
        if ((d-l) % 7 == 0) {
            cout << endl;
        } else {
            cout << " ";
        }
        d++;
    }
    return 0;
}