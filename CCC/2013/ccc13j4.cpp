#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;

const int inf = numeric_limits<int>::max();

int main() {
    fastio;
    int T, C;
    cin >> T;
    cin >> C;
    vector<int> chores;

    for (int i = 0; i < C; i++) {
        int x;
        cin >> x;
        chores.push_back(x);
    }

    sort(chores.begin(), chores.end());

    int ans = 0;
    for (int i = 0; i < C; i++) {
        if (T - chores[i] >= 0) {
            T -= chores[i];
            ans++;
        }
    }

    cout << ans << endl;

    return 0;
}