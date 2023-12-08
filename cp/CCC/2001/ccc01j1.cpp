#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int main() {
	fastio;
    int H;
	cin >> H;
	int r = 2 * H;
	int mid = (H + 1) / 2;
	for (int i = 1; i <= H; ++i) {
		int c = 4 * (abs(mid - i));
		int d = (r - c) / 2;
		cout << string(d, '*');
		cout << string(c, ' ');
		cout << string(d, '*') << endl;
	}
	return 0;
}