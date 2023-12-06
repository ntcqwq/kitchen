#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

const int inf = numeric_limits<int>::max();

int main() {
	fastio;
	int M;
    cin >> M;

    vector<vector<int>> seq(4*M);
    vector<int> v(M);

    for (int i = 0; i < M; i++) {
        cin >> v[i];
    }

    vector<int> mN, mX;
    vector<pair<int, int>> ans;
    int mL = -1;

    auto dif = [&](int x) { 
    	return v[x] - x + M;
    };

    for (int i = 0; i < M; i++) {
        while (!mN.empty() and v[mN.back()] > v[i]) {
            seq[dif(mN.back())].pop_back();
            mN.pop_back();
        }

        while (!mX.empty() and v[mX.back()] < v[i]) {
            mX.pop_back();
        }
        int a = dif(i);
        if (!seq[a].empty()) {
            int b = seq[a].back();
            if ((mX.empty() or mX.back() < b) and b > mL) {
                mL = b;
                ans.emplace_back(b, i);
            }
        }
        mN.emplace_back(i);
        mX.emplace_back(i);
        seq[a].emplace_back(i);
    }

    cout << ans.size() << endl;
    for (pair<int, int>i: ans) {
        cout << i.first + 1 << " " << i.second + 1 << endl;
    }

    return 0;
}