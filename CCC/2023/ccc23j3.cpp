#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

const int inf = numeric_limits<int>::max();

int main() {
    fastio;
    int N;
    cin >> N;
    vector<int> a(5);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 5; ++j) {
            char d;
            cin >> d;
            if (d == 'Y') {
                a[j]++;
            }
        }
    }
    int mD = 0;
    vector<int> d;
    for (int i = 0; i < 5; ++i) {
        if (mD < a[i]) {
            mD = a[i];
            d = {i};
        } else if (mD == a[i]) {
            d.push_back(i);
        }
    }

    cout << d[0]+1;
    d.erase(d.begin());


    for (int i: d) {
        cout << "," << i+1;
    }
    

    return 0;
}