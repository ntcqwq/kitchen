#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int t, s, h;

int main() {
	cheat;
	cin >> t >> s >> h;
	for (int i = 0; i < t; ++i) {
		cout << "*" << string(s, ' ') << "*" << string(s, ' ') << "*" << endl;
	}
	cout << string(3+s*2, '*') << endl;
	for (int i = 0; i < h; ++i) {
		cout << string(s+1, ' ') << "*" << endl;
	}
}