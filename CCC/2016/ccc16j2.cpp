#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int main() {
	cheat;
	vector<pair<int, int>> s(4, {0, 0});
	for (int i = 0; i < 4; ++i) {
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		s[i].first += (a + b + c + d);
		s[0].second += a;
		s[1].second += b;
		s[2].second += c;
		s[3].second += d;
	}

	int ans = 0;
	int m = s[0].first;

	for (int i = 0; i < 4; ++i) {
		if (s[i].first == m) {
			ans++;
		}
		if (s[i].second == m) {
			ans++;
		}
	}

	if (ans != 8) {
		cout << "not ";
	}
	cout << "magic" << endl;
}