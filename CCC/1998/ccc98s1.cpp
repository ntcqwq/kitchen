#include <bits/stdc++.h>
using namespace std;
#define endl "\n";
#define fio cin.tie(nullptr) -> sync_with_stdio(false); 
typedef long long ll;
const int inf = INT_MAX;

int main() {
    fio;
    int N;
    cin >> N;
    for (int i = 0; i <= N; ++i) {
        string l;
        getline(cin, l);
        stringstream ls(l);
        while (getline(ls, l, ' ')) {
            if (l.length() == 4) cout << "**** ";
            else cout << l << " ";
        }
        cout << endl;
    }
    return 0;
}