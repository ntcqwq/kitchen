#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;

const int inf = numeric_limits<int>::max();


int main() {
    fastio;
    int type, N;
    cin >> type >> N;
    
    vector<int> cD(N);
    vector<int> cP(N);

    for (int i = 0; i < N; i++) {
        cin >> cD[i];
    }

    for (int i = 0; i < N; i++) {
        cin >> cP[i];
    }

    int speed = 0;

    if (type == 1) {
        sort(cD.begin(), cD.end());
        sort(cP.begin(), cP.end());
        for (int C = 0; C < N; C++) {
            speed += max(cD[C], cP[C]);
        }
    }
    else if (type == 2) {
        sort(cD.begin(), cD.end());
        sort(cP.begin(), cP.begin() + N, greater<int>());
        for (int C = 0; C < N; C++) {
            speed += max(cD[C], cP[C]);
        }
    }

    cout << speed << endl;

    return 0;
}