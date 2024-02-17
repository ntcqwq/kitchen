#include <bits/stdc++.h>
using namespace std;
#define endl "\n";
#define fio ios_base::sync_with_stdio(false); cin.tie(nullptr);
typedef long long ll;
const int inf = INT_MAX;

int main() {
    fio;
    string a, b;
    unordered_map<char, int> ans;
    cin >> a >> b;
    for (char c: a) {
        ans[c] += 1;
    }
    for (char c: b) {
        ans[c] -= 1;
    }
    int d = ans['*'];
    for (auto&c: ans) {
        d += max(c.second, 0);
    }
    cout << char((d<=0)?'A':'N');
}