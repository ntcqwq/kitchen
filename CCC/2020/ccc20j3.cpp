#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;

const int inf = INT_MAX;

int main() {
	fastio;
	int N;
	cin >> N;
	int ax = -inf, ay = -inf, bx = inf, by = inf;
	while (N--) {
		int x, y;
		char c;
		cin >> x >> c >> y;
		ax = max(ax, x);
		ay = max(ay, y);
		bx = min(bx, x);
		by = min(by, y);
	}
	cout << bx-1 << "," << by-1 << endl;
	cout << ax+1 << "," << ay+1 << endl;
	return 0;
}