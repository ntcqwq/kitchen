#include <bits/stdc++.h>
using namespace std;
#define endl "\n";
#define fio cin.tie(nullptr) -> sync_with_stdio(false); 

typedef long long ll;
const int inf = INT_MAX;

int main() {
    fio;
    int N, ans = inf;
    cin >> N;
    vector<pair<int, int>> p(N);
    for (int i = 0; i < N; ++i) {
        cin >> p[i].first >> p[i].second;
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i != j) ans = min(ans, max(abs(p[i].first-p[j].first), abs(p[i].second-p[j].second)));
        }
    }
    cout << ans*ans;
    return 0;
}