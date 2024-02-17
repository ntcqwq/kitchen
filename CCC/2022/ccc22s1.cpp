#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

const int mx = 1e5;

int N, ans;

int main() {
	fastio;
	cin >> N;
	while (N >= 0) {
		if (N % 5 == 0) {
			ans++;
		}
		N -= 4;
	}
	cout << ans << endl;
}