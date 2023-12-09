#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int h, M;

int main() {
	cheat;
	cin >> h >> M;
	int t = 1;
	while (M--) {
		int ans = -6 * pow(t, 4) + h * pow(t, 3) + 2 * t * t + t;
		if (ans <= 0) {
			cout << "The balloon first touches ground at hour:" << endl;
			cout << t << endl;
			return 0;
		}
		t++;
	}
	cout << "The balloon does not touch ground in the given time." << endl;
}
