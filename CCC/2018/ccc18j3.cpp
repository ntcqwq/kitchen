#include <bits/stdc++.h>

using namespace std;

#define endl "\n"
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr)

typedef string str;
typedef long long ll;

const float inf = numeric_limits<float>::infinity();

int main() {
	fastio;
	vector<int> N(5);
	cin >> N[1] >> N[2] >> N[3] >> N[4];
	for (int i = 1; i < 5; ++i) {
		N[i] += N[i-1];
	}
	for (int n = 0; n < 5; ++n) {
		for (int i = 0; i < 5; ++i) {
			cout << abs(N[n]-N[i]) << " ";
		}
		cout << endl;
	}
}