#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define cheat ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

int main() {
	cheat;
	int lo, hi;
	cin >> lo >> hi;
	int ans = 0;
	for (int n = lo; n <= hi; ++n) {
		int count = 2;
		for (int i = 2; i < n; ++i) {
			if (n % i == 0) {
				count++;
				if (count > 4) {
					break;
				}
			}
		}
		if (count == 4) {
			ans++;
		}
	}
	cout << "The number of RSA numbers between " << lo << " and " << hi << " is " << ans << endl;
}